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

    glVertex2d(300, 400)

    glVertex2d(500, 400)

    glVertex2d(500, 200)

    glVertex2d(300, 200)

    glVertex2d(300, 400)

    glVertex2d(400, 500)

    glVertex2d(585, 500)

    glVertex2d(500, 400)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glVertex2d(400, 500)

    glVertex2d(400, 300)

    glVertex2d(300, 200)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glVertex2d(585, 500)

    glVertex2d(585, 300)

    glVertex2d(500, 200)

    glEnd()




    glBegin(GL_LINE_STRIP)

    glVertex2d(585, 300)

    glVertex2d(400, 300)


    glEnd()


    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(800, 800)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("COMPUTACAO_GRAFICA_CUBO")
myInit()
glutDisplayFunc(display) 
glutMainLoop()