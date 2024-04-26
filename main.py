from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
# importing Assets
from midpointCircle import drawCircle
from midpointLine import drawLine
from jet.jet import *
from jetClass import Jet, jetThrust
from blinkblink import *
from bullet import *
from button import Button, Text
from hpbar import HealthBar
# ===============Keyboard Listener================
def keyboard(key, x, y):
    global gamepage, pausepage, homepage, levelpage, gameoverpage, animation_loop, delay, bullet_player
    if gamepage:
        if not delay[0]:
            if key == b'\x1b':
                pausepage = True
                gamepage = False
                delay = [True, (animation_loop-90)%100]
        
        if key == b'a':
            if player.pos[0] > 0:
                player.pos[0] = (player.pos[0] - 10)
        if key == b'd':
            if player.pos[0] < 800- player.size[0]:
                player.pos[0] = (player.pos[0] + 10)
                
        if key == b' ':
            bullet = Bullet([player.pos[0]+player.size[0]/2, player.pos[1]+player.size[1]], 10, [0,10],8)
            bullet_player.append(bullet)
            
    if pausepage:
        if not delay[0]:
            if key == b'\x1b':
                pausepage = False
                gamepage = True
                delay = [True, (animation_loop-90)%100]
          
def mouse(button, state, x, y):
    y = 800 - y
    global homepage, levelpage, gamepage, pausepage, gameoverpage, level, delay,animation_loop, gameDelay
    
    if homepage:
        if not delay[0]:
            if play_button.pressed(x, y):
                homepage = False
                levelpage = True
                delay = [True, (animation_loop-90)%100]
            if quitButton.pressed(x, y):
                glutLeaveMainLoop()
    elif levelpage:
        if not delay[0]:
            if level1_button.pressed(x, y):
                gameDelay = [True, (animation_loop-50)%100]
                level = 1
                levelpage = False
                gamepage = True
            if level2_button.pressed(x, y):
                gameDelay = [True, (animation_loop-50)%100]
                level = 2
                levelpage = False
                gamepage = True
            if backtoHomeButton.pressed(x, y):
                levelpage = False
                homepage = True
    
    elif pausepage:
        if not delay[0]:
            if restartButton.pressed(x, y):
                gameDelay = [True, (animation_loop-50)%100]
                resetGame()
                pausepage = False
                gamepage = True
            if resumeButton.pressed(x, y):
                pausepage = False
                gamepage = True
            if backHomeButton.pressed(x, y):
                resetGame()
                pausepage = False
                homepage = True
                delay = [True, (animation_loop-90)%100]
    elif gamepage:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            bullet = Bullet([player.pos[0]+player.size[0]/2, player.pos[1]+player.size[1]], 10, [0,10],8)
            bullet_player.append(bullet)
            
    elif gameoverpage:
        if not delay[0]:
            if restartButton.pressed(x, y):
                resetGame()
                gameoverpage = False
                gamepage = True
            if backHomeButton.pressed(x, y):
                resetGame()
                gameoverpage = False
                homepage = True
                delay = [True, (animation_loop-90)%100]

def resetGame():
    global bullet_player, player, enemy, enemy_bullet, score
    bullet_player = []
    enemy = []
    enemy_bullet = []
    player.health = 1000
    player_healthbar.health = player.health
    score = 0

def BACKGROUND():
    for i in range(50):
        DRAWMATRIX.draw(starpos[i], STARBIG, STARCOLOR, 1)
        DRAWMATRIX.draw(starpos2[i], STARBIG, STARCOLOR2, 1)
    
    for i in meteor:
        if i[0][0] < 800:
            drawMeteor(i[0], i[1], i[2])
    
        
    for i in range(800):
        smallStar(starpos3[i], [0.4,0.098,0.819], 1)
        
def HOMEPAGE():
    Text.draw("AFTERBURN", [178, 650], [0.858,0.505,0.482], 7)
    Text.draw("ASSAULT", [228, 580], [0.858,0.505,0.482], 7)
    play_button.draw(True)
    quitButton.draw(True)
    
