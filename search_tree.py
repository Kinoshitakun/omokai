from main6 import Omok
from weight6 import Weight
import numpy as np



class Search_tree(object):
    def __init__(self,omok):
        self.s_board = omok.board
        self.turn = omok.turn
        self.teki_turn  = omok.teki_turn
        self.w = Weight(omok)
        self.weight = self.w.get_weight()
        self.max_weight_list = []
        self.tree_depth = 5
        self.curr_depth = 0

    def get_kouho(self,weight):
        kouho_list = []
        max = np.max(weight)
        for i in range(15):
            for j in range(15):
                if weight[i,j] == max:
                    kouho_list.append([i,j])
        return kouho_list
    
    def search(self,board,kouho,turn):
        cx,cy = 0
        for kh in kouho:
            if self.curr_depth == self.tree_depth:
                self.curr_depth = 0
                result = self.w.get_point()
                self.max_weight_list.append([cx,cy])
                continue
            x,y = kh
            b = board
            b[x,y] = turn
            self.w.board = b
            self.w.turn = -turn
            self.w.last_turn = [x,y]
            cx,cy = self.w.get_point()
            b[cx,cy] = -turn
            self.w.board = b
            self.w.turn = turn
            self.w.last_turn = [cx,cy]
            self.curr_depth += 1
            weight = self.w.get_weight
            next_kouho = self.get_kouho(weight)
            search(b,next_kouho,turn)
            


    def 
