import pygame

from CONST import *

class Game:
    def __init__(self):
        pass
    
    def show_board(self, surface):
        """Showing the chess board"""
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light green
                else:
                    color = (119, 150, 90) # dark green
                
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rect)
                
                pygame.draw.rect(surface, color, rect, 1)
    
    
    