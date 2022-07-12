from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def myInit():
    glClearColor(0, 0, 0, 1.0) 
    glColor3f(255,255,255)
    gluOrtho2D(0, 700, 0, 700)

def display():

    glClear(GL_COLOR_BUFFER_BIT)


    glBegin(GL_LINE_STRIP)

    glVertex2d(200, 300)

    glVertex2d(350, 500)

    glVertex2d(360, 200)

    glVertex2d(200, 300)


    glEnd()

    glBegin(GL_LINE_STRIP)

    glVertex2d(350, 500)

    glVertex2d(500, 300)

    glVertex2d(360, 200)

    glEnd()


    glBegin(GL_LINE_STRIP)

    glVertex2d(200, 300)

    glVertex2d(340, 350)

    glVertex2d(500, 300)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glVertex2d(340, 350)

    glVertex2d(350, 500)

    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(800, 800)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("Questao 1_Computacao Grafica_Estrela")
myInit()
glutDisplayFunc(display)
glutMainLoop()