import os
import tkinter as tk

import menu as m  # Import the menu module

def main():

    # Create the main application window
    root = tk.Tk()
    root.title("J*b Tracker")  # Set window title
    root.geometry("1000x707")  # Set window size

    m.create_menu(root)  # Call the function to create the menu
    job_title = tk.Entry(root, width=50)  # Create an entry widget for job title
    job_title.pack(pady=10)  # Add some padding around the entry widget

    add_button = tk.Button(root, text="Add Task", command=lambda: job_title.delete(0, tk.END))  # Button to add tasks
    add_button.pack()  # Display the button

    

    # Run the application
    root.mainloop()

if __name__ == "__main__":    main()
