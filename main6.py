import pygame,sys
from pygame.locals import*
import numpy as np
from weight4 import*

window_width = 800
window_height = 500
bg_color = (128,128,128)
grid_size = 30
transparent = (0,0,0,0)
fps = 60
fps_clock = pygame.time.Clock()

def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width,window_height))
    surface.fill(bg_color)
    omok = Omok(surface)
    run_game(surface,omok)

def run_game(surface,omok):
    omok.init_board()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.quit()
            elif event.type == MOUSEBUTTONUP:
                if omok.check_board(event.pos):
                    if omok.gameover():
                        print("GAMEOVER!!")
                        omok.show_menu(surface)
                        pygame.display.update()
                        fps_clock.tick(fps)
                        menu_run(surface,omok)
                    
        pygame.display.update()
        fps_clock.tick(fps)

def menu_run(surface,omok):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.quit()
            elif event.type == MOUSEBUTTONUP:
                if(omok.check_menu(event.pos)):
                    run_game(surface,omok)
                
        pygame.display.update()
        fps_clock.tick(fps)
    



class Omok(object):
    def __init__(self,surface):
        self.surface = surface
        self.grid_size = 30
        self.board = np.zeros((15,15))
        self.set_image()
        self.coords = []
        self.menu_coords = [[600,400]]
        self.init_board()
        self.set_coords()
        self.turn = 1
        self.last_turn = []

    def set_image(self):
        self.board_image = pygame.image.load('image/board.PNG')
        white_image = pygame.image.load('image/white.png')
        self.white_image = pygame.transform.scale(white_image,(grid_size,grid_size))
        black_image = pygame.image.load('image/black.png')
        self.black_image = pygame.transform.scale(black_image,(grid_size,grid_size))
        self.font = pygame.font.Font(None,40)
        self.redo_text = self.font.render("New Game",True,(0,0,128))
        self.whitewin_text = self.font.render("White Win!",True,(255,255,255))
        self.blackwin_text = self.font.render("Black Win!",True,(0,0,0))
        self.SamsamError_text = self.font.render("SamSam!",True,(255,255,255))
        self.YukmokError_text = self.font.render("Yukmok!",True,(255,255,255))
        self.Empty_text = pygame.Rect(550,50,80,40)
        
    
    def init_board(self):
        self.turn = 1
        self.board = np.zeros((15,15))
        self.surface.fill(bg_color)
        self.surface.blit(self.board_image,(0,0))
        
    def set_coords(self):
        for x in range(15):
            for y in range(15):
                self.coords.append([x*self.grid_size + 25 , y*self.grid_size + 25])

    def get_coords(self,pos):
        for coord in self.coords:
            x,y = coord
            rect = pygame.Rect(x,y,grid_size,grid_size)
            if rect.collidepoint(pos):
                return coord
        return False

    def get_point(self,pos):
        result = [int((pos[0]-25)/self.grid_size),int((pos[1]-25)/self.grid_size)]
        return result

    def check_board(self,pos):
        pos = self.get_coords(pos)
        if pos:
            x,y = self.get_point(pos)
            if self.board[x][y] == 0:

                rule = Rule(self)
                if rule.samsam([x,y]):
                    self.surface.blit(self.SamsamError_text,(550,50))
                    return False
                if rule.yukmok([x,y]):
                    self.surface.blit(self.YukmokError_text,(550,50))
                    return False
                self.surface.blit(self.black_image,pos)
                self.board[x][y] = 1
                if self.gameover():
                    pygame.draw.rect(self.surface,bg_color,self.Empty_text,100)
                    return True
                self.turn = -1
                self.last_turn = [x,y]  
                weight = Weight(self)
                comx,comy = weight.get_point()
                self.board[comx][comy] = -1
                self.surface.blit(self.white_image,[comx*30+25,comy*30+25])
                weight.print_weight()
                if self.gameover():
                    pygame.draw.rect(self.surface,bg_color,self.Empty_text,100)
                    return True
                self.turn = 1

                
                pygame.draw.rect(self.surface,bg_color,self.Empty_text,100)  
                return True
        return False


    def gameover(self):
        for x in range(15):#가로
            cnt = 1
            for y in range(14):
                if (self.board[x][y] != 0 and self.board[x][y] == self.board[x][y+1]):
                    cnt += 1
                else:
                    cnt = 1
                if cnt == 5:
                    return True
        for y in range(15):#세로
            cnt = 1
            for x in range(14):
                if (self.board[x][y] != 0 and self.board[x][y] == self.board[x+1][y]):
                    cnt += 1
                else:
                    cnt = 1
                if cnt == 5:
                    return True
        for x in range(11):#\대각
            for y in range(11):
                cnt = 1
                for l in range(4):
                    if (self.board[x][y] != 0 and self.board[x][y] == self.board[x+1+l][y+1+l]):
                        cnt += 1
                if cnt == 5:
                    return True
        for x in range(11):#/대각
            for y in range(11):
                cnt = 1
                for l in range(4):
                    if (self.board[x][14-y] != 0 and self.board[x][14-y] == self.board[x+1+l][14-y-1-l]):
                        cnt += 1
                if cnt == 5:
                    return True
        return False

    def show_menu(self,surface):
        if self.turn == -1:
            surface.blit(self.whitewin_text,(550,50))
        else:
            surface.blit(self.blackwin_text,(550,50))
        surface.blit(self.redo_text,(600,400))
    def check_menu(self,pos):
        redo_rect = pygame.Rect(600,400,80,30)
        if redo_rect.collidepoint(pos):
            return True
        return False
            

