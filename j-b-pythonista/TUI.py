import os
import pyfiglet
import textwrap
import services as ss

# TUI

# Global Terminal values
# Global values
usable_terminal = os.get_terminal_size().columns - 4

# ======== Start Loop ==========


# Start TUI. Take the path to database as input and the exports
def TUI_start(path_db, path_exports="exports"):
    # Check if the relevant folders exist and make them do so if not
    db_exist = ss.check_database_exists(path_db)
    export_exist = ss.check_export_exists_n_empty(path_exports)

    # Print the Logo
    logo()

    # Welcome message
    print_wrapped("\nWelcome to J*b Tracker! Your personal job application tracker. Using this tool, make sure to track all the details of your j*b applications. To protect your poor eyes, the word j*b will be censored as it should be. This is as functional as you make it, so have fun.\n")  # Welcome message

    print("\nPlease select an option:")

def logo():
    logo = pyfiglet.figlet_format(text="J*b Tracker")  # Create ASCII art for the application name

    # Calculate usable width for the separator
    separator = "*" * (usable_terminal)  # Create a separator line based on terminal width
    indented_logo = "\n".join(
        line.center(usable_terminal)
        for line in logo.splitlines()
        )

    print(separator, indented_logo,separator, sep="\n")  # Print the separator, logo, and another separator


# Menu logic

def menu_renderer(db_path, export_directory, no_db, empty_exports):
    pass

# ====== Table Renderer =======
def view_applications_ui(db_path):
    rows = ss.list_applications(db_path)

    if not rows:
        print("No applications found.")
        ss.pause()
        return

    print("\nID | Title | Company | Pay | Created")
    print("-" * 60)

    for r in rows:
        pay = f"{r[4]}-{r[5]} {r[6]}" if r[4] else "-"
        print(f"{r[0]} | {r[1]} | {r[2]} | {pay} | {r[7][:10]}")

    ss.pause()


# ======= Terminal logic =======

def print_wrapped(text, width=usable_terminal):
    for paragraph in text.split("\n\n"):
        print(textwrap.fill(paragraph, width))
        print()

def TUI_end():
    ss.spacing_buffer()
    print("Thank you for using J*b Tracker! Goodbye!\n")
    logo()  # Display the logo when exiting the application
    exit()