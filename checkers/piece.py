import pygame.draw
import pygame
from .constants import RED, WHITE, Border, GRAY, CROWN


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.king = False
        #color and the x to get the size 
        self.color = color
        
        self.x = 0
        self.y = 0
        self.calc()



    def put_crown_on_board(self):
        self.king = True


    def calculate_coordinate(self):
        self.x = Border * self.col + Border // 2
        self.y = Border * self.row + Border // 2



#using the pygame to make the outline 
    def draw(self, win):
        radius = Border // 2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x-CROWN.get_width()//2,self.y-CROWN.get_height()//2))

    def __repr__(self):
        return str(self.color)
    def move(self, row,col):
        self.row = row
        self.col = col
        self.calculate_coordinate()