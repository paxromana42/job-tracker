import tkinter as tk

def create_menu(root):
    app_menu_title = tk.Label(root, text="J*b Tracker", font=("Roboto", 25))  # Create a title label
    app_menu_title.pack(pady=10)  # Add some padding around the title label

    menu_bar = tk.Menu(root)  # Create a menu bar
    root.config(menu=menu_bar)  # Set the menu bar for the root window

    file_menu = tk.Menu(menu_bar, tearoff=0)  # Create a "File" menu
    file_menu.add_command(label="New", command=lambda: print("New File"))  # Add "New" option
    file_menu.add_command(label="Open", command=lambda: print("Open File"))  # Add "Open" option
    file_menu.add_separator()  # Add a separator line
    file_menu.add_command(label="Exit", command=root.quit)  # Add "Exit" option to close the application
    
    

    menu_bar.add_cascade(label="File", menu=file_menu)  # Add the "File" menu to the menu bar