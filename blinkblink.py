from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

STARBIG = [[0,0,0,0,1,0,0,0,0],
           [0,0,0,0,2,0,0,0,0],
           [0,0,0,0,3,0,0,0,0],
           [0,0,0,4,3,4,0,0,0],
           [1,2,3,3,4,3,3,2,1],
           [0,0,0,4,3,4,0,0,0],
           [0,0,0,0,3,0,0,0,0],
           [0,0,0,0,2,0,0,0,0],
           [0,0,0,0,1,0,0,0,0]]

STARCOLOR= {
    1: [0.0039, 0.28, 0.509],
    2: [0, 0.34, 0.68],
    3: [0.16, 0.58, 0.98],
    4: [0.36,0.72,0.96],
}
STARCOLOR2= {
    1: [0.49, 0.007, 0.023],
    2: [0.827, 0.078, 0.0509],
    3: [0.8, 0.086, 0.007],
    4: [0.98,0.639,0.243],
}

def smallStar(pos,color,px = 1):
    x = pos[0]
    y = pos[1]
    glPointSize(px)
    glBegin(GL_POINTS)
    top = [x,y+px]
    bottom = [x,y-px]
    left = [x-px,y]
    right = [x+px,y]
    glColor3f(color[0],color[1],color[2])
    glVertex2f(x,y)
    glColor4f(color[0],color[1],color[2],0.5)
    glVertex2f(top[0],top[1])
    glVertex2f(bottom[0],bottom[1])
    glVertex2f(left[0],left[1])
    glVertex2f(right[0],right[1])
    glEnd()
    
class DRAWMATRIX:
    def draw(pos, drawArr, colorPalette, px = 1):
        x = len(drawArr)
        glPointSize(px)
        glBegin(GL_POINTS)
        for i in range(len(drawArr)):

            for j in range(len(drawArr[i])):
                if drawArr[i][j] > 0:
                    x_ = ((j+1)*px)-1 + pos[0]
                    y_ = ((x-i+1)*px)-1 + pos[1]
                    c = colorPalette[drawArr[i][j]]
                    glColor3f(c[0],c[1],c[2])
                    glVertex2f(x_,y_)
        glEnd()

def drawPoints(pos, color, px = 1):
    glPointSize(px)
    glBegin(GL_POINTS)
    glColor3f(color[0],color[1],color[2])
    glVertex2f(pos[0],pos[1])
    glEnd()

def drawMeteor(pos, color,px):
    x = pos[0]
    y = pos[1]
    drawPoints([x,y], color, 3*px)
    drawPoints([x+1.5*px,y+1.5*px], color, 2*px)
    drawPoints([x+3*px,y+3*px], color, 1*px)
    drawPoints([x+4*px,y+4*px], color, 1*px)
    drawPoints([x+5*px,y+5*px], color, 1*px)
    drawPoints([x+6*px,y+6*px], color, 1*px)
    drawPoints([x+8*px,y+8*px], color, 1*px)
    drawPoints([x+9*px,y+9*px], color, 1*px)
    drawPoints([x+11*px,y+11*px], color, 1*px)
    drawPoints([x+13*px,y+13*px], color, 1*px)
    drawPoints([x+17*px,y+17*px], color, 1*px)
    
    
        