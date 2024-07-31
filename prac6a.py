import tkinter as tk
from tkinter import messagebox

class MissionariesCannibals:
    def __init__(self, master):
        self.master = master
        master.title("Missionaries and Cannibals")

        self.missionaries_left = 3
        self.cannibals_left = 3
        self.missionaries_right = 0
        self.cannibals_right = 0
        self.boat_position = "left"
        self.boat_capacity = 2

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.status_label = tk.Label(self.master, text="Missionaries: 3, Cannibals: 3")
        self.status_label.grid(row=0, column=0, columnspan=4)

        self.boat_label = tk.Label(self.master, text="Boat Position: Left")
        self.boat_label.grid(row=1, column=0, columnspan=4)

        self.left_frame = tk.Frame(self.master)
        self.left_frame.grid(row=2, column=0)

        self.right_frame = tk.Frame(self.master)
        self.right_frame.grid(row=2, column=2)

        self.boat_frame = tk.Frame(self.master)
        self.boat_frame.grid(row=2, column=1)

        self.left_canvas = tk.Canvas(self.left_frame, width=300, height=200, bg='lightblue')
        self.left_canvas.pack()

        self.right_canvas = tk.Canvas(self.right_frame, width=300, height=200, bg='lightblue')
        self.right_canvas.pack()

        self.boat_canvas = tk.Canvas(self.boat_frame, width=100, height=50, bg='lightblue')
        self.boat_canvas.pack()

        self.move_button = tk.Button(self.master, text="Move Boat", command=self.move_boat)
        self.move_button.grid(row=3, column=1, columnspan=2)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=4, column=1, columnspan=2)

        self.missionaries_to_move = tk.IntVar(value=0)
        self.cannibals_to_move = tk.IntVar(value=0)

        tk.Label(self.master, text="Missionaries to move:").grid(row=5, column=0)
        tk.Entry(self.master, textvariable=self.missionaries_to_move).grid(row=5, column=1)

        tk.Label(self.master, text="Cannibals to move:").grid(row=5, column=2)
        tk.Entry(self.master, textvariable=self.cannibals_to_move).grid(row=5, column=3)

    def update_display(self):
        self.left_canvas.delete("all")
        self.right_canvas.delete("all")
        self.boat_canvas.delete("all")

        # Draw missionaries and cannibals on the left side
        for i in range(self.missionaries_left):
            self.left_canvas.create_text(50, 30 + 60 * i, text="M", font=('Arial', 20, 'bold'), fill="black")
        for i in range(self.cannibals_left):
            self.left_canvas.create_text(100, 30 + 60 * i, text="C", font=('Arial', 20, 'bold'), fill="black")

        # Draw missionaries and cannibals on the right side
        for i in range(self.missionaries_right):
            self.right_canvas.create_text(50, 30 + 60 * i, text="M", font=('Arial', 20, 'bold'), fill="black")
        for i in range(self.cannibals_right):
            self.right_canvas.create_text(100, 30 + 60 * i, text="C", font=('Arial', 20, 'bold'), fill="black")

        # Draw the boat
        boat_x = 0 if self.boat_position == "left" else 200
        self.boat_canvas.create_rectangle(0, 0, 100, 50, fill='brown', outline='black')
        self.boat_canvas.create_text(50, 25, text="Boat", font=('Arial', 12, 'bold'), fill="white")
        self.boat_canvas.place(x=boat_x, y=150)

        self.boat_label.config(text=f"Boat Position: {self.boat_position.capitalize()}")

    def move_boat(self):
        m_to_move = self.missionaries_to_move.get()
        c_to_move = self.cannibals_to_move.get()

        if m_to_move + c_to_move > self.boat_capacity:
            messagebox.showinfo("Invalid Move", "The boat capacity is exceeded!")
            return

        if self.boat_position == "left":
            if m_to_move > self.missionaries_left or c_to_move > self.cannibals_left:
                messagebox.showinfo("Invalid Move", "Not enough missionaries or cannibals on the left!")
                return
            if not self.is_valid_state(self.missionaries_left - m_to_move, self.cannibals_left - c_to_move) or \
               not self.is_valid_state(self.missionaries_right + m_to_move, self.cannibals_right + c_to_move):
                messagebox.showinfo("Invalid Move", "Invalid move! Missionaries cannot be outnumbered.")
                return
            self.missionaries_left -= m_to_move
            self.cannibals_left -= c_to_move
            self.missionaries_right += m_to_move
            self.cannibals_right += c_to_move
            self.boat_position = "right"
        else:
            if m_to_move > self.missionaries_right or c_to_move > self.cannibals_right:
                messagebox.showinfo("Invalid Move", "Not enough missionaries or cannibals on the right!")
                return
            if not self.is_valid_state(self.missionaries_left + m_to_move, self.cannibals_left + c_to_move) or \
               not self.is_valid_state(self.missionaries_right - m_to_move, self.cannibals_right - c_to_move):
                messagebox.showinfo("Invalid Move", "Invalid move! Missionaries cannot be outnumbered.")
                return
            self.missionaries_left += m_to_move
            self.cannibals_left += c_to_move
            self.missionaries_right -= m_to_move
            self.cannibals_right -= c_to_move
            self.boat_position = "left"

        self.update_display()
        self.check_win_condition()

    def is_valid_state(self, missionaries, cannibals):
        if missionaries < 0 or cannibals < 0 or (missionaries > 0 and missionaries < cannibals):
            return False
        return True

    def check_win_condition(self):
        if self.missionaries_right == 3 and self.cannibals_right == 3:
            messagebox.showinfo("Congratulations!", "You have solved the puzzle!")
            self.master.quit()

def main():
    root = tk.Tk()
    game = MissionariesCannibals(root)
    root.mainloop()

if __name__ == "__main__":
    main()
