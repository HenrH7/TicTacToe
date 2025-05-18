import tkinter as tk
from tkinter import messagebox
from ai import Minimax

class Board():
    def __init__(self):
        self.pvp = messagebox.askyesno("Startup","Are you playing 2 player? Pressing \"no\" will player against the computer")
        self.window = tk.Tk()
        self.window.configure(bg='red')
        self.window.title("TicTacToe")
        self.window.resizable(False, False)

        self.game = True
        self.multiplayer = True
        self.current_player = 1
        self.guess_counter = 0

        self.minimax_scaler = Minimax(self.current_player)
       
        self.board = [0] * 9

        self.button_board = [[0,0,0], [0,0,0], [0,0,0]]
        for ro in range(3):
            for col in range(3):
                self.button_board[ro][col] = tk.Button(self.window, fg='white', bg='black', width=2, height=1, text="", font=("helvetica", 40), command=lambda ro=ro, col=col: self.player_placed(ro, col)) # type: ignore
                self.button_board[ro][col].grid(column=col, row=ro) #type: ignore 
    
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
            if (self.board[x*3] == self.board[x*3 + 1] == self.board[x*3 + 2] == self.current_player or self.board[x] == self.board[x + 3] == self.board[x + 6] == self.current_player):
                return True
        if (self.board[0] == self.board[4] == self.board[8] == self.current_player or self.board[2] == self.board[4] == self.board[6] == self.current_player):
            return True 
        return False
    
    def reset(self):
        self.board = [0]*9

        for ro in range(3):
            for col in range(3):
                self.button_board[ro][col].config(text="") #type: ignore

        self.guess_counter = 0

        print("-"*50)

    def player_placed(self, ro, col):
   
        if self.board[ro*3 + col] == 0:
            self.guess_counter += 1
    
            self.button_board[ro][col].config(text=self.get_player_icon())
            self.board[ro*3 + col] = self.current_player
     
            if self.win_check() == True:
                messagebox.showinfo("Tic Tac Toe", self.get_player_icon() + " Has won!")  #type: ignore
                self.reset()
            elif self.guess_counter == 9:
                messagebox.showinfo("Tic Tac Toe", "Its a tie")
                self.reset()
           
            self.switch_player()
            print(Minimax.depth, "minimax depth")
            if not(self.pvp):
                self.ai_place()
    def ai_place(self):
        aviable_moves = self.minimax_scaler.get_avaible_moves(self.board)
        if len(aviable_moves) > 0:
            self.guess_counter += 1

            move = self.minimax_scaler.find_move(aviable_moves, self.board)
            Minimax.depth = 0

            self.board[move] = self.current_player
            row, col = divmod(move, 3)
            self.button_board[row][col].config(text=self.get_player_icon()) #type: ignore
        
            if self.win_check() == True:
                messagebox.showinfo("Tic Tac Toe", self.get_player_icon() + " Has won!")  #type: ignore
                self.reset()
            elif self.guess_counter == 9:
                messagebox.showinfo("Tic Tac Toe", "Its a tie")
                self.reset()

            self.switch_player()
    def start(self):
        tk.mainloop()

