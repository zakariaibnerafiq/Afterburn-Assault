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

from button import Button
from hpbar import HealthBar
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
    
    if homepage:
        number_button.draw(True)
        lineButton.draw(True)
    elif levelpage:
        pass
    elif gamepage:
        pass
    elif pausepage:
        pass
    elif gameoverpage:
        pass
    
    player.draw()
    player_healthbar.draw(player.health)
    num.draw(str(animation_loop), [100, 700],[1,1,1],5)
    num.draw(str(animation_loop), [100, 500],[1,1,1],5)
    
    glutSwapBuffers()


def animate(value):
    global animation_loop
    animation_loop = (animation_loop + 1) % 100
    
    if animation_loop % 2 == 0:
        player.health -= 1
        if player.health <= 0:
            player.health = 100
    
    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Shoot the circles!")
animation_loop = 0
# Page Logic
homepage = True
levelpage = False
gamepage = False
pausepage = False
gameoverpage = False

number_button = Button([200,700], [1,1,1], 8, 3, ['EXIT'])

lineButton = Button([200,600], [1,1,1], 6, 1, [[0, 0, 0, 50,0,50],[0, 50, 50, 25,0,25]])
player = Jet([100,100], JET, JET_COLOR, 2)
num = Number()
player_healthbar = HealthBar(100,[50,10], [5,760])
glutDisplayFunc(showScreen)
animate(5)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)

glutMainLoop()