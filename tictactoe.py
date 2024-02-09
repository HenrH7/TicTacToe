#!usr/bin/bash python
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title("TicTacToe")

        self.game = True
        self.current_player = "X"
        self.game_counter = 0








        #Create Board and Input list
        self.str_board = [" "]*9
        
        self.Board = [[0,0,0], [0,0,0], [0,0,0]]
        for ro in range(3):
            for col in range(3):
                self.Board[ro][col] = Button(self.window, fg='black', width=20, height=10, text="", font="arial", command=lambda ro=ro, col=col: self.player_clicked_button(ro, col))
                self.Board[ro][col].grid(column=col, row=ro)


        



    def player_clicked_button(self, ro, col):

        if self.str_board[ro*3 + col] == " ":
            self.game_counter += 1
            self.Board[ro][col].config(text=self.current_player)
            self.str_board[ro*3 + col] = self.current_player
        
            

            if self.win_check() == True:
                messagebox.showinfo("Tic Tac Toe", self.current_player + " Has won!")
                self.reset()
            else:        
                if self.game_counter == 9:
                    messagebox.showinfo("Tic Tac Toe", "its a tie")
                    self.reset()
                
                
                
            self.switch_player()
    
    def win_check(self):
        for x in range(3):
            if (self.str_board[x*3] == self.str_board[x*3 + 1] == self.str_board[x*3 + 2] == self.current_player or self.str_board[x] == self.str_board[x + 3] == self.str_board[x + 6] == self.current_player):
                return True
        if (self.str_board[0] == self.str_board[4] == self.str_board[8] == self.current_player or self.str_board[2] == self.str_board[4] == self.str_board[6] == self.current_player):
            return True
  
        

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"



    def reset(self):
        self.str_board = [" "]*9

        for ro in range(3):
            for col in range(3):
                self.Board[ro][col].config(text=" ")

        self.game_counter = 0
    

    def run_game(self):
        self.window.mainloop()
                



Tic_Tac_Toe_game = TicTacToe()
Tic_Tac_Toe_game.run_game()
