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

class DRAWMATRIX:
    def draw(self, pos, drawArr, colorPalette, px = 1):
        x = len(drawArr)
        glPointSize(px)
        glBegin(GL_POINTS)
        for i in range(len(drawArr)):
            print(i)
            for j in range(len(drawArr[i])):
                if drawArr[i][j] > 0:
                    x_ = ((j+1)*px)-1 + pos[0]
                    y_ = ((x-i+1)*px)-1 + pos[1]
                    c = colorPalette[drawArr[i][j]]
                    glColor3f(c[0],c[1],c[2])
                    glVertex2f(x_,y_)
        
        glEnd()
        
        