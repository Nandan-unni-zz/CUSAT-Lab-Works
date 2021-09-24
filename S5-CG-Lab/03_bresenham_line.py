# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

size = 100


def plot_point(x, y):
    glVertex2f(x / size, y / size)


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


def plot_bresenham_line(x1, y1, x2, y2):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    plot_point(x1, y1)
    dy = y2 - y1
    dx = x2 - x1
    if dx > dy:
        m = 2 * dy
        dp = m - dx
        y = y1
        for x in range(x1, x2 + 1):
            plot_point(x, y)
            dp = dp + m
            if dp >= 0:
                y = y + 1
                dp = dp - 2 * (dx)
        plot_point(x2, y2)
    else:
        m = 2 * dx
        dp = m - dy
        x = x1
        for y in range(y1, y2 + 1):
            plot_point(x, y)
            dp = dp + m
            if dp >= 0:
                x = x + 1
                dp = dp - (2 * dy)
        plot_point(x2, y2)
    glEnd()


def display(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_bresenham_line(x1, y1, x2, y2)
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    x1 = int(input("Enter the initial x coordinate: "))
    y1 = int(input("Enter the initial y coordinate: "))
    x2 = int(input("Enter the final x coordinate: "))
    y2 = int(input("Enter the final y coordinate: "))
    init_glut()
    glutCreateWindow("Title")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display(x1, y1, x2, y2))
    init_window()


if __name__ == "__main__":
    main()
