# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import pi

size = 100


def plot_point(x, y):
    glVertex2f(x / size, y / size)


def plot_triangle(x1, x2, x3, y1, y2, y3):
    glBegin(GL_LINES)
    plot_point(x1, y1)
    plot_point(x2, y2)
    glEnd()

    glBegin(GL_LINES)
    plot_point(x2, y2)
    plot_point(x3, y3)
    glEnd()

    glBegin(GL_LINES)
    plot_point(x3, y3)
    plot_point(x1, y1)
    glEnd()


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


def plot_translate(x1, x2, x3, y1, y2, y3, x_trans, y_trans):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    plot_triangle(x1, x2, x3, y1, y2, y3)
    plot_triangle(
        x1 + x_trans,
        x2 + x_trans,
        x3 + x_trans,
        y1 + y_trans,
        y2 + y_trans,
        y3 + y_trans,
    )
    glEnd()
    plot_x_y_axis()
    glFlush()  # clean buffer


def plot_rotate(x1, x2, x3, y1, y2, y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glEnd()
    plot_x_y_axis()
    glFlush()  # clean buffer


def plot_scale(x1, x2, x3, y1, y2, y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glEnd()
    plot_x_y_axis()
    glFlush()  # clean buffer


def plot_reflect(x1, x2, x3, y1, y2, y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    plot_triangle(x1, x2, x3, y1, y2, y3)
    plot_triangle(
        newpoints[0][0],
        newpoints[1][0],
        newpoints[2][0],
        newpoints[0][1],
        newpoints[1][1],
        newpoints[2][1],
    )
    glEnd()
    plot_x_y_axis()
    glFlush()  # clean buffer


def display_translate(
    x1,
    x2,
    x3,
    y1,
    y2,
    y3,
):
    x_trans = int(input("\nX translation: "))
    y_trans = int(input("Y translation: "))
    init_glut()
    glutCreateWindow("Equilateral Triangle Translation")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: plot_translate(x1, x2, x3, y1, y2, y3, x_trans, y_trans))


def display_rotate(x1, x2, x3, y1, y2, y3):
    theta = (pi / 180) * int(input("\nEnter degress to be rotated: "))
    init_glut()
    glutCreateWindow("Equilateral Triangle Roation")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display_rotate(x1, x2, x3, y1, y2, y3, theta))


def display_scale(x1, x2, x3, y1, y2, y3):
    sc_x = int(input("\nEnter Scale along x: "))
    sc_y = int(input("Enter Scale along y: "))
    init_glut()
    glutCreateWindow("Equilateral Triangle Scaling")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display_scale(x1, x2, x3, y1, y2, y3, sc_x, sc_y))


def display_reflect(x1, x2, x3, y1, y2, y3):
    init_glut()
    glutCreateWindow("Equilateral Triangle Reflection")  # create window
    glutInitWindowSize(size, size)  # window size
    glutInitWindowPosition(100, 100)  # window position
    glutDisplayFunc(lambda: display_reflect(x1, x2, x3, y1, y2, y3))


def main():
    choice = 0
    while not choice == 3:
        print("_____________________________________\n")
        print("\nEnter Triangle co-ordinates:")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        side = int(input("side: "))
        x2 = side
        y2 = y1
        x3 = x1 + side / 2
        y3 = y1 + 0.86602540378 * side
        print("\n1. Translation")
        print("2. Rotation")
        print("3. Scaling")
        print("4. Reflection")
        print("5. Exit")
        choice = int(input("\nSelect : "))
        if choice in [1, 2, 3, 4]:
            if choice == 1:
                display_translate(x1, x2, x3, y1, y2, y3)
            elif choice == 2:
                display_rotate(x1, x2, x3, y1, y2, y3)
            elif choice == 3:
                display_scale(x1, x2, x3, y1, y2, y3)
            elif choice == 4:
                display_reflect(x1, x2, x3, y1, y2, y3)
            init_window()
        else:
            print("\nInvalid choice !")


if __name__ == "__main__":
    main()
