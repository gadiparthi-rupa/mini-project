import tkinter as tk
from tkinter import messagebox
import csv
import os

class MarriageInvitationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Marriage Invitation Data Entry")

        # Labels and Entry widgets for data
        tk.Label(root, text="Bride Name").grid(row=0, column=0, padx=10, pady=5)
        self.bride_name = tk.Entry(root)
        self.bride_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Groom Name").grid(row=1, column=0, padx=10, pady=5)
        self.groom_name = tk.Entry(root)
        self.groom_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)
        self.date = tk.Entry(root)
        self.date.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Venue").grid(row=3, column=0, padx=10, pady=5)
        self.venue = tk.Entry(root)
        self.venue.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Contact Number").grid(row=4, column=0, padx=10, pady=5)
        self.contact = tk.Entry(root)
        self.contact.grid(row=4, column=1, padx=10, pady=5)

        # Submit Button
        submit_btn = tk.Button(root, text="Submit", command=self.save_data)
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)

    def save_data(self):
        data = {
            "Bride Name": self.bride_name.get(),
            "Groom Name": self.groom_name.get(),
            "Date": self.date.get(),
            "Venue": self.venue.get(),
            "Contact Number": self.contact.get(),
        }

        # Basic validation
        if not all(data.values()):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        file_exists = os.path.isfile('marriage_invitations.csv')
        with open('marriage_invitations.csv', 'a', newline='') as csvfile:
            fieldnames = ["Bride Name", "Groom Name", "Date", "Venue", "Contact Number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)

        messagebox.showinfo("Success", "Invitation data saved successfully!")

        # Clear fields
        self.bride_name.delete(0, tk.END)
        self.groom_name.delete(0, tk.END)
        self.date.delete(0, tk.END)
        self.venue.delete(0, tk.END)
        self.contact.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MarriageInvitationApp(root)
    root.mainloop()
