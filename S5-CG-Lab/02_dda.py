# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def plot_point():
    x1 = int(input("Enter the initial x coordinate: "))
    y1 = int(input("Enter the initial y coordinate: "))
    x2 = int(input("Enter the final x coordinate: "))
    y2 = int(input("Enter the final y coordinate: "))
    if abs(x2 - x1) > abs(y2 - y1):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1
    y = y1
    glClear(GL_COLOR_BUFFER_BIT)
    # points
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x1 / 50, y1 / 50)
    for i in range(length):
        x = x + dx
        y = y + dy
        glVertex2f(x / 50, y / 50)
    glVertex2f(x2 / 50, y2 / 50)
    glEnd()


def plot():
    plot_point()
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    # Y-axis
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    # X-axis
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("DDA")
glutInitWindowSize(10, 10)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot)
clearScreen()
glutMainLoop()
