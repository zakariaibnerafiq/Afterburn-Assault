from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# importing Assets
from components import *
from midpointCircle import drawCircle
from midpointLine import drawLine
from jet.jet import JET, JET_COLOR
from jetClass import Jet
# ===============Keyboard Listener================

def keyboard(key, x, y):
    global angle
    if key == b"q":
        angle = (angle + 10) % 360

def mouse(button, state, x, y):
    button = button    
        
def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global animation_loop
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 1.0)
    glLoadIdentity()
    iterate()  
    # draw  
    player.draw(boundary= True)
    num.draw(str(animation_loop), [100, 700],[1,1,1],2)
    num.draw(str(animation_loop), [100, 500],[1,1,1],2)
    
    glutSwapBuffers()


def animate(value):
    global animation_loop
    animation_loop = (animation_loop + 1) % 100
    
    
    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Shoot the circles!")
animation_loop = 0

player = Jet([100,100], JET, JET_COLOR, 2)
num = Number()

glutDisplayFunc(showScreen)
animate(5)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)

glutMainLoop()