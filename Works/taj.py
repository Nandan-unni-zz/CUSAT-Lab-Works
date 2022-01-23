# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Taj Mahal"
WINDOW_SIZE = 500
PLANE_SIZE = 100


def init():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glFlush()


def main():
    init()
    glutDisplayFunc(display)  # display function
    glutMainLoop()  # process events and triggers callback functions


main()