def LEVELPAGE():
    global animation_loop
    Text.draw("CHOOSE LEVEL", [190, 580], [0.858,0.505,0.482], 5)
    level1_button.draw(True)
    level2_button.draw(True)
    backtoHomeButton.draw()
    Text.draw("HOME", [100, 714], [0.03,0.64,0.74], 4)
    
def GAMEPAGE():
    global animation_loop, level
    
    if player.health >= 0:
        Text.draw("HP "+str(player.health), [10, 770], [0.858,0.505,0.482], 1)
    
    player.draw()
    player_healthbar.draw(player.health)
    jetThrust([player.pos[0]+player.size[0]/2-8, player.pos[1]-15], 2)
    
    for i in range(len(enemy)):
        enemy[i].draw()
        enemy_healthbar[i].draw(enemy[i].health)
        
    for i in bullet_player:
        i.draw()
    
    for i in enemy_bullet:
        i.draw()
    
def PAUSEPAGE():
    restartButton.draw(True)
    resumeButton.draw(True)
    backHomeButton.draw(True)  

def GAMEOVERPAGE():
    global score
    
    x = (800-len(str(score))*4*7)/2
    Text.draw("GAME OVER", [180, 600], [0.858,0.505,0.482], 7)
    Text.draw("YOUR SCORE", [260, 530], [0.858,0.505,0.482], 4)
    Text.draw(str(score), [x, 480], [0.858,0.505,0.482], 4)
    restartButton.draw(True)
    backHomeButton.draw(True)
      
def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global animation_loop, homepage, levelpage, gamepage, pausepage, gameoverpage
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.074, 0.0627, 0.16, 1.0)
    glLoadIdentity()
    iterate()  
    # draw  
    BACKGROUND()
    
    if homepage:
        HOMEPAGE()
    elif levelpage:
        LEVELPAGE()
    elif gamepage:
        GAMEPAGE()
    elif pausepage:
        PAUSEPAGE()
    elif gameoverpage:
        GAMEOVERPAGE()
    
    glutSwapBuffers()
    
def backgroundAnimation():
    for i in range(50):
        starpos[i][1] = (starpos[i][1] - 1) % 800
        starpos2[i][1] = (starpos2[i][1] - 1.5) % 800
    for i in range(800):
        starpos3[i][1] = (starpos3[i][1] - 0.5) % 800
        
    for i in meteor:
        i[0][1] = (i[0][1] - i[2]*1.5) 
        i[0][0] = (i[0][0] - i[2]) 
        if i[0][1] < -17*i[2] or i[0][0] < -17*i[2]:
            i[0][0] = random.randint(0,1200)
            i[0][1] = 800
            i[2] = random.randint(1,3)

def generateEnemyBullet(i):  
    dx, dy = speedCheck(10,  player.pos[0], player.pos[1], i.pos[0], i.pos[1])
    if player.pos[0] < i.pos[0]:
        dx = -dx
    if dy > 0:
        dy = -dy
    enemy_bullet.append(Bullet([i.pos[0]+i.size[0]/2, i.pos[1]], 10, [dx,dy],8))     

def enemyBulletLogic():
    for i in enemy_bullet:
        i.move()
        if i.pos[1] < 0:
            enemy_bullet.remove(i)
        elif i.collision(player):
            player.health -= i.damage
            enemy_bullet.remove(i)
            
def enemyfunc():
    global animation_loop, enemy, enemy_bullet, enemy_healthbar, score
    if enemy == []:
        enemy.append(Jet([180, 700], ENEMY_JET, JET_COLOR,100, 2))
        enemy.append(Jet([380, 650], ENEMY_JET, JET_COLOR,400, 3))
        enemy.append(Jet([600, 700], ENEMY_JET, JET_COLOR,100, 2))
        enemy_healthbar.append(HealthBar(enemy[0].health,[enemy[0].size[0],3], [180,700+enemy[0].size[1]+5]))
        enemy_healthbar.append(HealthBar(enemy[1].health,[enemy[1].size[0],3], [380,650+enemy[1].size[1]+5]))
        enemy_healthbar.append(HealthBar(enemy[2].health,[enemy[2].size[0],3], [600,700+enemy[2].size[1]+5]))
    
    for i in enemy:
        if animation_loop>= 20 and animation_loop <= 40:
            if animation_loop % 5 == 0:
                generateEnemyBullet(i)
    
    enemyBulletLogic()
    
