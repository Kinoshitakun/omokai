from main5 import Omok
import numpy as np

class Weight(object):
    def __init__(self,omok):
        self.board = omok.board
        self.turn = omok.turn
        self.teki_t = -omok.turn
        self.last_turn = omok.last_turn
        self.weight = np.zeros((15,15))
        self.two_point = 2
        self.three_point = 3
        self.closed_four_point = 4
        self.four_point = 16
        self.omok_point = 100
        self.mawari()
        self.attack()



    
    def mawari(self):
        x = self.last_turn[0]
        y = self.last_turn[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                try:
                    if self.board[x+i,y+j] == 0:
                        self.weight[x+i,y+j] += 1
                except IndexError:
                    pass
    def attack(self):
        search_list = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        for i in range(15):
            for j in range(15):
                if self.board[i,j] == self.turn:
                    try:
                        for l in search_list:
                            a,b = l
                            if self.board[i-a,j-b] == 0:
                                if self.board[i+2*a,j+2*b] == self.turn:
                                    if self.board[i+3*a,j+3*b] == 0:
                                        if self.board[i+4*a,j+4*b] == 0:
                                            self.weight[i+3*a,j+3*b] += self.two_point#002112000
                                        elif self.board[i+4*a,j+4*b] == self.turn:
                                            if i+5*a <15 and i+5*a>=0 and j+5*b <15 and j+5*b>=0:
                                                if self.board[i+5*a,j+5*b] == 0:
                                                    if i+6*a <15 and i+6*a>=0 and j+6*b <15 and j+6*b>=0:
                                                        if self.board[i+6*a,j+6*b] == self.turn:
                                                            self.weight[i+3*a,j+3*b] += self.omok_point#000011511
                                                    else:
                                                        self.weight[i+3*a,j+3*b] += self.four_point#000011410
                                            else:
                                                self.weight[i+3*a,j+3*b] += self.closed_four_point#000001141
                                    elif self.board[i+3*a,j+3*b] == self.turn:
                                        if self.board[i+4*a,j+4*b] == 0:
                                            if i+5*a <15 and i+5*a>=0 and j+5*b <15 and j+5*b>=0:
                                                if self.board[i+5*a,j+5*b] == 0:
                                                    self.weight[i+4*a,j+4*b] += self.four_point#000011140
                                                elif self.board[i+5*a,j+5*b] == self.turn:
                                                    self.weight[i+4*a,j+4*b] += self.omok_point#000011151
                                            else:
                                                self.weight[i+4*a,j+4*b] += self.closed_four_point#000001114
                                        elif self.board[i+4*a,j+4*b] == self.turn:
                                            if self.board[i+5*a,j+5*b] == 0:
                                                self.weight[i+5*a,j+5*b] += self.omok_point#000511115
                                elif self.board[i+2*a,j+2*b] == 0:
                                    if self.board[i+3*a,j+3*b] == self.turn:
                                        if self.board[i+4*a,j+4*b] == 0:
                                            self.weight[i+2*a,j+2*b] += self.three_point#000131000
                                            if self.board[i+5*a,j+5*b] == 0:
                                                self.weight[i+4*a,j+4*b] += self.three_point#003101300
                                            elif self.board[i+5*a,j+5*b] == self.turn:
                                                self.weight[i+4*a,j+4*b] += self.closed_four_point#000101410
                                        elif self.board[i+4*a,j+4*b] == self.turn:
                                            if i+5*a <15 and i+5*a>=0 and j+5*b <15 and j+5*b>=0:
                                                if self.board[i+5*a,j+5*b] == self.turn:
                                                    self.weight[i+2*a,j+2*b] += self.omok_point#000151110
                                                elif self.board[i+5*a,j+5*b] == 0:
                                                    self.weight[i+2*a,j+2*b] += self.four_point#000141100
                                                elif self.board[i+5*a,j+5*b] == self.teki_t:
                                                    self.weight[i+2*a,j+2*b] += self.closed_four_point#0001411-10
                                            else:
                                                self.weight[i+2*a,j+2*b] += self.closed_four_point#000001411
                                    elif self.board[i+3*a,j+3*b] == 0:
                                        if self.board[i+4*a,j+4*b] == 0:
                                            self.weight[i+3*a,j+3*b] += self.two_point#020102000
                                        elif self.board[i+4*a,j+4*b] == self.turn:
                                            if self.board[i+5*a,j+5*b] == 0:
                                                self.weight[i+2*a,j+2*b] += self.three_point#000130100
                                                self.weight[i+3*a,j+3*b] += self.three_point#000103100
                                            elif self.board[i+5*a,j+5*b] == self.turn:
                                                self.weight[i+2*a,j+2*b] += self.closed_four_point#000140110
                                                self.weight[i+3*a,j+3*b] += self.closed_four_point#000104110
                    except IndexError:
                        pass
    def get_weight(self):
        return self.weight
    def print_weight(self):
        print(self.weight)
    
    def get_point(self):
        self.mawari()
        self.attack()
        doko = []
        print(np.argmax(self.weight))
        x = np.argmax(self.weight)
        i = np.argmax(self.weight)//15 + 1
        j = np.argmax(self.weight)%15
        doko = [i,j]

        return doko
        