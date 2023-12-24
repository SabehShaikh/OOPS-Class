import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # X starts first

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 40), width=3, height=1, command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def button_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == " ":
            button["text"] = self.current_player
            self.check_winner()
            self.switch_player()

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != " ":
                self.show_winner(self.buttons[i][0]["text"])
                return
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != " ":
                self.show_winner(self.buttons[0][i]["text"])
                return
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            self.show_winner(self.buttons[0][0]["text"])
            return
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            self.show_winner(self.buttons[0][2]["text"])
            return

        # Check for a tie
        if all(button["text"] != " " for row in self.buttons for button in row):
            self.show_winner("Tie")

    def show_winner(self, winner):
        tk.messagebox.showinfo("Winner", f"{winner} wins!")
        self.reset_board()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = " "
        self.current_player = "X"

game = TicTacToe()
game.window.mainloop()