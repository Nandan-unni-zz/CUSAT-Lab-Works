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


def plot_bresenham_line(x1, y1, x2, y2):
    # Implement Bresenhams Algorithm
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    dyGreater = dy > dx

    # Set the initial points
    x, y = x1, y1

    if dyGreater:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    m = 2 * dy
    p = m - dx  # initial value for p (decision parameter)

    # Init line plotting
    glColor3f(0.0, 1.0, 0.0)  # Set the color in RGB
    glPointSize(5.0)  # Set the size of the point
    glBegin(GL_POINTS)

    # Loop from x1 to x2+1 and plot each points
    glVertex2f(y, x) if dyGreater else glVertex2f(x, y)
    for x in range(x1, x2 + 1):
        glVertex2f(y, x) if dyGreater else glVertex2f(x, y)
        # plot the point
        if p < 0:
            p = p + m  # Initial value
        else:
            y = y + 1
            p = p + m - (2 * dx)
    glVertex2f(y, x) if dyGreater else glVertex2f(x, y)

    glEnd()
    # glColor3f(0.0, 0.0, 1.0)
    # glPointSize(5.0)
    # glBegin(GL_POINTS)
    # glVertex2f(x1, y1)
    # dy = y2 - y1
    # dx = x2 - x1
    # if dx > dy:
    #     m = 2 * dy
    #     dp = m - dx
    #     y = y1
    #     for x in range(x1, x2 + 1):
    #         glVertex2f(x, y)
    #         dp = dp + m
    #         if dp >= 0:
    #             y = y + 1
    #             dp = dp - 2 * (dx)
    #     glVertex2f(x2, y2)
    # else:
    #     m = 2 * dx
    #     dp = m - dy
    #     x = x1
    #     for y in range(y1, y2 + 1):
    #         glVertex2f(x, y)
    #         dp = dp + m
    #         if dp >= 0:
    #             x = x + 1
    #             dp = dp - (2 * dy)
    #     glVertex2f(x2, y2)
    # glEnd()


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
    glutCreateWindow("Bresenham Line")  # create window
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display(x1, y1, x2, y2))
    init_window()


if __name__ == "__main__":
    main()
