from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from midpointLine import drawLine
from jet.jet import *
from blinkblink import *

class Jet:
    def __init__(self, pos, drawArr, colorPalette,health, px = 1):
        self.pos = pos
        self.drawArr = drawArr
        self.colorPalette = colorPalette
        self.px = px
        self.size = [len(drawArr[0])*px, len(drawArr)*px]
        self.inithp = health
        self.health = health
        self.shieldStatus = False
        self.shield = self.health/4
    
    def draw(self, boundary = False):
        x = len(self.drawArr)
        glPointSize(self.px)
        glBegin(GL_POINTS)
        for i in range(len(self.drawArr)):
            for j in range(len(self.drawArr[i])):
                if self.drawArr[i][j] > 0:
                    x_ = ((j+1)*self.px)-1 + self.pos[0]
                    y_ = ((x-i+1)*self.px)-1 + self.pos[1]
                    c = self.colorPalette[self.drawArr[i][j]]
                    glColor3f(c[0],c[1],c[2])
                    glVertex2f(x_,y_)
        glEnd()
        if boundary:
            self.drawBoundaryBox()
    
    def activateShield(self):
        self.shieldStatus = True
        self.shield = int(self.inithp/4 )
    
    def damageShield(self, damage):
        self.shield -= damage
        if self.shield <= 0:
            self.shieldStatus = False
            
    def heal(self, health):
        if self.health + health > self.inithp:
            self.health = self.inithp
        else:
            self.health += health
            
    def drawBoundaryBox(self):
        x1 = self.pos[0]
        y1 = self.pos[1]
        x2 = x1 + self.size[0]
        y2 = y1 + self.size[1]
        drawLine(x1,y1, x2,y1, [1,1,1], 1)
        drawLine(x1,y1, x1,y2, [1,1,1], 1)
        drawLine(x2,y1, x2,y2, [1,1,1], 1)
        drawLine(x1,y2, x2,y2, [1,1,1], 1)
    
    def __str__(self) -> str:
        return f"Jet at {self.pos}\n"

def jetThrust(pos, px = 1):
    DRAWMATRIX.draw(pos, JET_THRUSTER, THRUSTER, px)

if __name__ == '__main__':
    print("Hello World")