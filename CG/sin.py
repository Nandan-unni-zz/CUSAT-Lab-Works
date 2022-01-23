# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
# PLANE_SIZE =
X = 0


def get_inputs():
    global X
    X = float(input("Enter X: "))


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(1024, 768)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-720, 720, -2, 2)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-720, 0)
    glVertex2f(720, 0)
    glVertex2f(0, 2)
    glVertex2f(0, -2)
    glEnd()
    glColor3f(1.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for x in range(-720, 721):
        if not x == 0:
            glVertex2f(x, (sin(radians(x))) / radians(x))
    glEnd()
    glFlush()


def main():
    # get_inputs()
    init_glut()
    glutDisplayFunc(display)  # display function
    glutMainLoop()  # process events and triggers callback functions


main()
