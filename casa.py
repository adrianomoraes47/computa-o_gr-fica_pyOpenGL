from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#import sys


def myInit():
    glClearColor(0, 0, 0, 1.0) 
    gluOrtho2D(0,500,0,500)

def display():
    

    glClear(GL_COLOR_BUFFER_BIT)

    
    #Quadrilátero que representa o telhado 
    glBegin(GL_QUADS)
    glColor3f(255,0,0)
    glVertex2f(200, 200)
    glVertex2f(250,300)
    glVertex2f(400,300)
    glVertex2f(400,200)
    glVertex2f(300,200)
    glEnd()

    #Quadrilátero que representa as paredes 
    glBegin(GL_QUADS)
    glColor3f(0,0,255)
    glVertex2f(200, 200)
    glVertex2f(200,100)
    glVertex2f(400,100)
    glVertex2f(400,200)
    glVertex2f(200,200)
    glEnd()

    #Quadrilátero que representa a porta  
    glBegin(GL_QUADS)
    glColor3f(0,255,0)
    glVertex2f(225, 100)
    glVertex2f(225,170)
    glVertex2f(275,170)
    glVertex2f(275,100)
    glEnd()

    #Quadrilátero que representa a janela 
    glBegin(GL_QUADS)
    glColor3f(0,255,0)
    glVertex2f(325, 130)
    glVertex2f(375,130)
    glVertex2f(375,170)
    glVertex2f(325,170)
    glEnd()

    # As linhas abaixo foram usadas para dar o contorno, ou seja, melhorando a visibilidade do desenho 
    glBegin(GL_LINE_STRIP)
    glColor3f(255,255,255)
    glVertex2f(200.0, 200.0) 
    glVertex2f(250.0, 300.0) 
    glVertex2f(300.0, 200.0)
    glVertex2f(200.0, 200.0)
    glEnd()

    glBegin(GL_LINE_STRIP) 
    glVertex2f(250,300)
    glVertex2f(400,300)
    glVertex2f(400,200)
    glVertex2f(300,200)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(255,250,250)
    glVertex2f(200,200)
    glVertex2f(200,100)
    glVertex2f(300,100)
    glVertex2f(300,200)
    glEnd()

    glBegin(GL_LINE_STRIP) 
    glVertex2f(225,100)
    glVertex2f(225,170)
    glVertex2f(275,170)
    glVertex2f(275,100)
    glEnd()

    glBegin(GL_LINE_STRIP) 
    glVertex2f(300,100)
    glVertex2f(400,100)
    glVertex2f(400,200)
    glEnd()

    glBegin(GL_LINE_STRIP) 
    glVertex2f(325,130)
    glVertex2f(375,130)
    glVertex2f(375,170)
    glVertex2f(325,170)
    glVertex2f(325,130)
    glEnd()

    glFinish()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(800, 800)  
glutInitWindowPosition(200, 700)
glutCreateWindow("Computacao Grafica_Casa")
myInit()
glutDisplayFunc(display)
glutMainLoop()