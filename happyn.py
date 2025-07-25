import tkinter as tk
import random

class NewYearApp:
    def __init__(self, root):
        self.root = root
        root.title("Happy New Year Countdown")
        root.geometry("600x400")
        # Set background color to yellow
        root.configure(bg="#FFD700")
        
        self.count = 10
        self.flash_on = True

        # Create canvas with yellow background
        self.canvas = tk.Canvas(root, width=600, height=300, bg="#FFD700", highlightthickness=0)
        self.canvas.pack()

        # Label for countdown and message with italic and bold font
        self.label = tk.Label(root, text="Countdown: 10",
                              font=("Helvetica", 30, "bold italic"), fg="#8B4513", bg="#FFD700")
        self.label.pack(pady=10)

        self.countdown()

    def countdown(self):
        self.canvas.delete("all")
        self.draw_flowers(12)
        if self.count > 0:
            self.label.config(text=f"Countdown: {self.count}", fg="#8B4513",
                              font=("Helvetica", 30, "bold italic"))
            self.count -= 1
            self.root.after(1000, self.countdown)
        else:
            self.flash_text()

    def flash_text(self):
        self.canvas.delete("all")
        self.draw_flowers(20)
        if self.flash_on:
            # Italic and bold for the Happy New Year message
            self.label.config(text="🎉 Happy New Year! 🎉", fg="#B22222",
                              font=("Helvetica", 32, "bold italic"))
        else:
            self.label.config(text="", fg="#FFD700")
        self.flash_on = not self.flash_on
        self.root.after(500, self.flash_text)

    def draw_flowers(self, count):
        # Draw simple flowers as circles (center) and petals (ovals)
        petal_colors = ["#FF69B4", "#FF4500", "#FF8C00", "#FF1493", "#FF6347"]
        center_color = "#FFDAB9"

        for _ in range(count):
            x = random.randint(50, 550)
            y = random.randint(50, 250)
            size = random.randint(15, 25)

            # Draw petals around center
            petal_offsets = [
                (-size, 0), (size, 0),
                (0, -size), (0, size),
                (-size*0.7, -size*0.7), (size*0.7, -size*0.7),
                (-size*0.7, size*0.7), (size*0.7, size*0.7)
            ]
            petal_color = random.choice(petal_colors)

            for dx, dy in petal_offsets:
                self.canvas.create_oval(x+dx, y+dy, x+dx+size, y+dy+size,
                                        fill=petal_color, outline="")

            # Draw center circle
            self.canvas.create_oval(x, y, x+size, y+size,
                                    fill=center_color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewYearApp(root)
    root.mainloop()
