import tkinter as tk
import random

class NewYearApp:
    def __init__(self, root):
        self.root = root
        root.title("Happy New Year Countdown")
        root.geometry("600x400")
        # Changed background to deep navy
        root.configure(bg="#0b1a4d")
        
        self.count = 10
        self.flash_on = True

        # Create canvas for shapes
        self.canvas = tk.Canvas(root, width=600, height=300, bg="#0b1a4d", highlightthickness=0)
        self.canvas.pack()

        # Label for countdown and message with italic and bold font
        self.label = tk.Label(root, text="Countdown: 10",
                              font=("Helvetica", 30, "bold italic"), fg="#FFD700", bg="#0b1a4d")
        self.label.pack(pady=10)

        self.countdown()

    def countdown(self):
        self.canvas.delete("all")
        self.draw_random_shapes(10)
        if self.count > 0:
            self.label.config(text=f"Countdown: {self.count}", fg="#FFD700", font=("Helvetica", 30, "bold italic"))
            self.count -= 1
            self.root.after(1000, self.countdown)
        else:
            self.flash_text()

    def flash_text(self):
        self.canvas.delete("all")
        self.draw_random_shapes(15)
        if self.flash_on:
            # Italic and bold for the Happy New Year message
            self.label.config(text="🎉 Happy New Year! 🎉", fg="#FF4500",
                              font=("Helvetica", 32, "bold italic"))
        else:
            self.label.config(text="", fg="#0b1a4d")
        self.flash_on = not self.flash_on
        self.root.after(500, self.flash_text)

    def draw_random_shapes(self, count):
        colors = ["#FF6347", "#FFD700", "#40E0D0", "#9ACD32", "#FF69B4", "#1E90FF"]
        for _ in range(count):
            shape_type = random.choice(["circle", "rectangle", "triangle"])
            x1 = random.randint(10, 580)
            y1 = random.randint(10, 280)
            size = random.randint(20, 50)
            color = random.choice(colors)

            if shape_type == "circle":
                self.canvas.create_oval(x1, y1, x1+size, y1+size, fill=color, outline="")
            elif shape_type == "rectangle":
                self.canvas.create_rectangle(x1, y1, x1+size, y1+size, fill=color, outline="")
            elif shape_type == "triangle":
                points = [x1, y1+size, x1 + size/2, y1, x1 + size, y1+size]
                self.canvas.create_polygon(points, fill=color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewYearApp(root)
    root.mainloop()
