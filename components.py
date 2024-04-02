from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpointLine import drawLine
from midpointCircle import drawCircle

class Cross:
    def __init__(self, x = 0, y = 0, size = 10, color = [1,1,1],px=2):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.px = px
    
    def draw(self):
        drawLine(self.x,self.y,self.x+self.size,self.y+self.size,self.color,self.px)
        drawLine(self.x,self.y+self.size,self.x+self.size,self.y,self.color,self.px)
        
    def pressed(self, x, y):
        if self.x < x < self.x + self.size and self.y < y < self.y + self.size:
            print("Close")
            return True
        return False

class Pause:
    def __init__(self, x = 0, y = 0, size = 10, color = [1,1,1],px=2):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.px = px
    def play(self):
        drawLine(self.x,self.y,self.x,self.y+self.size,self.color,self.px)
        drawLine(self.x,self.y,self.x+self.size,self.y+self.size/2,self.color,self.px)
        drawLine(self.x,self.y+self.size,self.x+self.size,self.y+self.size/2,self.color,self.px)
    def pause(self):
        drawLine(self.x,self.y,self.x,self.y+self.size,self.color,self.px)
        drawLine(self.x+self.size,self.y,self.x+self.size,self.y+self.size,self.color,self.px)
    def draw(self, p ):
        if p:
            self.play()
        else:
            self.pause()
    def pressed(self, x, y):
        if self.x < x < self.x + self.size and self.y < y < self.y + self.size:
            print("Pause")
            return True
        return False

class Reset:
    def __init__(self, x = 0, y = 0, size = 10, color = [1,1,1], px=2):
        self.x = x
        self.y = y
        self.size = size

        self.color = color
        self.px = px
    def draw(self):
        drawLine(self.x,self.y+self.size/2,self.x+self.size,self.y+self.size/2,self.color,self.px)
        drawLine(self.x,self.y+self.size/2,self.x+self.size/3,self.y,self.color,self.px)
        drawLine(self.x,self.y+self.size/2,self.x+self.size/3,self.y+self.size,self.color,self.px)
        
    def pressed(self, x, y):
        if self.x < x < self.x + self.size and self.y < y < self.y + self.size:
            print("Restart")
            return True
        return False

class Slider:
    def __init__(self, x, y, size, color = [1,1,1], px=2):
        self.size = size
        self.color = color
        self.px = px
        self.x = int(x - size/2)
        self.y = y
    
    def draw(self):
        rad = int(self.size/2)
        center = [self.x + rad, self.y + rad]
        drawCircle(center, rad, self.color, self.px)
    
    def goRight(self, sp):
        if self.x + self.size < 800:
            self.x += sp
    def goLeft(self, sp):
        if self.x > 0:
            self.x -= sp
        
class Ball:
    def __init__(self, x, y, radius, color = [1,1,1], px=2):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.px = px
        self.size = radius*2
    
    def draw(self):
        center = [self.x + self.radius, self.y + self.radius]
        if self.y < 700:
            drawCircle(center, self.radius, self.color, self.px)
    
    def move(self, dy):
        self.y -= dy 
    
    def checkCollision(self, item):
        # if item bottom is in range of the object
        if item.y <= self.y + self.size and item.y >= self.y:
            # if item left is in range of the object
            if item.x >= self.x and item.x <= self.x + self.size:
                return True
            
            # if item right is in range of the object
            elif item.x + item.size >= self.x and item.x + item.size <= self.x + self.size:
                return True
            
        # if item top is in range of the object
        elif item.y + item.size <= self.y + self.size and item.y + item.size >= self.y:
            # if item left is in range of the object
            if item.x >= self.x and item.x <= self.x + self.size:
                return True
            
            # if item right is in range of the object
            elif item.x + item.size >= self.x and item.x + item.size <= self.x + self.size:
                return True
            
        return False

class Number:
    def __init__(self):
        self.numbers = {
            0: [[0,1,1,1,0],
                [1,1,0,1,1],
                [1,1,0,1,1],
                [1,1,0,1,1],
                [1,1,0,1,1],
                [1,1,0,1,1],
                [0,1,1,1,0]],
            1: [[0,0,1,1,0,0],
                [0,1,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0]],
            2: [[0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [0,0,0,0,1,1],
                [0,0,1,1,1,0],
                [0,1,1,0,0,0],
                [1,1,0,0,0,0],
                [1,1,1,1,1,1]],
            3: [[0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [0,0,0,0,1,1],
                [0,0,1,1,1,0],
                [0,0,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0]],
            4: [[0,0,0,1,1,0],
                [0,0,1,1,1,0],
                [0,1,0,1,1,0],
                [1,0,0,1,1,0],
                [1,1,1,1,1,1],
                [0,0,0,1,1,0],
                [0,0,0,1,1,0]],
            5: [[1,1,1,1,1,1],
                [1,0,0,0,0,0],
                [1,1,1,1,1,0],
                [0,0,0,0,1,1],
                [0,0,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0]],
            6: [[0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [1,1,0,0,0,0],
                [1,1,1,1,1,0],
                [1,1,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0]],
            7: [[1,1,1,1,1,1],
                [0,0,0,0,1,1],
                [0,0,0,1,1,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0]],
            8: [[0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0]],
            9: [[0,1,1,1,1,0],
                [1,1,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,1],
                [0,0,0,0,1,1],
                [1,1,0,0,1,1],
                [0,1,1,1,1,0]]
        }
    def drawMatrix(self,x,px, offset):
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] == 1:
                    x_ = ((j+1)*px)-1 + offset[0]
                    y_ = ((7-i+1)*px)-1 + offset[1]
                    glVertex2f(x_,y_)
        
    def draw(self,string,offset,color,px):
        glColor3f(color[0], color[1], color[2])
        glPointSize(px) 
        glBegin(GL_POINTS)
        x, y = offset
        for i in range(len(string)):
            self.drawMatrix(self.numbers[int(string[i])], px, [x,y])
            x += px*7
        glEnd()
from jet import JET, JET_COLOR

def drawMatrix(arr,px, offset):
    x = len(arr)
    glPointSize(px)
    glBegin(GL_POINTS)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > 0:
                x_ = ((j+1)*px)-1 + offset[0]
                y_ = ((x-i+1)*px)-1 + offset[1]
                c = JET_COLOR[arr[i][j]]
                glColor3f(c[0],c[1],c[2])
                glVertex2f(x_,y_)
    glEnd()
class Bullet:
    def __init__(self, center, size, color = [1,1,1], px=1):
        self.radius = int(size/2)
        self.x = center[0] - self.radius
        self.y = center[1] - self.radius
        self.size = size
        self.color = color
        self.px = px  
    
    def draw(self):
        center = [self.x + self.radius, self.y + self.radius]
        drawCircle(center, self.radius, self.color, self.px)
    
    def move(self, dy):
        self.y += dy
        
if __name__ == "__main__":
    pass