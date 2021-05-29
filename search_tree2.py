
import numpy as np
from weight7 import Weight


class Search_tree(object):
    def __init__(self,omok):
        self.s_board = omok.board.copy()
        self.turn = omok.turn
        self.teki_turn  = omok.teki_turn
        self.w = Weight(omok)
        self.weight = self.w.get_weight()
        self.max_weight_list = []
        self.node_weight_list = []
        self.tree_depth = 2
        self.curr_depth = 0

    def get_kouho(self,w):
        kouho_list = []
        result = np.max(w)
        for i in range(15):
            for j in range(15):
                if w[i][j] == result:
                    kouho_list.append([i,j])
        return kouho_list
    
    def search(self,board,kouho,turn):
        cx = 0
        cy = 0
        self.curr_depth += 1
        for kh in kouho:
            
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
            if self.curr_depth == self.tree_depth:
                result = self.w.get_point()
                self.node_weight_list.append([cx,cy])
                if self.node_weight_list:
                    if len(self.node_weight_list) == len(kouho):
                        self.max_weight_list.append(np.max(self.node_weight_list)) 
                        self.curr_depth = 0
                        self.node_weight_list = []
                continue
            weight = self.w.get_weight()
            next_kouho = self.get_kouho(weight)
            self.search(b,next_kouho,turn)
            
    

    def run(self):
        kouho = self.get_kouho(self.weight)
        self.search(self.s_board,kouho,self.turn)
        print(self.max_weight_list)
        print(self.weight)
        result_index = np.argmax(self.max_weight_list)
        return kouho[result_index]