def playerBulletLogic():
    global score
    for i in bullet_player:
        i.move()
        if i.pos[1] > 800:
            bullet_player.remove(i)
        else:
            for j in enemy:
                if i.collision(j):
                    j.health -= i.damage
                    bullet_player.remove(i)
                    if j.health <= 0:
                        enemy_healthbar.remove(enemy_healthbar[enemy.index(j)])
                        enemy.remove(j)
                        score += 10
                        break

def playerfunc():
    global gamepage, gameoverpage
    
    if player.health <= 0:
        gamepage = False
        gameoverpage = True
        
    playerBulletLogic()
    
def game():
    global bullet_player, player, animation_loop
    
    enemyfunc()
    playerfunc()
    
def timeloop():
    global animation_loop, delay, gameDelay, timer_loop
    animation_loop = (animation_loop + 1) % 100
    if animation_loop % 10 == 0:
        timer_loop = (timer_loop + 1) % 100
        
    if delay[0]:
        if delay[1] == animation_loop:
            delay = [False, 0]
    if gameDelay[0]:
        if gameDelay[1] == animation_loop:
            gameDelay = [False, 0]
 
def animate(value):
    global animation_loop, delay, gameDelay
    
    timeloop()
    
    if not pausepage:
        backgroundAnimation()

    if gamepage:
        if not gameDelay[0]:
            game()
        
    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Afterburn Assault")
animation_loop = 0
timer_loop = 0
# background
starpos = []
starpos2 = []
starpos3 = []
meteor = []
for i in range(50):
    starpos.append([random.randint(0,800), random.randint(0,800)])
    starpos2.append([random.randint(0,800), random.randint(0,800)])
for i in range(800):
    starpos3.append([random.randint(0,800), random.randint(0,800)])

meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
# Page Logic
delay = [False, 0]
homepage = True
levelpage = False
gamepage = False
pausepage = False
gameoverpage = False
# Level Logic
level = 1
# ===================
# Button Logic - Homepage
play_button = Button([324,400], [0.58,0.749,0.56], 4, 3, ['PLAY'], [20,20])
quitButton = Button([324,300], [0.788,0.392,0.501], 4, 3, ['EXIT'], [20,20])

# Button Logic - Levelpage
level1_button = Button([282,400], [0.58,0.749,0.56], 4, 3, ['LEVEL 1'], [20,20])
level2_button = Button([282,300], [0.58,0.749,0.56], 4, 3, ['LEVEL 2'], [20,20])
# Universal Button
backtoHomeButton = Button([50,700], [0.03,0.64,0.74], 3, 1, [[0, 35, 0, 35, 35, 165, 35,165, 165, 165],[25, 50, 25, 0, 50, 50,0,0, 50, 0]], [5,5])
# pause menu button
restartButton = Button([282,370], [0.58,0.749,0.56], 4, 3, ['RESTART'], [20,20])
resumeButton = Button([282,470], [0.58,0.749,0.56], 4, 3, ['RESUME'], [34,20])
backHomeButton = Button([282,270], [0.58,0.749,0.56], 4, 3, ['HOME'], [62,20])
# Abilites
ability1 = [True, 0]
ability2 = [True, 0]
ability3 = [True, 0]

ability1_state = [False, 0]
ability2_state = [False, 0]
ability3_state = [False, 0]

# gamepage variables
gameDelay =[False, 0]
score = 0
bullet_player = []
enemy = []
enemy_healthbar = []    
enemy_bullet = []
player = Jet([100,70], JET, JET_COLOR,1000, 2)
# enemy = Jet([500,500], ENEMY_JET, JET_COLOR, 2)
player_healthbar = HealthBar(player.health,[100,10], [5,760])

glutDisplayFunc(showScreen)
animate(5)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
# glutSpecialFunc(specialKeyListener)

glutMainLoop()