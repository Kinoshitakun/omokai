import numpy as np
import copy
from weight8 import get_weight

class Tree(object):
    def __init__(self,parent,omok):
        self.turn = turn
        self.board = omok.board
        self.win = 0
        self.parent = parent
        self.visits = 0
        self.children = {}

    def expand(self,doko):
        if doko in children.key():
            return False
        else:
            x,y = doko
            board_copy = copy.deepcopy(self.board)
            board_copy[x,y] = self.turn
            self.children[doko] = Tree(self,board_copy,-turn)

            return True
        

    def get_ucb(self,root_win):
        c = np.sqrt(2)
        q = self.win / (root_win + 2e-3)
        e = c*(np.sqrt(np.log(self.parent.visits) / (self.visits + 2e-3)))
        return q + e

    def get_max_ucb_node(self):
        node = None
        max_ucb = 0
        for n in self.children.values():
            if n.get_ucb >= max_ucb:
                max_ucb = n.get_ucb
                node = n
        return node

    def update_lose(self):
        self.visits += 1
        if self.parent:
            self.parent.update_lose()
    
    def update_win(self):
        self.visits += 1
        self.win += 1
        if self.parent:
            self.parent.update_win()
            

    def is_leaf(self):
        return self.children == {}

    def is_root(self):
        return self.parent == None

class MCTS:
    def __init__(self,omok,rule):
        self.omok = copy.deepcopy(omok)
        self.root = Tree(None,omok)
        self.rule = rule
        
    def selection(self):
        return self.root.get_max_ucb_node()

    def expansion(self,node):
        s = np.random.choice(15,2)
        if self.omok.board[s] != 0:
            self.expansion()
        else:
            if not node.expand(s):
                self.expansion()
    def get_zero_list(self,board,turn):
        zero_list = []
        for i in range(15):
            for j in range(15):
                if board[i,j] == 0:
                    if turn != 1:
                        zero_list.append([i,j])
                    else:
                        if self.rule.samsam([i,j]) or self.rule.yukmok([i,j]):
                            continue
                        else:
                            zero_list.append([i,j])
        return zero_list
    
    def playout(self,state):
        omok = copy.deepcopy(self.omok)
        while(1):
            s = np.random.choice(self.get_zero_list(omok.board))
            omok.board[s] = omok.turn
            omok.turn *= -1
            omok.teki_turn *= -1
            if omok.gameover():
                return -omok.turn

    def backpropagation(self,node,turn):
        if turn == 1:
            node.update_win()
        else:
            node.update_lose()


            
        
        
    
    