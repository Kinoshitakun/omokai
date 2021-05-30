
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
        self.node1_weight_list = []
        self.node2_weight_list = []
        self.tree_depth = 3
        self.curr_depth = 0
        self.node1_kouho = []

    def get_kouho(self,w):
        l = w.copy()
        m = np.max(w)
        kouho_list = []
        for i in range(15):
            for j in range(15):
                if w[i,j] == m:
                    kouho_list.append([i,j])
                    l[i,j] = 0
        n = np.max(l)
        if n != 0:
            for i in range(15):
                for j in range(15):
                    if w[i,j] == n:
                        kouho_list.append([i,j])
                        l[i,j] = 0
        return kouho_list
    
    def search(self,board,kouho,turn):
        cx = 0
        cy = 0
        self.curr_depth += 1
        for kh in kouho:
            print(self.curr_depth , 'floor:' , kouho )
            if self.curr_depth == 2:
                self.node1_kouho = kouho.copy()
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
                point = self.w.get_point()
                self.node2_weight_list.append(self.w.weight[point])
                if self.node2_weight_list :
                    if len(self.node2_weight_list) == len(kouho):
                        self.node1_weight_list.append(np.max(self.node2_weight_list)) 
                        # print("third tree" , self.node2_weight_list)
                        self.curr_depth = self.tree_depth - 1
                        self.node2_weight_list = []
                        if len(self.node1_weight_list) == len(self.node1_kouho):
                            self.max_weight_list.append(np.max(self.node1_weight_list)) 
                            self.curr_depth = 1
                            # print("second tree" , self.node1_weight_list)
                            self.node1_weight_list = []
                            self.node1_kouho = []
                continue
            weight = self.w.get_weight()
            next_kouho = self.get_kouho(weight)
            self.search(b,next_kouho,turn)
            
    

    def run(self):
        kouho = self.get_kouho(self.weight)
        self.search(self.s_board,kouho,self.turn)
        print("first tree" , self.max_weight_list)
        # print(self.weight)
        result_index = np.argmax(self.max_weight_list)
        return kouho[result_index]
