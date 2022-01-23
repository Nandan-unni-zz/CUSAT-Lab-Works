from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

x = 0
y = 0


def glut_init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()
    glutInitWindowSize(1024, 768)
    glutCreateWindow("string")
    gluOrtho2D(-720, 720, -360, 360)
    glClearColor(1.0, 1.0, 1.0, 1.0)


def inputt():
    global x, y
    x = int(input("enter the number"))
    y = int(input("enter y "))


def display():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0, 360)
    glVertex2f(0, -360)
    glVertex2f(720, 0)
    glVertex2f(-720, 0)
    glEnd()
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    inputt()
    glut_init()
    glutDisplayFunc(display)
    glutMainLoop()


main()
