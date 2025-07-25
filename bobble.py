import tkinter as tk
from tkinter import messagebox
import csv
import os

# Define CSV file path
CSV_FILE = "bobble_game_data.csv"

def save_data():
    player = entry_player.get().strip()
    score = entry_score.get().strip()
    date = entry_date.get().strip()

    if not player or not score or not date:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return
    
    # Validate score is an integer
    if not score.isdigit():
        messagebox.showwarning("Input Error", "Score must be a number.")
        return

    # Write header if file doesn't exist
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Player", "Score", "Date"])
        writer.writerow([player, score, date])

    messagebox.showinfo("Success", "Data saved successfully!")

    # Clear inputs
    entry_player.delete(0, tk.END)
    entry_score.delete(0, tk.END)
    entry_date.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Bobble Game Data Entry")

# Create labels and entries
tk.Label(root, text="Player Name:").grid(row=0, column=0, padx=10, pady=5)
entry_player = tk.Entry(root)
entry_player.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Score:").grid(row=1, column=0, padx=10, pady=5)
entry_score = tk.Entry(root)
entry_score.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
entry_date = tk.Entry(root)
entry_date.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=save_data)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
