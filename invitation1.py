import tkinter as tk
from tkinter import messagebox
import csv
import os

class FestivalInvitationApp:
    def __init__(self, root):
        self.root = root
        root.title("Festival Invitation Data Maintenance")
        root.geometry("400x350")
        root.configure(bg="#f7f7f7")

        # Labels and Entries
        tk.Label(root, text="Name:", bg="#f7f7f7").pack(pady=(15, 0))
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Festival:", bg="#f7f7f7").pack(pady=(10, 0))
        self.festival_entry = tk.Entry(root, width=40)
        self.festival_entry.pack(pady=5)

        tk.Label(root, text="Date (YYYY-MM-DD):", bg="#f7f7f7").pack(pady=(10, 0))
        self.date_entry = tk.Entry(root, width=40)
        self.date_entry.pack(pady=5)

        tk.Label(root, text="Contact Number:", bg="#f7f7f7").pack(pady=(10, 0))
        self.contact_entry = tk.Entry(root, width=40)
        self.contact_entry.pack(pady=5)

        # Submit Button
        submit_btn = tk.Button(root, text="Submit", command=self.submit_data, bg="#4caf50", fg="white", width=15)
        submit_btn.pack(pady=20)

    def submit_data(self):
        name = self.name_entry.get().strip()
        festival = self.festival_entry.get().strip()
        date = self.date_entry.get().strip()
        contact = self.contact_entry.get().strip()

        # Simple validation
        if not name or not festival or not date or not contact:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        # CSV file path
        file_exists = os.path.isfile("festival_invitations.csv")
        
        try:
            with open("festival_invitations.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                # Write header if file is new
                if not file_exists:
                    writer.writerow(["Name", "Festival", "Date", "Contact Number"])
                # Write data row
                writer.writerow([name, festival, date, contact])
            
            messagebox.showinfo("Success", "Data saved successfully!")

            # Clear entries after successful submission
            self.name_entry.delete(0, tk.END)
            self.festival_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FestivalInvitationApp(root)
    root.mainloop()
