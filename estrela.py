from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myInit():
    glClearColor(0, 0, 0, 1.0) 
    glColor3f(255,255,255)
    gluOrtho2D(0, 700, 0, 700)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    #TRAÇADO DA ESTRELA (VARIAÇÕES DE VALORES DE 50 ou 100 NAS DIREÇÕES X E Y)

    glBegin(GL_LINE_STRIP)

    glVertex2f(400.0, 400.0)

    glVertex2f(450.0, 500.0)

    glVertex2f(500.0, 400.0)

    glVertex2f(600.0, 350.0)

    glVertex2f(500.0, 300.0)

    glVertex2f(450.0, 200.0)

    glVertex2f(400.0, 300.0)

    glVertex2f(300.0, 350.0)

    glVertex2f(400.0, 400.0)

    glEnd()



    #lINHAS PARA CAUSAR EFEITO VISUAL - APENAS LIGAÇÕES DE VERTICES 
    glBegin(GL_LINES)

    #LINHA MAIOR VERTICAL
    glVertex2f(450.0, 500.0)
    glVertex2f(450.0, 200.0)

    #LINHA DIAGONAL 
    glVertex2f(500.0, 400.0)
    glVertex2f(400.0, 300.0)

    #LINHA DIAGOAL 2 (DO PONTO 5 - ATÉ ORIGEM)
    glVertex2f(500.0, 300.0)
    glVertex2f(400.0, 400.0)

    #LINHA MAIOR HORIZONTAL 
    glVertex2f(600.0, 350.0)
    glVertex2f(300.0, 350.0)

    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(800, 800)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("Computacao_Grafica_Estrela")
myInit()
glutDisplayFunc(display)
glutMainLoop()