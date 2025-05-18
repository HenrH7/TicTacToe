import random

class Minimax():
    depth = 0
    def __init__(self, player):
        Minimax.depth += 1

        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
    def get_avaible_moves(self, board):
        avaible_moves_indexs = []
        self.new_board = board.copy()
        for i, val in enumerate(board):
            if val == 0:
                avaible_moves_indexs.append(i)
                self.new_board[i] = "done"
        return avaible_moves_indexs
    def find_move(self, avilible_moves, board):
        # return index of the board that corresponds to the button
        # return random.choice(avilible_moves)
        move = 0
        init_board = board.copy()
        patterns = []
        
        for move in avilible_moves:
            patterns.append(PossiblePattern(init_board, move, self.player, self.opponent))

        self.best_score = 0
        for p in patterns:
            if p.score > self.best_score:
                self.best_score = p.score
                move = p.move
            elif p.score == self.best_score:
                choice = random.randint(0, 2)
                if choice == 0:
                    self.best_score = p.score
                    move = p.move
                   
        if self.best_score == 0 and len(avilible_moves) > 0:
            move = random.choice(avilible_moves)
        return move
    

class PossiblePattern():
    def __init__(self, board, move, player, opponent) -> None:
        self.board = board.copy()
        self.opponent_board = board.copy()
        self.board[move] = player
        self.opponent_board[move] = opponent

        self.score = 0
        self.move = move
        self.player = player
        self.opponent = opponent
 
        #Win for itself
        if self.win_check(self.player, self.board):
            print("win", end=" ")
            if Minimax.depth < 2:
                self.score += 10
            elif Minimax.depth == 2:
                self.score += 8
            elif Minimax.depth == 3:
                self.score += 5
            else:
                self.score += 3
        #Stop Opponent
        if self.win_check(self.opponent, self.opponent_board):
            if Minimax.depth < 2:
                self.score += 6
            elif Minimax.depth == 2:
                self.score += 5
            elif Minimax.depth == 3:
                self.score += 4
            else:
                self.score += 3
        if Minimax.depth < 8:
            self.new_depth()
            print(Minimax.depth)
        
    def visualize(self):
        print(self.board)
    def win_check(self, player_to_check, player_board):
        for x in range(3):
            if (player_board[x*3] == player_board[x*3 + 1] == player_board[x*3 + 2] == player_to_check or player_board[x] == player_board[x + 3] == player_board[x + 6] == player_to_check):
                return True
        if (player_board[0] == player_board[4] == player_board[8] == player_to_check or player_board[2] == player_board[4] == player_board[6] == player_to_check):
            return True 
        return False
    def new_depth(self):
        #get a new move
        next_minimax = Minimax(self.player)
        availible_moves = next_minimax.get_avaible_moves(self.board)
        best_move = next_minimax.find_move(availible_moves, self.board)
        self.score += next_minimax.best_score




