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
        # self.clock = pygame.time.Clock()
        
    
    def gameloop(self):
        """Main game loop"""
        while True:
            self.game.show_board(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # self.clock.tick(60)
            
            
            pygame.display.update()
    
main = Main()
main.gameloop()