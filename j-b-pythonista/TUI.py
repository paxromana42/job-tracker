import os
from unittest import case
import pyfiglet
import database_logic
import csv
import pathlib as plib


# TUI

def TUI_start(path_to_db, path_exports="exports"):
    db_exist = check_database_exists(path_to_db)  # Check if the database exists before starting the application
    export_exist = check_export_exists(path_exports)

    logo()  # Display the logo when starting the application

    print("\nWelcome to J*b Tracker! Your personal job application tracker. Using this tool, make sure to track all the details of your j*b applications. To protect your poor eyes, the word j*b will be censored as it should be. This is as functional as you make it, so have fun.\n")  # Welcome message

    print("\nPlease select an option:")

    if db_exist:
        print("\t1. Add a new application")
        print("\t2. View all applications")
    else:
        print("\t1. Create Application database file")
        print("\t2. Point to an existing database file")
    print("\t3. Help 0o0")
    print("\t4. Exit :)")

    start_input = input("Enter your choice: ")  # Get user input for menu selection

    if start_input == "4":
        return

    return (start_input, db_exist) # Return the user's selection for further processing in the main function


def TUI_end():
    spacing_buffer()
    print("Thank you for using J*b Tracker! Goodbye!\n")
    logo()  # Display the logo when exiting the application
    exit()

def new_query(db_path):
    print("NEW QUERY — to be implemented")

def table(db_path):
    print("TABLE VIEW — to be implemented")

def spacing_buffer():
    print("\n" * 4)  # Print multiple newlines to create spacing in the terminal

def main_menu(selection_tuple, db_path):
    choice, db_exists = selection_tuple

    if choice == "3":
        help_background()
    elif db_exists:
        if choice == "1":
            new_query(db_path)
        elif choice == "2":
            table(db_path)
        else:
            print("Invalid choice.")
    else:
        if choice == "1":
            database_logic.create_database_file(plib.Path(db_path))
        elif choice == "2":
            new_path = input("Enter path to existing database: ")
            TUI_start(new_path)
        else:
            print("Invalid choice.")

def check_database_exists(path_to_db):
    if os.path.exists("database") or os.path.exists(plib.Path(path_to_db).parent):
        print("\nDatabase folder exists.")
        if os.path.exists(path_to_db) and plib.Path(path_to_db).name:
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

def check_export_exists(path_to_exports):
    if os.path.exists("exports"):
        print("\nExports folder exists.", end=" ")
        if len(os.listdir(path_to_exports)) > 0:  # Check if the exports folder is not empty:
            print("It is not empty. There may be a conflict with existing export files. Please check the exports folder before exporting new data.")
            return True
        else:
            print("It is empty! No Conflict management needed :) yet :(")
            return False
    else:
        print("Exports folder does not exist. Creating exports folder...")
        os.makedirs("exports", exist_ok=True)
        print("Exports folder created.")
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen based on the operating system


# Displays the information the J*b tracker relevant to the TUI, ommiting the C++ information in the README. This will at a minimum print the manifesto, the input fields, the calculated fields, the export options and the functions.
def help_background():
    with open("help_info/manifesto.txt") as f:
        print(f.read())
    os.system("pause")

    spacing_buffer()
    print("Here is information on the attributes of the entities we will be storing:")
    read_csv_safely("help_info/attributes.csv")
    os.system("pause")

    spacing_buffer()
    print("Here is the information on the inputs")
    read_csv_safely("help_info/input_fields.csv")
    os.system("pause")

    spacing_buffer()
    print("Here is the information on the calculted returns")
    read_csv_safely("help_info/calc_fields.csv")
    os.system("pause")

    spacing_buffer()
    print("Here is the information on the functions in this program")
    read_csv_safely("help_info/functions.txt")

# I had no idea how to do this, so I got this function from here: https://www.owais.io/blog/2025-09-23_python-csv-complete-beginners-guide-terminal/
def read_csv_safely(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = []

            for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 (after header)
                try:
                    # Process row with validation
                    if not row['name'].strip():
                        print(f"Warning: Empty name in row {row_num}")
                        continue

                    data.append(row)

                except KeyError as e:
                    print(f"Missing column {e} in row {row_num}")
                except ValueError as e:
                    print(f"Invalid data in row {row_num}: {e}")

            return data

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return []
    except PermissionError:
        print(f"Error: Permission denied accessing '{file_path}'")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
