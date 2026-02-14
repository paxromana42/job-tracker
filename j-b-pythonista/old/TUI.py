import os
import pyfiglet
import database_logic
import csv
import pathlib as plib
import textwrap



# TUI

def TUI_start(path_to_db, path_exports="exports"):
    db_exist = check_database_exists(path_to_db)  # Check if the database exists before starting the application
    export_exist = check_export_exists(path_exports)

    logo()  # Display the logo when starting the application

    print("\nWelcome to J*b Tracker! Your personal job application tracker. Using this tool, make sure to track all the details of your j*b applications. To protect your poor eyes, the word j*b will be censored as it should be. This is as functional as you make it, so have fun.\n")  # Welcome message

    print("\nPlease select an option:")

    if db_exist:
        print("\t1. Add new application")
        print("\t2. View applications")
        print("\t3. Bulk import CSV")
        print("\t4. Update status")
        print("\t5. View updates")

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
    print("Add New Application")

    title = safe_input("Title: ")
    company = safe_input("Company: ")

    posted = safe_input("Posted Date (YYYY-MM-DD, leave blank if unknown): ")
    if not posted:
        posted = None

    location = safe_input("Location: ")
    source = safe_input("Source: ")
    link = safe_input("Link: ")

    wage_min = safe_input("Min Pay: ")
    wage_max = safe_input("Max Pay: ")
    freq = safe_input("Pay Frequency (hourly/monthly/yearly): ")
    hours = safe_input("Hours per week: ")

    database_logic.add_application(
        db_path,
        title,
        company,
        posted,
        location,
        source,
        link,
        float(wage_min) if wage_min else None,
        float(wage_max) if wage_max else None,
        freq,
        int(hours) if hours else None
    )

def table(db_path):
    rows = database_logic.get_applications(db_path)

    if not rows:
        print("No applications found.")
        return

    print("\nID | Title | Company | Status | Created")
    print("-" * 80)

    for r in rows:
        print(f"{r[0]:<3} | {r[1][:20]:<20} | {r[2][:15]:<15} | {r[3]:<10} | {r[4]}")


def spacing_buffer():
    print("\n" * 4)  # Print multiple newlines to create spacing in the terminal

def main_menu(selection_tuple, db_path):
    choice, db_exists = selection_tuple

    if db_exists:
        if choice == "1":
            new_query(db_path)
        elif choice == "2":
            table(db_path)
        elif choice == "3":
            bulk_add(db_path)
        elif choice == "4":
            update_status(db_path)
        elif choice == "5":
            show_updates(db_path)
    else:
        if choice == "1":
            database_logic.create_database_file(str(db_path))
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
    # ---- Manifesto ----
    try:
        with open("help_info/manifesto.txt", encoding="utf-8") as f:
            print_wrapped(f.read())
    except FileNotFoundError:
        print("Manifesto not found.")

    pause()

    # ---- Attributes ----
    spacing_buffer()
    print("=== ATTRIBUTES ===")
    print_csv_table("help_info/attributes.csv")
    pause()

    # ---- Inputs ----
    spacing_buffer()
    print("=== INPUT FIELDS ===")
    print_csv_table("help_info/input_fields.csv")
    pause()

    # ---- Calculations ----
    spacing_buffer()
    print("=== CALCULATED VALUES ===")
    print_csv_table("help_info/calc_fields.csv")
    pause()

    # ---- Functions ----
    spacing_buffer()
    generate_function_docs()
    print("=== FUNCTIONS ===")
    try:
        with open("help_info/functions.txt", encoding="utf-8") as f:
            print_wrapped(f.read())
    except FileNotFoundError:
        print("Functions file not found.")

    pause()

def add_update(db_path):
    app_id = input("Application ID: ")
    status = input("New status: ")
    note = input("Note (optional): ")

    import datetime
    timestamp = datetime.datetime.now().isoformat()

    database_logic.insert_update(db_path, app_id, timestamp, status, note)


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

def pause():
    input("\nPress ENTER to continue...")

def print_wrapped(text, width=None):
    width = width or os.get_terminal_size().columns - 4

    for paragraph in text.split("\n\n"):
        print(textwrap.fill(paragraph, width))
        print()

def import_csv(db_path):
    file_path = input("Enter CSV path: ")

    try:
        with open(file_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                database_logic.insert_application(
                    db_path,
                    row.get("created_at"),
                    row.get("title"),
                    row.get("company"),
                    row.get("location"),
                    row.get("source"),
                    row.get("link")
                )

        print("Import complete.")
    except Exception as e:
        print(f"Import failed: {e}")


def print_csv_table(file_path, max_width=25):
    data = read_csv_safely(file_path)

    if not data:
        print("No data found.")
        return

    headers = list(data[0].keys())

    # ---- Determine column widths ----
    col_widths = {}
    for h in headers:
        max_len = max(len(str(row[h])) for row in data)
        col_widths[h] = min(max(max_len, len(h)), max_width)

    # ---- Print header ----
    header_line = " | ".join(h.ljust(col_widths[h]) for h in headers)
    print(header_line)
    print("-" * len(header_line))

    # ---- Print rows with wrapping ----
    for row in data:
        wrapped_cells = []

        # Wrap each cell
        for h in headers:
            cell = str(row[h])
            wrapped = textwrap.wrap(cell, width=col_widths[h]) or [""]
            wrapped_cells.append(wrapped)

        # Determine row height (max lines)
        max_lines = max(len(cell) for cell in wrapped_cells)

        # Print each line of the row
        for i in range(max_lines):
            line_parts = []
            for j, h in enumerate(headers):
                cell_lines = wrapped_cells[j]
                if i < len(cell_lines):
                    line_parts.append(cell_lines[i].ljust(col_widths[h]))
                else:
                    line_parts.append(" " * col_widths[h])
            print(" | ".join(line_parts))

        print("-" * len(header_line))

def bulk_add(db_path):
    path = input("CSV file path: ")
    database_logic.bulk_insert_from_csv(db_path, path)

def table(db_path):
    database_logic.view_applications(db_path)

def update_status(db_path):
    app_id = safe_input("Application ID")
    if app_id is None:
        return

    status = safe_input("New Status")
    if status is None:
        return

    note = safe_input("Note", allow_empty=True)

    database_logic.add_update(db_path, int(app_id), status, note)


def show_updates(db_path):
    app_id = input("Application ID: ")
    database_logic.view_updates(db_path, int(app_id))

def safe_input(prompt, allow_empty=False):
    while True:
        val = input(prompt + " (or type 'q' to cancel): ")

        if val.lower() == "q":
            return None

        if not val and not allow_empty:
            print("Input cannot be empty.")
            continue

        return val

def follow_up_menu(db_path):
    rows = database_logic.follow_up_candidates(db_path)

    if not rows:
        print("No follow-ups needed.")
        return

    for r in rows:
        print(r)

def get_int(prompt):
    while True:
        val = input(prompt)

        if val.lower() == "q":
            return None

        try:
            return int(val)
        except:
            print("Enter a valid number.")

def generate_function_docs():
    import inspect

    for name, func in inspect.getmembers(database_logic, inspect.isfunction):
        print(f"{name}: {func.__doc__}")
