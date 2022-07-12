from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL._bytes import as_8_bit

PROMPT = ("COMPUTAÇÃO GRÁFICA")
PROMPT_1 = ("UFMA - ENGENHARIA DA COMPUTAÇÃO")
PROMPT_2 = ("a - ANIMAÇÕES DE TEXTO")
PROMPT_3 = ("b - TRANSFORMAÇÕES GEOMÉTRICAS")
PROMPT_4 = ("c - CASA")
PROMPT_5 = ("d - PIRÂMIDE")
PROMPT_6 = ("e - CUBO")
PROMPT_7 = ("f - ESTRELA")
PROMPT_8 = ("g - ANIMAÇÕES")


x = 65
y = 250

z = 43
w = 230

g = 25
h = 150

n = 25
m = 140

l = 25
k = 130

Q = 25
A = 120

T = 25
V = 110

B = 25
X = 100

S = 25 
Z = 90 



def display():
    global x, y, z, w, g, h, n, m, l, k, Q, A, T, V, B, X, S, Z
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

    glRasterPos2d(z,w)
    for d in PROMPT_1:
        glRasterPos(z, w)
        z += 7.0
        for e in d:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(e))

    glRasterPos2d(g,h)
    for i in PROMPT_2:
        glRasterPos(g, h)
        g += 7.0
        for j in i:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(j))

    glRasterPos2d(n,m)
    for u in PROMPT_3:
        glRasterPos(n, m)
        n += 7.0
        for U in u:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(U))

    glRasterPos2d(l,k)
    for K in PROMPT_4:
        glRasterPos(l, k)
        l += 7.0
        for O in K:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(O))

    glRasterPos2d(Q,A)
    for p in PROMPT_5:
        glRasterPos(Q, A)
        Q += 7.0
        for L in p:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(L))

    glRasterPos2d(T,V)
    for E in PROMPT_6:
        glRasterPos(T, V)
        T += 7.0
        for r in E:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(r))

    glRasterPos2d(B,X)
    for J in PROMPT_7:
        glRasterPos(B, X)
        B += 7.0
        for R in J:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(R))

    glRasterPos2d(S,Z)
    for N in PROMPT_8:
        glRasterPos(S, Z)
        S += 7.0
        for H in N:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(H))

    glFlush()

def teclado(key, x, y):
    if ord(key) == 97:
        import texto
    elif ord(key) == 98:
        import transformacoes
    elif ord(key) == 99:
        import casa
    elif ord(key) == 100:
        import piramide
    elif ord(key) == 101:
        import cubo
    elif ord(key) == 102:
        import estrela
    elif ord(key) == 103:
        import animacoes
    display()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(1000, 1000)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("_MENU_INICIAL_")
glClearColor(0, 0, 0, 1)
glutKeyboardFunc(teclado)
glutDisplayFunc(display) 
glutMainLoop()