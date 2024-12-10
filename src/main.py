import pygame
import sys

from CONST import *
from game import Game
from board import Board
from dragger import Dragger


class Main:
    
    def __init__(self):
        """Initializing the game window"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chess Game")
        self.game = Game()
        self.board = Board()
        
        
    
    def gameloop(self):
        """Main game loop"""
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        
        while True:
            
            game.show_board(screen)
            game.show_pieces(screen)
            
            if dragger.isDragging:          # if the piece is being dragged
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                    # Moving Pieces
                if event.type == pygame.MOUSEBUTTONDOWN:     # click
                    dragger.update_mouse(event.pos)
                       
                    clicked_row = dragger.mouseY // SQUARE_SIZE  # Clicked Sqaures
                    clicked_col = dragger.mouseX // SQUARE_SIZE
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial_pos(event.pos)
                        dragger.dragging_piece(piece)
                        print(piece)
                       
                elif event.type == pygame.MOUSEMOTION:   # mouse motion
                    if dragger.isDragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)
                
                elif event.type == pygame.MOUSEBUTTONUP:      # click release
                    dragger.undrag_piece()
                    
                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # self.clock.tick(60)
            
            
            pygame.display.update()
    
main = Main()
main.gameloop()