import os
from unittest import case
import pyfiglet
import database_logic


# TUI

def TUI_start(path_to_db):
    exist = check_database_exists(path_to_db)  # Check if the database exists before starting the application

    logo()  # Display the logo when starting the application

    print("\nWelcome to J*b Tracker! Your personal job application tracker. Using this tool, make sure to track all the details of your job applications.\n")  # Welcome message

    print("\nPlease select an option:")

    if exist:
        print("\t1. Add a new application")
        print("\t2. View all applications")
    else:
        print("\t1. Create Application database file")
        print("\t2. Point to an existing database file")
    print("\t3. Exit :)")

    start_input = input("Enter your choice: ")  # Get user input for menu selection

    if start_input == "3":
        return

    return (start_input, exist) # Return the user's selection for further processing in the main function


def TUI_end():
    print("Thank you for using J*b Tracker! Goodbye!\n")
    logo()  # Display the logo when exiting the application
    exit()

def new_query():
    pass

def table():
    pass

def spacing_buffer():
    print("\n" * 5)  # Print multiple newlines to create spacing in the terminal

def main_menu(selection, database_location):
    clear_screen()  # Clear the terminal screen before displaying the menu
    if selection == "1 True":
        new_query()
    elif selection == "2 True":
        table()
    elif selection == "1 False":
        create_database_file()
    elif selection == "2 False":
        print("Please point to an existing database file to make use of J*b Tracker.")
        TUI_start(input("Write the path to the existing database file (absolute or relative): "))
        

def check_database_exists(path_to_db):
    if os.path.isdir("database"):
        print("\nDatabase folder exists.")
        if os.path.isfile(path_to_db):
            print("Database file exists.")
            return True
        else:
            print("Database file does not exist. Please create the database file to make use of J*b Tracker.")
            return False
    else:
        print("Database folder does not exist. Creating database folder...")
        os.makedirs("database", exist_ok=True)
        print("Database folder created. Please create the database file to make use of J*b Tracker.")
        return False

def logo():
    logo = pyfiglet.figlet_format(text="J*b Tracker")  # Create ASCII art for the application name

    terminal_width = os.get_terminal_size().columns
    usable_width = terminal_width - 4  # Calculate usable width for the separator
    separator = "*" * (usable_width)  # Create a separator line based on terminal width
    indented_logo = "\n".join(
        line.center(usable_width)
        for line in logo.splitlines()
        )

    print(separator, indented_logo,separator, sep="\n")  # Print the separator, logo, and another separator

def create_database_file():
    print("Creating database file...")
    # Code to create the database file goes here
    database_logic.create_database_file("database/app-repo.db")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen based on the operating system

