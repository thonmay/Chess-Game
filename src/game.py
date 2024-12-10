import pygame
from board import Board
from dragger import Dragger
from CONST import *

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
    def show_board(self, surface):
        """Showing the Chess board"""
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light green
                else:
                    color = (119, 150, 90) # dark green
                
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rect)
                
                pygame.draw.rect(surface, color, rect, 1)
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # Showing all the pieces except for the Dragiing piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
                    
                    
    