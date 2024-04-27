from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from midpointLine import drawLine

class HealthBar:
    def __init__(self, max_health,dimension, pos):
        self.max_health = max_health
        self.health = max_health
        
        self.pos = pos
        self.width = dimension[0]
        self.height = dimension[1]
    
    def draw(self, currentHealth):
        healthpercent = int((currentHealth/self.max_health)*self.width)
        temp = self.width/2
        if healthpercent > temp:
            red  = (healthpercent- temp)/temp
            color = [1- red,1,0]
        
        else:
            green = healthpercent/temp
            color = [1,green,0]
            
        drawLine(self.pos[0], self.pos[1], self.pos[0]+self.width, self.pos[1], color, 1)
        drawLine(self.pos[0], self.pos[1], self.pos[0], self.pos[1]+self.height, color, 1)
        drawLine(self.pos[0]+self.width, self.pos[1], self.pos[0]+self.width, self.pos[1]+self.height, color, 1)
        drawLine(self.pos[0], self.pos[1]+self.height, self.pos[0]+self.width, self.pos[1]+self.height, color, 1)
        
        
        for i in range(healthpercent):
            drawLine(self.pos[0]+i, self.pos[1], self.pos[0]+i, self.pos[1]+self.height, color, 1)
            