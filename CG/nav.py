from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE = 600
PLANES = 500
x1, y1, x2, y2 = 0, 0, 0, 0


def plotGrid():
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(0.5, 0.5, 0.1)
    glVertex2f(0, PLANES)
    glVertex2f(0, -PLANES)
    glVertex2f(PLANES, 0)
    glVertex2f(-PLANES, 0)
    glEnd()


def plotLine():
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def disp():
    glClear(GL_COLOR_BUFFER_BIT)
    plotGrid()
    plotLine()
    glFlush()


def Init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutCreateWindow("o/p")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0, PLANES, 0, PLANES)


def readInput():
    global x1, y1, x2, y2
    x1 = int(input("Enter x1"))
    y1 = int(input("Enter y1"))
    x2 = int(input("Enter x2"))
    y2 = int(input("Enter y2"))


def main():
    readInput()
    Init()
    glutDisplayFunc(disp)
    glutMainLoop()


main()
