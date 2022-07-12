print("PARA USAR O PROGRAMA UTILIZE AS SEGUINTES TECLAS:\nOBS: VALORIZE A DIFERENÇA ENTRE LETRAS MAIÚSCULAS E MINÚSCULAS")
print("a - PRA ESQUERDA")
print("d - PRA DIREITA")
print("w - PRA CIMA")
print("s - PRA BAIXO")
print("e - DIAGONAL PRA DIREITA")
print("q - DIAGONAL PRA ESQUERDA")
print("c - DIAGONAL PARA BAIXO PRA DIREITA")
print("z - DIAGONAL BAIXO PRA ESQUERDA")


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL._bytes import as_8_bit


PROMPT = ("ANA")
x = 130
y = 150

def display1():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        x -= 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display2():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        x += 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display3():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y += 10
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display4():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y -= 10
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display5():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y += 10.0 
        x += 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display6():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y += 10.0 
        x -= 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display7():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y -= 10.0 
        x += 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display8():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        y -= 10.0 
        x -= 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glFlush()

def display9():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,300,0,300)
    glColor3f(255,255,255)
    glRasterPos2d(x,y)
    for s in PROMPT:
        glRasterPos(x, y)
        x += 10.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    glFlush()

def teclado(key, x, y):
    if ord(key) == 97:
        print("PRA ESQUERDA")
        display1()
    elif ord(key) == 100:
        print("PRA DIREITA")
        display2()
    elif ord(key) == 119:
        print("PRA CIMA")
        display3()
    elif ord(key) == 115:
        print("PRA BAIXO")
        display4()
    elif ord(key) == 101:
        print("DIAGONAL DIREITA PRA CIMA")
        display5()
    elif ord(key) == 113:
        print("DIAGONAL ESQUERDA PRA CIMA")
        display6()
    elif ord(key) == 99:
        print("DIAGONAL DIREITA PRA BAIXO")
        display7()
    elif ord(key) == 122:
        print("DIAGONAL ESQUERDA PRA BAIXO")
        display8()
    elif ord(key) == 43:
        print("DIAGONAL ESQUERDA PRA BAIXO")
        display9()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("COMPUTACAO_GRAFICA_TEXTO")
glClearColor(0, 0, 0, 1)
glutKeyboardFunc(teclado)
glutDisplayFunc(display1) 
glutMainLoop()