import tkinter as tk
from tkinter import messagebox
import csv
import os

# File path
CSV_FILE = "students.csv"

# Function to write data to CSV
def save_data():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    dept = entry_dept.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if not (name and age and gender and dept and email and phone):
        messagebox.showerror("Input Error", "All fields are required!")
        return

    # Save to CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Age', 'Gender', 'Department', 'Email', 'Phone'])
        writer.writerow([name, age, gender, dept, email, phone])

    messagebox.showinfo("Success", "Student data saved!")
    clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set(None)
    entry_dept.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Student Biodata Entry")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Student Biodata Form", font=('Arial', 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Department").pack()
entry_dept = tk.Entry(root)
entry_dept.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Phone Number").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Submit button
tk.Button(root, text="Submit", command=save_data).pack(pady=20)

root.mainloop()
