from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# importing Assets
from midpointCircle import drawCircle
from midpointLine import drawLine
from jet.jet import *
from jetClass import Jet, jetThrust
from bullet import Bullet

# ===============Keyboard Listener================

def specialKeyListener(key, x, y):
    global cor2, bxx
    glutPostRedisplay()
    
    if key==GLUT_KEY_RIGHT:
        player.pos[0] = (player.pos[0] + 5) % 800
    if key==GLUT_KEY_LEFT:
        player.pos[0] = (player.pos[0] - 5) % 800

def keyboard(key, x, y):
    global animation_loop, delay
          
def mouse(button, state, x, y):
    y = 800 - y
  
def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global animation_loop
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.074, 0.0627, 0.16, 1.0)
    glLoadIdentity()
    iterate()  
    # draw  
    player.draw()
    glutSwapBuffers()

def game():
 
      
    global animation_loop
    
    # enemy.pos[0] = (enemy.pos[0] + 1) % 800
    
            
def animate(value):
    global animation_loop, delay
    animation_loop = (animation_loop + 1) % 100

    if delay[0]:
        if delay[1] == animation_loop:
            delay = [False, 0]

    game()
        

    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Afterburn Assault")
animation_loop = 0
# background

delay = [False, 0]

player = Jet([100,70], JET, JET_COLOR, 2)
# enemy = Jet([500,500], ENEMY_JET, JET_COLOR, 2)
bullet = Bullet([100,100], 10, 1)
glutDisplayFunc(showScreen)
animate(5)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutSpecialFunc(specialKeyListener)


glutMainLoop()