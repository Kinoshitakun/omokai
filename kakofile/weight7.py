
import numpy as np

class Weight(object):
    def __init__(self,omok):
        self.samsamyong_board = omok.board
        self.board = omok.board.copy()
        self.turn = omok.turn
        self.teki_t = -omok.turn
        self.last_turn = omok.last_turn
        self.weight = np.zeros((15,15))
        self.two_point = 2
        self.three_point = 50
        self.closed_four_point = 200
        self.shin_closed_four_point = 250
        self.four_point = 1250
        self.omok_point = 30000
        self.def_point = 0
        self.teki_two_point = 5
        self.teki_three_point = 250
        self.teki_closed_three_point = 30
        self.teki_four_point = 5000
        self.samsam_point = 100



    
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
                            if i+a <15 and i+a>=0 and j+b <15 and j+b>=0:
                                if i-a <15 and i-a>=0 and j-b <15 and j-b>=0:
                                    if self.board[i-a,j-b] == 0:
                                        if self.board[i+a,j+b] == self.turn:
                                            if i+3*a <15 and i+3*a>=0 and j+3*b <15 and j+3*b>=0:
                                                if self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == 0:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == self.turn:
                                                                self.weight[i+2*a,j+2*b] += self.closed_four_point#0001140100
                                                                self.weight[i+3*a,j+3*b] += self.closed_four_point#0001104100
                                                            else:
                                                                self.weight[i+2*a,j+2*b] += self.three_point#003113000
                                                                if self.samsam([i+2*a,j+2*b],self.turn):
                                                                    self.weight[i+2*a,j+2*b] += self.samsam_point
                                                        else:
                                                            self.weight[i+2*a,j+2*b] += self.three_point#003113000
                                                            if self.samsam([i+2*a,j+2*b],self.turn):
                                                                self.weight[i+2*a,j+2*b] += self.samsam_point
                                                    elif self.board[i+3*a,j+3*b] == self.turn:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+2*a,j+2*b] += self.four_point#000011410
                                                            elif self.board[i+4*a,j+4*b] == self.turn:
                                                                self.weight[i+2*a,j+2*b] += self.omok_point#000011511
                                                        else:
                                                            self.weight[i+2*a,j+2*b] += self.shin_closed_four_point#000001141
                                                elif self.board[i+2*a,j+2*b] == self.turn:
                                                    if self.board[i+3*a,j+3*b] == 0:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+3*a,j+3*b] += self.four_point#000011140
                                                            elif self.board[i+4*a,j+4*b] == self.turn:
                                                                self.weight[i+3*a,j+3*b] += self.omok_point#000011151
                                                        else:
                                                            self.weight[i+3*a,j+3*b] += self.shin_closed_four_point#000001114
                                                    elif self.board[i+3*a,j+3*b] == self.turn:
                                                        if self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+4*a,j+4*b] += self.omok_point#000511115
                                        elif self.board[i+a,j+b] == 0:
                                            if i+2*a <15 and i+2*a>=0 and j+2*b <15 and j+2*b>=0:
                                                if self.board[i+2*a,j+2*b] == self.turn:
                                                    if i+3*a <15 and i+3*a>=0 and j+3*b <15 and j+3*b>=0:
                                                        if self.board[i+3*a,j+3*b] == 0:
                                                            self.weight[i+a,j+b] += self.three_point#000131000
                                                            if self.samsam([i+a,j+b],self.turn):
                                                                self.weight[i+a,j+b] += self.samsam_point
                                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                                if self.board[i+4*a,j+4*b] == 0:
                                                                    self.weight[i+3*a,j+3*b] += self.three_point#003101300
                                                                    if self.samsam([i+3*a,j+3*b],self.turn):
                                                                        self.weight[i+3*a,j+3*b] += self.samsam_point
                                                                elif self.board[i+4*a,j+4*b] == self.turn:
                                                                    self.weight[i+3*a,j+3*b] += self.closed_four_point#000101410
                                                        elif self.board[i+3*a,j+3*b] == self.turn:
                                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                                if self.board[i+4*a,j+4*b] == self.turn:
                                                                    self.weight[i+a,j+b] += self.omok_point#000151110
                                                                elif self.board[i+4*a,j+4*b] == 0:
                                                                    self.weight[i+a,j+b] += self.four_point#000141100
                                                                elif self.board[i+4*a,j+4*b] == self.teki_t:
                                                                    self.weight[i+a,j+b] += self.shin_closed_four_point#0001411-10
                                                            else:
                                                                self.weight[i+a,j+b] += self.shin_closed_four_point#000001411
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    self.weight[i+a,j+b] += self.two_point#002120000
                                                    if i+3*a <15 and i+3*a>=0 and j+3*b <15 and j+3*b>=0:
                                                        if self.board[i+3*a,j+3*b] == self.turn:
                                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                                if self.board[i+4*a,j+4*b] == 0:
                                                                    self.weight[i+a,j+b] += self.three_point#000130100
                                                                    if self.samsam([i+a,j+b],self.turn):
                                                                        self.weight[i+a,j+b] += self.samsam_point
                                                                    self.weight[i+2*a,j+2*b] += self.three_point#000103100
                                                                    if self.samsam([i+2*a,j+2*b],self.turn):
                                                                        self.weight[i+2*a,j+2*b] += self.samsam_point
                                                                elif self.board[i+4*a,j+4*b] == self.turn:
                                                                    self.weight[i+a,j+b] += self.closed_four_point#000140110
                                                                    self.weight[i+2*a,j+2*b] += self.closed_four_point#000104110
                                                        elif self.board[i+3*a,j+3*b] == 0:
                                                            self.weight[i+2*a,j+2*b] += self.two_point#020102000
                                    elif self.board[i-a,j-b] == self.teki_t:
                                        if self.board[i+a,j+b] == self.turn:
                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                if self.board[i+2*a,j+2*b] == self.turn:
                                                    if self.board[i+3*a,j+3*b] == self.turn:
                                                        if self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+4*a,j+4*b] += self.omok_point#000-111115
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+3*a,j+3*b] += self.shin_closed_four_point#000-1111400
                                                            self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1111040
                                                        elif self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+3*a,j+3*b] += self.omok_point#000-1111510
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == self.turn:
                                                        if self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+2*a,j+2*b] += self.omok_point#000-1115110
                                                        elif self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+2*a,j+2*b] += self.shin_closed_four_point#000-1114100
                                                            self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1110140
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+2*a,j+2*b] += self.closed_four_point#000-1114010
                                                            self.weight[i+3*a,j+3*b] += self.closed_four_point#000-1110410
                                        elif self.board[i+a,j+b] == 0:
                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                if self.board[i+2*a,j+2*b] == self.turn:
                                                    if self.board[i+3*a,j+3*b] == self.turn:
                                                        if self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+a,j+b] += self.omok_point#000-1151110
                                                        elif self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+a,j+b] += self.shin_closed_four_point#000-1141100
                                                            self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1101140
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+a,j+b] += self.closed_four_point#000-1141010
                                                            self.weight[i+3*a,j+3*b] += self.closed_four_point#000-1101410
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == self.turn:
                                                        if self.board[i+4*a,j+4*b] == self.turn:
                                                            self.weight[i+a,j+b] += self.closed_four_point#000-1140110
                                                            self.weight[i+2*a,j+2*b] += self.closed_four_point#000-1104110
                                else:# i-a or j-b is out of range
                                    if self.board[i+a,j+b] == self.turn:
                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                            if self.board[i+2*a,j+2*b] == self.turn:
                                                if self.board[i+3*a,j+3*b] == self.turn:
                                                    if self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+4*a,j+4*b] += self.omok_point#000-111115
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+3*a,j+3*b] += self.shin_closed_four_point#000-1111400
                                                        self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1111040
                                                    elif self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+3*a,j+3*b] += self.omok_point#000-1111510
                                            elif self.board[i+2*a,j+2*b] == 0:
                                                if self.board[i+3*a,j+3*b] == self.turn:
                                                    if self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+2*a,j+2*b] += self.omok_point#000-1115110
                                                    elif self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+2*a,j+2*b] += self.shin_closed_four_point#000-1114100
                                                        self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1110140
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+2*a,j+2*b] += self.closed_four_point#000-1114010
                                                        self.weight[i+3*a,j+3*b] += self.closed_four_point#000-1110410
                                    elif self.board[i+a,j+b] == 0:
                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                            if self.board[i+2*a,j+2*b] == self.turn:
                                                if self.board[i+3*a,j+3*b] == self.turn:
                                                    if self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+a,j+b] += self.omok_point#000-1151110
                                                    elif self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+a,j+b] += self.shin_closed_four_point#000-1141100
                                                        self.weight[i+4*a,j+4*b] += self.closed_four_point#000-1101140
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+a,j+b] += self.closed_four_point#000-1141010
                                                        self.weight[i+3*a,j+3*b] += self.closed_four_point#000-1101410
                                            elif self.board[i+2*a,j+2*b] == 0:
                                                if self.board[i+3*a,j+3*b] == self.turn:
                                                    if self.board[i+4*a,j+4*b] == self.turn:
                                                        self.weight[i+a,j+b] += self.closed_four_point#000-1140110
                                                        self.weight[i+2*a,j+2*b] += self.closed_four_point#000-1104110
                    except IndexError:
                        pass
                


    def defense(self):
        search_list = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        for i in range(15):
            for j in range(15):
                if self.board[i,j] == -self.turn:
                    try:
                        for l in search_list:
                            a,b = l
                            if i+a <15 and i+a>=0 and j+b <15 and j+b>=0:
                                if i-a <15 and i-a>=0 and j-b <15 and j-b>=0:
                                    if self.board[i-a,j-b] == 0:
                                        if self.board[i+a,j+b] == -self.turn:
                                            if i+3*a <15 and i+3*a>=0 and j+3*b <15 and j+3*b>=0:
                                                if self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == 0:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == -self.turn:
                                                                self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#0001140100
                                                                self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#0001104100
                                                            else:
                                                                self.weight[i+2*a,j+2*b] += self.teki_two_point+self.def_point#003113000
                                                        else:
                                                            self.weight[i+2*a,j+2*b] += self.teki_two_point+self.def_point#003113000
                                                    elif self.board[i+3*a,j+3*b] == -self.turn:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+2*a,j+2*b] += self.teki_three_point+self.def_point#000011410
                                                            elif self.board[i+4*a,j+4*b] == -self.turn:
                                                                self.weight[i+2*a,j+2*b] += self.teki_four_point+self.def_point#000011511
                                                        else:
                                                            self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000001141
                                                elif self.board[i+2*a,j+2*b] == -self.turn:
                                                    if self.board[i+3*a,j+3*b] == 0:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:#errrrrror
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+3*a,j+3*b] += self.teki_three_point+self.def_point#000011140
                                                            elif self.board[i+4*a,j+4*b] == -self.turn:
                                                                self.weight[i+3*a,j+3*b] += self.teki_four_point+self.def_point#000011151
                                                        else:
                                                            self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000001114
                                                    elif self.board[i+3*a,j+3*b] == -self.turn:
                                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+4*a,j+4*b] += self.teki_four_point+self.def_point#000511115
                                                            
                                        elif self.board[i+a,j+b] == 0:
                                            if i+2*a <15 and i+2*a>=0 and j+2*b <15 and j+2*b>=0:
                                                if self.board[i+2*a,j+2*b] == -self.turn:
                                                    if i+3*a <15 and i+3*a>=0 and j+3*b <15 and j+3*b>=0:
                                                        if self.board[i+3*a,j+3*b] == 0:
                                                            self.weight[i+a,j+b] += self.teki_two_point+self.def_point#000131000
                                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                                if self.board[i+4*a,j+4*b] == 0:
                                                                    self.weight[i+3*a,j+3*b] += self.teki_two_point+self.def_point#003101300
                                                                elif self.board[i+4*a,j+4*b] == -self.turn:
                                                                    self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000101410
                                                        elif self.board[i+3*a,j+3*b] == -self.turn:
                                                            if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                                if self.board[i+4*a,j+4*b] == -self.turn:
                                                                    self.weight[i+a,j+b] += self.teki_four_point+self.def_point#000151110
                                                                elif self.board[i+4*a,j+4*b] == 0:
                                                                    self.weight[i+a,j+b] += self.teki_three_point+self.def_point#000141100
                                                                elif self.board[i+4*a,j+4*b] == self.teki_t:
                                                                    self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#0001411-10
                                                            else:
                                                                self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000001411
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    self.weight[i+a,j+b] += self.two_point#002120000
                                                    if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                                        if self.board[i+3*a,j+3*b] == -self.turn:
                                                            if self.board[i+4*a,j+4*b] == 0:
                                                                self.weight[i+a,j+b] += self.teki_two_point+self.def_point#000130100
                                                                self.weight[i+2*a,j+2*b] += self.teki_two_point+self.def_point#000103100
                                                            elif self.board[i+4*a,j+4*b] == -self.turn:
                                                                self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000140110
                                                                self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000104110
                                

                                    elif self.board[i-a,j-b] == -self.teki_t:
                                        if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                            if self.board[i+a,j+b] == -self.turn:
                                                if self.board[i+2*a,j+2*b] == -self.turn:
                                                    if self.board[i+3*a,j+3*b] == -self.turn:
                                                        if self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+4*a,j+4*b] += self.teki_four_point+self.def_point#000-111115
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1111400
                                                            self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1111040
                                                        elif self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+3*a,j+3*b] += self.teki_four_point+self.def_point#000-1111510
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == -self.turn:
                                                        if self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+2*a,j+2*b] += self.teki_four_point+self.def_point#000-1115110
                                                        elif self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1114100
                                                            self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1110140
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1114010
                                                            self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1110410
                                            elif self.board[i+a,j+b] == 0:
                                                if self.board[i+2*a,j+2*b] == -self.turn:
                                                    if self.board[i+3*a,j+3*b] == -self.turn:
                                                        if self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+a,j+b] += self.teki_four_point+self.def_point#000-1151110
                                                        elif self.board[i+4*a,j+4*b] == 0:
                                                            self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1141100
                                                            self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1101140
                                                    elif self.board[i+3*a,j+3*b] == 0:
                                                        if self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1141010
                                                            self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1101410
                                                elif self.board[i+2*a,j+2*b] == 0:
                                                    if self.board[i+3*a,j+3*b] == -self.turn:
                                                        if self.board[i+4*a,j+4*b] == -self.turn:
                                                            self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1140110
                                                            self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1104110
                                else:# i-a or j-b is out of range
                                    if i+4*a <15 and i+4*a>=0 and j+4*b <15 and j+4*b>=0:
                                        if self.board[i+a,j+b] == -self.turn:
                                            if self.board[i+2*a,j+2*b] == -self.turn:
                                                if self.board[i+3*a,j+3*b] == -self.turn:
                                                    if self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+4*a,j+4*b] += self.teki_four_point+self.def_point#000-111115
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1111400
                                                        self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1111040
                                                    elif self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+3*a,j+3*b] += self.teki_four_point+self.def_point#000-1111510
                                            elif self.board[i+2*a,j+2*b] == 0:
                                                if self.board[i+3*a,j+3*b] == -self.turn:
                                                    if self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+2*a,j+2*b] += self.teki_four_point+self.def_point#000-1115110
                                                    elif self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1114100
                                                        self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1110140
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1114010
                                                        self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1110410
                                        elif self.board[i+a,j+b] == 0:
                                            if self.board[i+2*a,j+2*b] == -self.turn:
                                                if self.board[i+3*a,j+3*b] == -self.turn:
                                                    if self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+a,j+b] += self.teki_four_point+self.def_point#000-1151110
                                                    elif self.board[i+4*a,j+4*b] == 0:
                                                        self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1141100
                                                        self.weight[i+4*a,j+4*b] += self.teki_closed_three_point+self.def_point#000-1101140
                                                elif self.board[i+3*a,j+3*b] == 0:
                                                    if self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1141010
                                                        self.weight[i+3*a,j+3*b] += self.teki_closed_three_point+self.def_point#000-1101410
                                            elif self.board[i+2*a,j+2*b] == 0:
                                                if self.board[i+3*a,j+3*b] == -self.turn:
                                                    if self.board[i+4*a,j+4*b] == -self.turn:
                                                        self.weight[i+a,j+b] += self.teki_closed_three_point+self.def_point#000-1140110
                                                        self.weight[i+2*a,j+2*b] += self.teki_closed_three_point+self.def_point#000-1104110


                    except IndexError:
                        pass          

    def samsam(self,pos,turn):
        x,y = pos
        cnt = 0
        test_list_1 = [[1,-1],[1,1],[0,1],[1,0]]
        test_list_2 = [[1,-1],[-1,1],[1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        #이어진3 검출
        for coord in test_list_1:
            a,b = coord
            if x+2*a<14 and x+2*a>=0 and y+2*b<14 and y+2*b >=0 and self.samsamyong_board[x+2*a][y+2*b] == 0:
                if self.samsamyong_board[x+a][y+b] == turn:
                    if x-2*a<14 and x-2*a>=0 and y-2*b<14 and y-2*b >=0:
                        if self.samsamyong_board[x-a][y-b] == turn:
                            if self.samsamyong_board[x-2*a][y-2*b] == 0 and self.samsamyong_board[x+2*a][y+2*b] == 0:
                                if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0:
                                    if  self.samsamyong_board[x+3*a][y+3*b] == turn:
                                        continue    
                                if x-3*a<14 and x-3*a>=0 and y-3*b<14 and y-3*b >=0:
                                    if  self.samsamyong_board[x-3*a][y-3*b] == turn:
                                        continue
                                cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0 and self.samsamyong_board[x+3*a][y+3*b] == 0:
                if self.samsamyong_board[x+2*a][y+2*b] == turn:
                    if self.samsamyong_board[x+a][y+b] == turn:
                        if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                            if self.samsamyong_board[x-a][y-b] == 0:
                                if x+4*a<14 and x+4*a>=0 and y+4*b<14 and y+4*b >=0:
                                    if self.samsamyong_board[x+4*a][y+4*b] == turn:
                                        continue
                                if x-2*a<14 and x-2*a>=0 and y-2*b<14 and y-2*b >=0:
                                    if self.samsamyong_board[x-2*a][y-2*b] == turn:
                                        continue
                                cnt += 1
                            # elif self.samsamyong_board[x-a][y-b] == 1:
                            #     if x-2*a <= 14 and x-2*a >= 0 and y-2*b <= 14 and y-2*b >= 0:
                            #         if self.samsamyong_board[x-2*a][y-2*b] == 0:
                            #             cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+4*a<14 and x+4*a>=0 and y+4*b<14 and y+4*b >=0 and self.samsamyong_board[x+4*a][y+4*b] == 0:
                if self.samsamyong_board[x+3*a][y+3*b] == turn:
                    if self.samsamyong_board[x+2*a][y+2*b] == turn:
                        if self.samsamyong_board[x+a][y+b] == 0:
                            if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                                if self.samsamyong_board[x-a][y-b] == 0:
                                    cnt += 1
                    elif self.samsamyong_board[x+2*a][y+2*b] == 0:
                        if self.samsamyong_board[x+a][y+b] == turn:
                            if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                                if self.samsamyong_board[x-a][y-b] == 0:
                                    cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0 and self.samsamyong_board[x+3*a][y+3*b] == 0:
                if self.samsamyong_board[x+2*a][y+2*b] == turn:
                    if self.samsamyong_board[x+a][y+b] == 0:
                        if x-2*a <= 14 and x-2*a >= 0 and y-2*b <= 14 and y-2*b >= 0:
                            if self.samsamyong_board[x-a][y-b] == turn:
                                if self.samsamyong_board[x-2*a][y-2*b] == 0:
                                    cnt += 1
        if cnt >= 2:
            return True
        return False      
    def get_weight(self):
        self.weight = np.zeros((15,15))
        self.mawari()
        self.attack()
        self.defense()
        
        return self.weight

    def print_weight(self):
        print(self.weight.T)
    
    def get_point(self):
        self.weight = np.zeros((15,15))
        self.mawari()
        self.attack()
        self.defense()
        doko = []
        # print(np.argmax(self.weight))
        x = np.argmax(self.weight)
        i = np.argmax(self.weight)//15
        j = np.argmax(self.weight)%15
        doko = [i,j]
        # print([i,j])

        return doko
        