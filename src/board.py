import tkinter as tk
from tkinter import messagebox

class Board():
    def __init__(self):
        super().__init__()

        self.window = tk.Tk()
        self.window.title("TicTacToe")

        self.game = True
        self.current_player = 1
        self.game_counter = 0
        
        self.board = [0] * 9

        self.button_board = [[0,0,0], [0,0,0], [0,0,0]]
        for ro in range(3):
            for col in range(3):
                self.button_board[ro][col] = tk.Button(self.window, fg='black', width=20, height=10, text="", font="arial", command=lambda ro=ro, col=col: self.player_clicked_button(ro, col)) # type: ignore
                self.button_board[ro][col].grid(column=col, row=ro) #type: ignore 
    def __repr__(self):
        return self.board
    

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_player_icon(self):
        if self.current_player == 1:
            return "X"
        elif self.current_player == 2:
            return "O"
    
    def win_check(self):
        for x in range(3):
            if (self.board[x*3] == self.board[x*3 + 1] == self.board[x*3 + 2] == self.get_player_icon() or self.board[x] == self.board[x + 3] == self.board[x + 6] == self.get_player_icon()):
                return True
        if (self.board[0] == self.board[4] == self.board[8] == self.get_player_icon() or self.board[2] == self.board[4] == self.board[6] == self.get_player_icon()):
            return True 
        return False
    
    def reset(self):
        self.board = [0]*9

        for ro in range(3):
            for col in range(3):
                self.button_board[ro][col].config(text="") #type: ignore

        self.game_counter = 0

    def player_clicked_button(self, ro, col):
        if self.board[ro*3 + col] == 0:
            self.game_counter += 1
            self.button_board[ro][col].config(text=self.get_player_icon())
            self.board[ro*3 + col] = self.current_player
        
            if self.win_check() == True:
                messagebox.showinfo("Tic Tac Toe", self.get_player_icon() + " Has won!")  #type: ignore

                self.reset()
            else:        
                if self.game_counter == 9:
                    messagebox.showinfo("Tic Tac Toe", "its a tie")
                    self.reset()
            print(self.board)
            self.switch_player()
    def start(self):
        tk.mainloop()

