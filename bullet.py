from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpointLine import drawLine
from midpointCircle import drawCircle
import math

def drawPoint(x,y,px,color):
    glPointSize(px)
    glBegin(GL_POINTS)
    glColor3f(color[0],color[1],color[2])
    glVertex2f(x,y)
    glEnd()
class Bullet:
    def __init__(self, pos, damage, inc,px):
        self.pos = [pos[0]-px/2, pos[1]]
        self.damage = damage
        self.size = [px, px] 
        self.speed = 10
        self.color = [1,1,1]
        self.inc = inc
    
    
    def draw(self):
        rad = self.size[0]/2
        center = [self.pos[0]+self.size[0]/2, self.pos[1]+self.size[1]/2]
        drawPoint(center[0],center[1],rad,[0.98,0.93,0.95])
        drawCircle(center, 2*rad/4, [1,0.72,0.47],rad/3)
        drawCircle(center, 3*rad/4, [0.95,0.55,0.42],rad/3)
        drawCircle(center, rad, [0.917,0.384,0.384],rad/3)
    
    def move(self): 
        self.pos[0] += self.inc[0]
        self.pos[1] += self.inc[1]
        
def speedCheck(sp, x1, y1, x2, y2):
    if x1 == x2:
        if y1 > y2:
            return 0, sp
        else:
            return 0, -sp
    else:
        m = (y1-y2)/(x1-x2)
        d = math.atan(m)
        c = math.cos(d)
        s = math.sin(d)
        dx = (sp*(c))
        dy = (sp*(s))
    return  dx, dy