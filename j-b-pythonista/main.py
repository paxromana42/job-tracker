import TUI as tui

# Main function loop
def main():
    db_path = "database/app-repo.db"

    while True:
        choice_tuple = tui.TUI_start(db_path)

        if not choice_tuple:
            break

        tui.main_menu(choice_tuple, db_path)

    tui.TUI_end()

if __name__ == "__main__":    main()
