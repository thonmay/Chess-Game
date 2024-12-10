import pygame
from piece import Piece
from CONST import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.isDragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = -1
        self.initial_col = -1
    
    def update_blit(self, surface):
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        
        # Image
        img = pygame.image.load(texture)    
        # Rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
    
    def update_mouse(self, pos):    
        self.mouseX, self.mouseY = pos  # x, y cordinates
        
    def save_initial_pos(self, pos):
        self.initial_row = pos[1] // SQUARE_SIZE
        self.initial_col = pos[0] // SQUARE_SIZE
    
    def dragging_piece(self, piece):
        self.piece = piece
        self.isDragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.isDragging = False
        
        