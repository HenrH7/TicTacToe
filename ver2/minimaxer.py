import random

class Minimax():
    depth = 0
    def __init__(self, player):
        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
    def get_avaible_moves(self, board):
        avaible_moves_indexs = []
        for i, val in enumerate(board):
            if val == 0:
                avaible_moves_indexs.append(i)
        return avaible_moves_indexs
