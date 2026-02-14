import os
import pathlib as plib

# Better input function that includes an escape and a protection against blank values where it is not expected.
def safe_input(prompt, allow_empty=False):
    while True:
        val = input(prompt + " (or type 'q' to cancel): ")

        if val.lower() == "q":
            return None

        if not val and not allow_empty:
            print("Input cannot be empty.")
            continue

        return val

# Integer input validation
def get_int(prompt):
    while True:
        val = input(prompt)

        if val.lower() == "q":
            return None

        try:
            return int(val)
        except:
            print("Enter a valid number.")

# Pause input
def pause():
    input("\nPress ENTER to continue...")

# Clear terminal window

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen based on the operating system

# Spacing
def spacing_buffer():
    print("\n" * 4)  # Print multiple newlines to create spacing in the terminal

# Does the database exist?
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

def check_export_exists_n_empty(path_to_exports):
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

