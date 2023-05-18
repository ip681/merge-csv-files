import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
from datetime import datetime


def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")])
    for file_path in file_paths:
        file_list.insert(tk.END, file_path)


def merge_csv_files():
    file_paths = file_list.get(0, tk.END)
    merged_data = pd.concat([pd.read_csv(file) for file in file_paths])

    # Get the path to the "Downloads" folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Generate the name of the merged CSV file with date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    merged_csv_name = f"merged_{current_datetime}.csv"
    merged_csv_path = os.path.join(downloads_folder, merged_csv_name)

    # Save the merged CSV file
    merged_data.to_csv(merged_csv_path, index=False)


def clear_files():
    file_list.delete(0, tk.END)


def show_instructions():
    instructions = """
    Instructions for working with the program:

      1. Click the "Load Files" button to select CSV files you want to merge.
      2. Select one or more files from the file open window.
      3. Click the "Merge" button to merge the selected files into one CSV file.
      4. The merged CSV file will be saved in the Downloads directory.
      5. Click the "Clear" button if you want to clear the list of loaded files to load others.

      When selecting files, they can be selected multiple times.

      Once you have selected one or more files, others can be added to them. This can be useful if the others are in a separate directory.
    """
    messagebox.showinfo("Instruction", instructions)


window = tk.Tk()
window.title("Merge CSV Files")

file_list = tk.Listbox(window)
file_list.config(width=60)
file_list.grid(row=0, column=0, columnspan=4)

select_button = tk.Button(window, text="Load files", command=select_files)
select_button.configure(font=("Arial", 14), foreground="white", background="blue")
select_button.grid(row=1, column=0)

merge_button = tk.Button(window, text="Merge", command=merge_csv_files)
merge_button.configure(font=("Arial", 14), foreground="white", background="blue")
merge_button.grid(row=1, column=1)

clear_button = tk.Button(window, text="Clean", command=clear_files)
clear_button.configure(font=("Arial", 14), foreground="white", background="blue")
clear_button.grid(row=1, column=2)

instructions_button = tk.Button(window, text="Instruction", command=show_instructions)
instructions_button.configure(font=("Arial", 14), foreground="white", background="blue")
instructions_button.grid(row=1, column=3)

window.mainloop()