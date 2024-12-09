import pygame
import sys

from CONST import *
from game import Game

class Main:
    
    def __init__(self):
        """Initializing the game window"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chess Game")
        self.game = Game()
        
        
    
    def gameloop(self):
        """Main game loop"""
        game = self.game
        screen = self.screen
        
        while True:
            game.show_board(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # self.clock.tick(60)
            
            
            pygame.display.update()
    
main = Main()
main.gameloop()