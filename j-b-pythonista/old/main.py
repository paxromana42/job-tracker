from pathlib import Path
import TUI as tui  # Import the menu module

database_location = Path("database/app-repo.db")
exports_location = Path("exports")

def main():
    while True:
        tui.clear_screen()

        selection = tui.TUI_start(database_location, exports_location)

        if selection is None:
            tui.TUI_end()

        tui.main_menu(selection, database_location)

        input("\nPress Enter to continue...")


if __name__ == "__main__":    main()
