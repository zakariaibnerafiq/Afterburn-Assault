from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpointLine import drawLine

class Bullet:
    def __init__(self, pos, damage):
        self.pos = pos
        self.damage = damage
        self.size = [2,5]
        self.speed = 10
        self.color = [1,1,1]
    
    def draw(self):
        x1 = self.pos[0]
        y1 = self.pos[1]
        x2 = x1 + self.size[0]
        y2 = y1 + self.size[1]
        drawLine(x1,y1, x2,y1, self.color, 1)
        drawLine(x1,y1, x1,y2, self.color, 1)
        drawLine(x2,y1, x2,y2, self.color, 1)
        drawLine(x1,y2, x2,y2, self.color, 1)
        
        