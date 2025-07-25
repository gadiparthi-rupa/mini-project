import tkinter as tk
from tkinter import messagebox
import csv

def save_data():
    name = name_entry.get()
    date = date_entry.get()
    status = status_var.get()

    if name and date and status:
        with open("attendance.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, date, status])
        messagebox.showinfo("Success", "Attendance saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

root = tk.Tk()
root.title("Attendance Management")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Date:").grid(row=1, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=1, column=1)

tk.Label(root, text="Status:").grid(row=2, column=0)
status_var = tk.StringVar(value="Present")
tk.Radiobutton(root, text="Present", variable=status_var, value="Present").grid(row=2, column=1)
tk.Radiobutton(root, text="Absent", variable=status_var, value="Absent").grid(row=2, column=2)

# Save Button
save_button = tk.Button(root, text="Save Attendance", command=save_data)
save_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
