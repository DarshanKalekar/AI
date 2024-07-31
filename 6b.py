import tkinter as tk
import random

class Puzzle8:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle")

        self.buttons = {}
        self.grid = [[0] * 3 for _ in range(3)]
        self.empty_pos = (2, 2)
        
        self.init_game()
        self.create_widgets()

    def init_game(self):
        numbers = list(range(1, 9)) + [0]
        random.shuffle(numbers)
        self.grid = [numbers[i:i + 3] for i in range(0, 9, 3)]
        self.empty_pos = (2, 2)
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    self.empty_pos = (i, j)

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                number = self.grid[i][j]
                if number != 0:
                    text = str(number)
                else:
                    text = ""
                btn = tk.Button(self.root, text=text, font=('Arial', 24), width=5, height=2,
                                command=lambda i=i, j=j: self.move_tile(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[(i, j)] = btn

    def move_tile(self, x, y):
        empty_x, empty_y = self.empty_pos
        if (abs(x - empty_x) == 1 and y == empty_y) or (abs(y - empty_y) == 1 and x == empty_x):
            self.grid[empty_x][empty_y], self.grid[x][y] = self.grid[x][y], self.grid[empty_x][empty_y]
            self.empty_pos = (x, y)
            self.update_buttons()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                number = self.grid[i][j]
                if number != 0:
                    text = str(number)
                else:
                    text = ""
                self.buttons[(i, j)].config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Puzzle8(root)
    root.mainloop()
