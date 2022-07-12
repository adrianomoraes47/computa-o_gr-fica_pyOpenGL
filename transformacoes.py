print("PARA USAR O PROGRAMA UTILIZE AS SEGUINTES TECLAS:\nOBS: VALORIZE A DIFERENÇA ENTRE LETRAS MAIÚSCULAS E MINÚSCULAS")
print("a - PRA ESQUERDA")
print("d - PRA DIREITA")
print("w - PRA CIMA")
print("s - PRA BAIXO")
print("+ - AUMENTA A ESCALA DO DESENHO")
print("- - DIMINUI A ESCALA DO DESENHO")
print("r - ROTACIONA")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

escala = 1
tran_x = 0
tran_y = 0
rotacao = 1


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-15,15,-15,15)
    glScalef(escala, escala, 0)
    glTranslatef(tran_x, tran_y, 0)
    glRotatef(rotacao,rotacao, rotacao, 0)
    glBegin(GL_QUADS)
    glColor3f(0,0,255)
    glVertex2f(-2,2)
    glVertex2f(2,2)
    glVertex2f(2,-2)
    glVertex2f(-2,-2)
    glEnd()

    glFlush()


def teclado(key, x, y):
    global escala, tran_y, tran_x, rotacao, ang

    if ord(key) == 119:
        tran_y = tran_y + 1
    elif ord(key) == 115:
        tran_y = tran_y - 1
    elif ord(key) == 100:
        tran_x = tran_x + 1
    elif ord(key) == 97:
        tran_x = tran_x - 1
    elif ord(key) == 43: 
        escala = escala + 1 
    elif ord(key) == 45: 
        escala = escala - 1
    elif ord(key) == 114: 
        rotacao = rotacao + 1
    elif ord(key) == 82: 
        rotacao = rotacao - 1 
    display()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("My OpenGL Code")
glClearColor(1, 0, 0, 0)
glutKeyboardFunc(teclado)
glutDisplayFunc(display) 
glutMainLoop()



