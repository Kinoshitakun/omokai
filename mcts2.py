import numpy as np
import copy
# from weight8 import Weight.get_weight

class Tree(object):
    def __init__(self,parent,board,turn):
        self.turn = turn
        self.board = board
        self.win = 0
        self.parent = parent
        self.visits = 0
        self.children = {}

    def expand(self,doko):
        x,y = doko
        kore = (x,y)
        if self.children != {}:
            if kore in self.children.keys():
                return False
        
        board_copy = copy.copy(self.board)
        board_copy[x][y] = self.turn
        self.children[kore] = Tree(self,board_copy,-self.turn)

        return self.children[kore]
        

    def get_ucb(self,root_win):
        c = np.sqrt(2)
        q = self.win / (root_win + 2e-3)
        # e = c*(np.sqrt(np.log(self.parent.visits+2e-3) / (self.visits + 2e-3)))
        e = c*(np.log(self.parent.visits+2e-3) / (self.visits + 2e-3))
        return q + e

    def get_max_ucb_node(self,root_win,owari = 0):
        node = None
        max_ucb = 0
        x,y = [0,0]
        print('bbb')
        if self.children =={}:
            print('aaa')
            return self
        if owari == 1:
            max_winrate = 0
            for n in self.children.items():
                if n[1].visits != 0:
                    if n[1].win/n[1].visits >= max_winrate:
                        max_winrate = n[1].win/n[1].visits
                        x,y = n[0]
            print([x,y])
            return [x,y]
        for n in self.children.items():
            if n[1].get_ucb(root_win) >= max_ucb:
                max_ucb = n[1].get_ucb(root_win)
                node = n[1]
                x,y = n[0]
                print(x,y)
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

class MCTS(object):
    def __init__(self,omok,rule):
        self.board = copy.copy(omok.board)
        self.turn = omok.turn
        self.root = Tree(None,omok.board,omok.turn)
        self.rule = rule
        self.playcnt = 1000
        
    def selection(self,node):
        if node.children == {}:
            print("uun")
            return node
        else:
            return node.get_max_ucb_node(self.root.win)

    def expansion(self,node):
        s = np.random.choice(15,2)
        if node.board[s[0]][s[1]] != 0:
            self.expansion(node)
        else:
            if not node.expand(s):
                print(self.root.children.keys())
                self.expansion(node)
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
        board = copy.copy(self.board)
        turn = self.turn
        while(1):
            s = np.random.choice(self.get_zero_list(board))
            board[s] = turn
            turn *= -1
            if gameover(board):
                return -turn


    def result_playout(self,state,playcnt):
        result = 0
        for i in range(playcnt):
            result += playout(state)
        if result > 0:
            return 1
        else:
            return -1



    def backpropagation(self,node,turn):
        if turn == -1:
            node.update_win()
        else:
            node.update_lose()


    def run(self):

        for i in range(10):
            print(i)
            node_1 = self.selection(self.root)
            if node_1.is_leaf() == False:
                node_2 = self.selection(node_1)
                if node_2.is_leaf() == False:
                    node_3 = self.selection(node_2)
                    ex_node = self.expansion(node_3)
                    if ex_node:
                        result = result_playout(ex_node.board,self.playcnt)
                        self.backpropagation(ex_node,result)
                    else:
                        continue
                else:
                    ex_node = self.expansion(node_2)
                    if ex_node:
                        result = result_playout(ex_node.board,self.playcnt)
                        self.backpropagation(ex_node,result)
                    else:
                        continue

            else:
                ex_node = self.expansion(node_1)
                if ex_node:
                    result = result_playout(ex_node.board,self.playcnt)
                    self.backpropagation(ex_node,result)
                else:
                    continue
        return self.root.get_max_ucb_node(self.root.win,owari = 1)
        
def gameover(board):
        for x in range(15):#가로
            cnt = 1
            for y in range(14):
                if (board[x][y] != 0 and board[x][y] == board[x][y+1]):
                    cnt += 1
                else:
                    cnt = 1
                if cnt == 5:
                    return True
        for y in range(15):#세로
            cnt = 1
            for x in range(14):
                if (board[x][y] != 0 and board[x][y] == board[x+1][y]):
                    cnt += 1
                else:
                    cnt = 1
                if cnt == 5:
                    return True
        for x in range(11):#\대각
            for y in range(11):
                cnt = 1
                for l in range(4):
                    if (board[x][y] != 0 and board[x][y] == board[x+1+l][y+1+l]):
                        cnt += 1
                if cnt == 5:
                    return True
        for x in range(11):#/대각
            for y in range(11):
                cnt = 1
                for l in range(4):
                    if (board[x][14-y] != 0 and board[x][14-y] == board[x+1+l][14-y-1-l]):
                        cnt += 1
                if cnt == 5:
                    return True
        return False
            


            
        
        
    
    