import os

class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1 # 1 for white, -1 for black
        self.moves = []
        self.moved = False
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        
    def set_texture(self, size=80):
        """Setting the Image of the piece"""
        self.texture = os.path.join(
        f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
    
    def add_moves(self, move):
        
        self.moves.append(move)
    
    
"""Chess Pieces"""
class Pawn(Piece):
    def __init__(self, color):
        if color == "white":
            self.dir = -1   # -1 for white, 1 for black
        else:
            self.dir = 1 
        super().__init__("pawn", color, 1.0)

class Rook(Piece):
    def __init__(self, color):
        super().__init__("rook", color, 5.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__("knight", color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("bishop", color, 3.001)

class Queen(Piece):
    def __init__(self, color):
        super().__init__("queen", color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__("king", color, 1000.0)
