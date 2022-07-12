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
teste = 0


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


def temporizador(value):
    global escala, tran_y, tran_x, rotacao, ang, teste
    if teste == 1:
        escala = escala + 0.005
    elif teste == 2:
        escala = escala - 0.005
    elif teste == 3:
        tran_y = tran_y + 0.005
    elif teste == 4:
        tran_y = tran_y - 0.005
    elif teste == 5:
        tran_x = tran_x + 0.005
    elif teste == 6:
        tran_x = tran_x - 0.005
    elif teste == 7:
        rotacao = rotacao + 1
    elif teste == 8:
        rotacao = rotacao - 1
    glutTimerFunc(10,temporizador, 1)
    display()

def teclado(key, x, y):
    global escala, tran_y, tran_x, rotacao, ang, teste 

    if ord(key) == 119:
        teste = 3 
    elif ord(key) == 115:
        teste = 4
    elif ord(key) == 100:
        teste = 5 
    elif ord(key) == 97:
        teste = 6 
    elif ord(key) == 43: 
        teste = 1
    elif ord(key) == 45: 
        teste = 2
    elif ord(key) == 114:
        teste = 7 
    elif ord(key) == 82:
        teste = 8
    display()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(500, 500)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("ANIMACOES")
glClearColor(1, 0, 0, 0)
glutTimerFunc(10,temporizador, 1)
glutKeyboardFunc(teclado)
glutDisplayFunc(display) 
glutMainLoop()