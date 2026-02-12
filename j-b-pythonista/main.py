import os
import tkinter as tk

from altair import selection

import TUI as tui  # Import the menu module

def main():
    database_location = "database/app-repo.db"  # Define the path to the database file
    selection = tui.TUI_start(database_location)  # Start the Text User Interface (TUI)

    tui.spacing_buffer()  # Add spacing in the terminal for better readability

    tui.main_menu(selection, database_location)  # Call the menu function with the user's selection

    tui.spacing_buffer()  # Add spacing in the terminal for better readability
    tui.TUI_end()  # End the Text User Interface (TUI)



if __name__ == "__main__":    main()
