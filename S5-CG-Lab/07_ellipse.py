# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sin, cos, sqrt, pi

WINDOW_SIZE = 500
PLANE_SIZE = 100


def init_glut():
    # initiate GLUT
    glutInit()
    # initiate the display mode with RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


def init_window():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # backgcolor
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


def plot_polar_ellipse(xc, yc, rx, ry):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    theta = 0
    theta_end = 2 * pi
    while theta <= theta_end:
        x = rx * (cos(theta)) + xc
        y = ry * (sin(theta)) + yc
        glVertex2f((x + xc), (y + yc))
        theta += 0.001
    glEnd()


def plot_nonpolar_ellipse(xc, yc, rx, ry):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x = -rx
    b = ry
    a = rx
    v = 1 - ((x / a) * (x / a))
    while x < 0:
        y = b * (sqrt(1 - ((x / a) * (x / a))))
        glVertex2f((x + xc), (y + yc))
        glVertex2f((-x + xc), (y + yc))
        glVertex2f((-x + xc), (-y + yc))
        glVertex2f((x + xc), (-y + yc))
        x += 0.01
    glEnd()


def display(choice, xc, yc, rx, ry):
    glClear(GL_COLOR_BUFFER_BIT)

    if choice == 1:
        plot_polar_ellipse(xc, yc, rx, ry)
    elif choice == 2:
        plot_nonpolar_ellipse(xc, yc, rx, ry)

    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    choice = 0
    while not choice == 3:
        rx = float(input("Radius along x axis: "))
        ry = float(input("Radius along y axis: "))
        xc = float(input("x-coordinate of center: "))
        yc = float(input("y-coordinate of center: "))
        print("\n1. Polar ellipse drawing Algorithm")
        print("2. Non-Polar ellipse drawing Algorithm")
        print("3. Exit")
        choice = int(input("\nSelect Algorithm: "))
        if choice in [1, 2]:
            init_glut()
            glutCreateWindow("Plot Point")  # create window
            glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
            glutDisplayFunc(lambda: display(choice, xc, yc, rx, ry))
            init_window()
        else:
            print("\nInvalid choice !")


if __name__ == "__main__":
    main()
