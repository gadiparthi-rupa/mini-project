import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.width = 500
        self.height = 500
        self.cell_size = 20

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Initialize game state
        self.direction = "Right"
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]  # list of (x,y) tuples
        self.food_position = self.set_new_food_position()
        self.score = 0

        # Display score
        self.score_text = self.canvas.create_text(45, 12, text=f"Score: {self.score}", fill="white", font=('Arial', 14))

        # Start game loop
        self.game_running = True
        self.root.bind("<Key>", self.change_direction)
        self.perform_actions()

    def set_new_food_position(self):
        while True:
            x = random.randrange(0, self.width, self.cell_size)
            y = random.randrange(0, self.height, self.cell_size)
            if (x, y) not in self.snake_positions:
                return (x, y)

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = ("Up", "Down", "Left", "Right")
        opposites = (("Up", "Down"), ("Left", "Right"))
        
        if new_direction in all_directions:
            # Prevent snake from reversing
            if (self.direction, new_direction) not in opposites and (new_direction, self.direction) not in opposites:
                self.direction = new_direction

    def perform_actions(self):
        if self.game_running:
            self.move_snake()
            self.check_collisions()
            self.check_food_collision()
            self.update_canvas()
            self.root.after(100, self.perform_actions)
        else:
            self.game_over()

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]

        if self.direction == "Left":
            new_head = (head_x - self.cell_size, head_y)
        elif self.direction == "Right":
            new_head = (head_x + self.cell_size, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - self.cell_size)
        elif self.direction == "Down":
            new_head = (head_x, head_y + self.cell_size)

        self.snake_positions = [new_head] + self.snake_positions[:-1]

    def check_collisions(self):
        head_x, head_y = self.snake_positions[0]

        # Check walls
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            self.game_running = False

        # Check self collision
        if self.snake_positions[0] in self.snake_positions[1:]:
            self.game_running = False

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])  # Add segment to tail
            self.food_position = self.set_new_food_position()

    def update_canvas(self):
        self.canvas.delete("all")

        # Draw snake
        for x, y in self.snake_positions:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="lime", outline="")

        # Draw food
        fx, fy = self.food_position
        self.canvas.create_oval(fx, fy, fx + self.cell_size, fy + self.cell_size, fill="red", outline="")

        # Draw score
        self.canvas.create_text(45, 12, text=f"Score: {self.score}", fill="white", font=('Arial', 14))

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(self.width/2, self.height/2, text=f"Game Over! Score: {self.score}",
                                fill="red", font=('Arial', 24))
        self.canvas.create_text(self.width/2, self.height/2 + 30, text="Press Esc to exit.",
                                fill="white", font=('Arial', 16))
        self.root.bind("<Escape>", lambda e: self.root.destroy())

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
