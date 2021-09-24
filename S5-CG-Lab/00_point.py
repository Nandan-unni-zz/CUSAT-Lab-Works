# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

size = 100


def init_glut():
    # initiate GLUT
    glutInit()
    # initiate the display mode with RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


def init_window():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # background color
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # foreground color
    glutMainLoop()  # process events and triggers callback functions


def plot_x_y_axis():
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


def plot_point(x, y):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x / size, y / size)
    glEnd()


def display(x, y):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_point(x, y)
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    x = int(input("Enter x-coordinate : "))
    y = int(input("Enter y-coordinate : "))
    init_glut()
    glutCreateWindow("Plot Point")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display(x, y))
    init_window()


if __name__ == "__main__":
    main()
