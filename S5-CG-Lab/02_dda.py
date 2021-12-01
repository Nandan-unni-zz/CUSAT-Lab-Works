# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE = 500
PLANE_SIZE = 100


def init_glut():
    # initiate GLUT
    glutInit()
    # initiate the display mode with RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


def init_window():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # background color
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)
    glutMainLoop()  # process events and triggers callback functions


def plot_x_y_axis():
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    # Y-axis
    glVertex2f(0.0, PLANE_SIZE)
    glVertex2f(0.0, -PLANE_SIZE)
    # X-axis
    glVertex2f(-PLANE_SIZE, 0.0)
    glVertex2f(PLANE_SIZE, 0.0)
    glEnd()


def plot_dda_line(x1, y1, x2, y2):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    if abs(x2 - x1) > abs(y2 - y1):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1
    y = y1
    glVertex2f(x1, y1)
    for _ in range(length):
        x = x + dx
        y = y + dy
        glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()


def display(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_dda_line(x1, y1, x2, y2)
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    x1 = int(input("Enter the initial x coordinate: "))
    y1 = int(input("Enter the initial y coordinate: "))
    x2 = int(input("Enter the final x coordinate: "))
    y2 = int(input("Enter the final y coordinate: "))
    init_glut()
    glutCreateWindow("Title")  # create window
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display(x1, y1, x2, y2))
    init_window()


if __name__ == "__main__":
    main()
