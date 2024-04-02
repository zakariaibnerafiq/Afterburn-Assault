from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# importing Assets
from components import *
from midpointCircle import drawCircle
from midpointLine import drawLine
from jet import JET

# ===============Keyboard Listener================


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global score
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 1.0)
    glLoadIdentity()
    iterate()  
    # draw  
    drawCircle([400,400],100,[1,1,1],2)
    drawMatrix(JET, 10, [100,100])
    glutSwapBuffers()


def animate(value):
    
    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Shoot the circles!")


glutDisplayFunc(showScreen)
animate(5)

glutMainLoop()