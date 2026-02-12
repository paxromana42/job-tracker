import TUI as tui  # Import the menu module

def main():
    database_location = "database/app-repo.db"
    exports_location = "exports"

    while True:
        choice_tuple = tui.TUI_start(database_location, exports_location)
        
        if choice_tuple is None:
            tui.TUI_end()
            break

        tui.clear_screen()
        tui.main_menu(choice_tuple, database_location)

        input("\nPress Enter to continue...")
        tui.spacing_buffer()


if __name__ == "__main__":    main()
