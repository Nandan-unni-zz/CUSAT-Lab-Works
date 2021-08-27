# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init_glut():
    # initiate GLUT
    glutInit()
    # initiate the display mode with RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


def init_window():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # background color
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # foreground color
    glutMainLoop()  # process events and triggers callback functions


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # plot func here

    glFlush()  # clean buffer


def main():
    init_glut()
    glutCreateWindow("Plot Point")  # create window
    glutInitWindowSize(500, 500)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(display)
    init_window()


if __name__ == "__main__":
    main()
