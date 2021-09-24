# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sin, cos, pi, sqrt

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


def plot_8_parts(x, y, xc, yc):
    plot_point((x + xc), (y + yc))  # I - top
    plot_point((-x + xc), (-y + yc))  # III - down
    plot_point((x + xc), (-y + yc))  # IV - down
    plot_point((-x + xc), (y + yc))  # II - top
    plot_point((y + xc), (x + yc))  # I - down
    plot_point((-y + xc), (-x + yc))  # III - top
    plot_point((y + xc), (-x + yc))  # IV - top
    plot_point((-y + xc), (x + yc))  # II - down


def mid_point_circle(r, xc, yc):
    x = 0
    y = r

    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    plot_point((x + xc), (y + yc))
    dp = (5 / 4) - r
    while x < y:
        x = x + 1
        if dp < 0:
            dp = dp + (2 * x) + 1
        else:
            y = y - 1
            dp = dp + (2 * x) - (2 * y) + 1
        plot_8_parts(x, y, xc, yc)
    glEnd()


def polar_point_circle(r, xc, yc):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    thetta = 0
    d_thetta = 1 / r
    thetta_end = pi / 4
    while thetta < thetta_end:
        x = r * cos(thetta)
        y = r * sin(thetta)
        plot_8_parts(x, y, xc, yc)
        thetta += d_thetta
    glEnd()


def nonpolar_point_circle(r, xc, yc):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    dp = 3 - (2 * r)
    x = 0
    y = r
    while x <= y:
        plot_8_parts(x, y, xc, yc)
        if dp < 0:
            dp = dp + (4 * x) + 6
        else:
            dp = dp + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
    glEnd()


def display(choice, r, xc, yc):
    glClear(GL_COLOR_BUFFER_BIT)

    if choice == 1:
        mid_point_circle(r, xc, yc)
    elif choice == 2:
        polar_point_circle(r, xc, yc)
    elif choice == 3:
        nonpolar_point_circle(r, xc, yc)

    plot_x_y_axis()
    glFlush()  # clean buffer


def main():
    choice = 0
    while not choice == 4:
        print("_____________________________________\n")
        # r, xc, yc = 50, 30, 30
        r = int(input("Enter Radius: "))
        xc = int(input("Enter x coordinate of center: "))
        yc = int(input("Enter y coordinate of center: "))
        print("\n1. Mid Point circle Algorithm")
        print("2. Polar Point circle Algorithm")
        print("3. Non-Polar Point circle Algorithm")
        print("4. Exit")
        choice = int(input("\nSelect Algorithm: "))
        if choice in [1, 2, 3]:
            init_glut()
            glutCreateWindow("Plot Circle")  # create window
            glutInitWindowSize(size, size)  # window size
            glutInitWindowPosition(size, size)  # window position
            glutDisplayFunc(lambda: display(choice, r, xc, yc))
            init_window()
        else:
            print("\nInvalid choice !")


if __name__ == "__main__":
    main()
