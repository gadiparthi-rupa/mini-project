
import tkinter as tk
from tkinter import messagebox
import csv
import datetime

BOARD_SIZE = 5  # You can change the board size

class SOSGame:
    def __init__(self, master):
        self.master = master
        self.master.title("SOS Game")
        self.current_player = "Player 1"
        self.symbol_choice = tk.StringVar(value="S")
        self.board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.buttons = []
        self.player_scores = {"Player 1": 0, "Player 2": 0}
        self.moves = []

        self.setup_ui()

    def setup_ui(self):
        top_frame = tk.Frame(self.master)
        top_frame.pack()

        tk.Label(top_frame, text="Current Player:").grid(row=0, column=0)
        self.turn_label = tk.Label(top_frame, text=self.current_player)
        self.turn_label.grid(row=0, column=1)

        tk.Radiobutton(top_frame, text="S", variable=self.symbol_choice, value="S").grid(row=0, column=2)
        tk.Radiobutton(top_frame, text="O", variable=self.symbol_choice, value="O").grid(row=0, column=3)

        self.score_label = tk.Label(top_frame, text="Scores - Player 1: 0, Player 2: 0")
        self.score_label.grid(row=1, column=0, columnspan=4)

        board_frame = tk.Frame(self.master)
        board_frame.pack()

        for row in range(BOARD_SIZE):
            button_row = []
            for col in range(BOARD_SIZE):
                button = tk.Button(board_frame, text="", width=4, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            symbol = self.symbol_choice.get()
            self.board[row][col] = symbol
            self.buttons[row][col].config(text=symbol, state="disabled")

            move_data = {
                "player": self.current_player,
                "symbol": symbol,
                "row": row,
                "col": col
            }
            self.moves.append(move_data)

            points = self.check_sos(row, col, symbol)
            if points > 0:
                self.player_scores[self.current_player] += points
                self.update_score_label()
                # Same player plays again
            else:
                # Switch player
                self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
                self.turn_label.config(text=self.current_player)

            if self.check_game_over():
                self.end_game()

    def check_sos(self, row, col, symbol):
        count = 0

        def get(r, c):
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                return self.board[r][c]
            return None

        directions = [
            ((-1, 0), (1, 0)),   # Vertical
            ((0, -1), (0, 1)),   # Horizontal
            ((-1, -1), (1, 1)),  # Diagonal \
            ((-1, 1), (1, -1))   # Diagonal /
        ]

        for dir1, dir2 in directions:
            r1, c1 = row + dir1[0], col + dir1[1]
            r2, c2 = row + dir2[0], col + dir2[1]
            if symbol == "O":
                if get(r1, c1) == "S" and get(r2, c2) == "S":
                    count += 1
            elif symbol == "S":
                # Check S-O-S forward
                mid_r, mid_c = row + dir2[0], col + dir2[1]
                end_r, end_c = row + 2 * dir2[0], col + 2 * dir2[1]
                if get(mid_r, mid_c) == "O" and get(end_r, end_c) == "S":
                    count += 1
                # Check S-O-S backward
                mid_r, mid_c = row + dir1[0], col + dir1[1]
                end_r, end_c = row + 2 * dir1[0], col + 2 * dir1[1]
                if get(mid_r, mid_c) == "O" and get(end_r, end_c) == "S":
                    count += 1

        return count

    def update_score_label(self):
        self.score_label.config(text=f"Scores - Player 1: {self.player_scores['Player 1']}, "
                                     f"Player 2: {self.player_scores['Player 2']}")

    def check_game_over(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def end_game(self):
        winner = None
        p1 = self.player_scores["Player 1"]
        p2 = self.player_scores["Player 2"]
        if p1 > p2:
            winner = "Player 1"
        elif p2 > p1:
            winner = "Player 2"
        else:
            winner = "Draw"

        self.save_to_csv(winner)
        messagebox.showinfo("Game Over", f"Game over! Winner: {winner}")
        self.master.destroy()

    def save_to_csv(self, winner):
        filename = "sos_game_log.csv"
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Player", "Symbol", "Row", "Col"])
            for move in self.moves:
                writer.writerow([now, move["player"], move["symbol"], move["row"], move["col"]])
            writer.writerow([f"Final Score: Player 1 = {self.player_scores['Player 1']}, "
                             f"Player 2 = {self.player_scores['Player 2']}, Winner = {winner}"])
            writer.writerow([])  # blank line for separation

# === Run the Game ===
if __name__ == "__main__":
    root = tk.Tk()
    game = SOSGame(root)
    root.mainloop()