class Rule(object):
    def __init__(self,omok):
        self.board = omok.board
        self.turn = omok.turn
    
    def samsam(self,pos):
        x,y = pos
        cnt = 0
        test_list_1 = [[1,-1],[1,1],[0,1],[1,0]]
        test_list_2 = [[1,-1],[-1,1],[1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        #이어진3 검출
        for coord in test_list_1:
            a,b = coord
            if x+2*a<14 and x+2*a>=0 and y+2*b<14 and y+2*b >=0 and self.board[x+2*a][y+2*b] == 0:
                if self.board[x+a][y+b] == 1:
                    if x-2*a<14 and x-2*a>=0 and y-2*b<14 and y-2*b >=0:
                        if self.board[x-a][y-b] == 1:
                            if self.board[x-2*a][y-2*b] == 0 and self.board[x+2*a][y+2*b] == 0:
                                if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0:
                                    if  self.board[x+3*a][y+3*b] == 1 or self.board[x-3*a][y-3*b] == 1:
                                        continue    
                                    cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0 and self.board[x+3*a][y+3*b] == 0:
                if self.board[x+2*a][y+2*b] == 1:
                    if self.board[x+a][y+b] == 1:
                        if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                            if self.board[x-a][y-b] == 0:
                                if x+4*a<14 and x+4*a>=0 and y+4*b<14 and y+4*b >=0:
                                    if self.board[x+4*a][y+4*b] == 1:
                                        continue
                                cnt += 1
                            elif self.board[x-a][y-b] == 1:
                                if x-2*a <= 14 and x-2*a >= 0 and y-2*b <= 14 and y-2*b >= 0:
                                    if self.board[x-2*a][y-2*b] == 0:
                                        cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+4*a<14 and x+4*a>=0 and y+4*b<14 and y+4*b >=0 and self.board[x+4*a][y+4*b] == 0:
                if self.board[x+3*a][y+3*b] == 1:
                    if self.board[x+2*a][y+2*b] == 1:
                        if self.board[x+a][y+b] == 0:
                            if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                                if self.board[x-a][y-b] == 0:
                                    cnt += 1
                    elif self.board[x+2*a][y+2*b] == 0:
                        if self.board[x+a][y+b] == 1:
                            if x-a <= 14 and x-a >= 0 and y-b <= 14 and y-b >= 0:
                                if self.board[x-a][y-b] == 0:
                                    cnt += 1
        for coord in test_list_2:
            a,b = coord
            if x+3*a<14 and x+3*a>=0 and y+3*b<14 and y+3*b >=0 and self.board[x+3*a][y+3*b] == 0:
                if self.board[x+2*a][y+2*b] == 1:
                    if self.board[x+a][y+b] == 0:
                        if x-2*a <= 14 and x-2*a >= 0 and y-2*b <= 14 and y-2*b >= 0:
                            if self.board[x-a][y-b] == 1:
                                if self.board[x-2*a][y-2*b] == 0:
                                    cnt += 1
        if cnt >= 2:
            return True
        return False
    
    def yukmok(self,pos):
        x,y = pos
        test_list_1 = [[1,-1],[1,1],[0,1],[1,0]]
        for coord in test_list_1:
            a,b = coord
            cnt = 0
            for l in range(-5,5):
                if l == 0:
                    if x+a<14 and x+a>=0 and y+b<=14 and y+b >=0:
                        if self.board[x+a][y+b] == 1:
                            cnt += 1
                            if cnt >= 5:
                                return True
                        else:
                            cnt = 0
                        continue
                    else:
                        break
                if l == -1:
                    if x-a<14 and x-a>=0 and y-b<=14 and y-b >=0:
                        if self.board[x-a][y-b] == 1:
                            cnt += 1
                            if cnt >= 5:
                                return True
                        else:
                            cnt = 0
                        continue
                    else:
                        break
                    
                if x+l*a<=14 and x+l*a>=0 and y+l*b <=14 and y+l*b >=0:
                    if self.board[x+l*a][y+l*b] == 1:
                        if x+(l+1)*a<=14 and x+(l+1)*a>=0 and y+(l+1)*b <=14 and y+(l+1)*b >=0:
                            if self.board[x+l*a][y+l*b] == self.board[x+(l+1)*a][y+(l+1)*b]:
                                cnt += 1
                            else:
                                cnt = 0
                            if cnt >= 5:
                                return True
                    else:
                        continue
                else:
                    break
        return False
                

if __name__ == "__main__":
    main()
