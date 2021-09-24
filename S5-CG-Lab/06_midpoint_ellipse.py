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


def plot_midpoint_ellipse(rx, ry, xc, yc):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x, y = 0, ry
    dp1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while dx < dy:
        plot_point((x + xc), (y + yc))
        plot_point((-x + xc), (y + yc))
        plot_point((x + xc), (-y + yc))
        plot_point((-x + xc), (-y + yc))

        if dp1 < 0:
            x += 1
            dx = dx + (2 * ry * ry)
            dp1 = dp1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            dp1 = dp1 + dx - dy + (ry * ry)

    dp2 = (
        ((ry * ry) * ((x + 0.5) * (x + 0.5)))
        + ((rx * rx) * ((y - 1) * (y - 1)))
        - (rx * rx * ry * ry)
    )

    while y >= 0:
        plot_point((x + xc), (y + yc))
        plot_point((-x + xc), (y + yc))
        plot_point((x + xc), (-y + yc))
        plot_point((-x + xc), (-y + yc))

        if dp2 > 0:
            y -= 1
            dy = dy - (2 * rx * rx)
            dp2 = dp2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            dp2 = dp2 + dx - dy + (rx * rx)
    glEnd()


def display(rx, ry, xc, yc):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_midpoint_ellipse(rx, ry, xc, yc)
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    rx = float(input("Radius along x axis: "))
    ry = float(input("Radius along y axis: "))
    xc = float(input("x-coordinate of center: "))
    yc = float(input("y-coordinate of center: "))
    init_glut()
    glutCreateWindow("Plot Point")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display(rx, ry, xc, yc))
    init_window()


if __name__ == "__main__":
    main()
