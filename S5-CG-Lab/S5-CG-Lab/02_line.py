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


def plot_line():
    print("\n1. Draw a horizontal line")
    print("2. Draw a vertical line")
    print("3. Draw a diagonal line\n")
    ch = int(input("Select line: "))

    x1, x2, y1, y2 = 0, 0, 0, 0
    if ch == 1:
        x1 = int(input("Enter the initial x coordinate: "))
        x2 = int(input("Enter the final x coordinate: "))
        y1 = int(input("Enter the y coordinate: "))
        y2 = y1
    elif ch == 2:
        x1 = int(input("Enter the initial x coordinate: "))
        x2 = x1
        y1 = int(input("Enter the y coordinate: "))
        y2 = int(input("Enter the final y coordinate: "))
    elif ch == 3:
        x1 = int(input("Enter the initial x coordinate: "))
        x2 = int(input("Enter the final x coordinate: "))
        y1 = x1
        y2 = x2
    else:
        print("Invalid choice")

    glPointSize(10.0)  # point size

    # creating x-axis & y-axis
    glColor3f(0.0, 0.0, 0.0)  # x-axis & y-axis color
    glBegin(GL_LINES)
    # y-axis
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    # x-axis
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()

    # plotting line
    x1, x2, y1, y2 = x1 / 100, x2 / 100, y1 / 100, y2 / 100
    glColor3f(0.2, 0.8, 0.2)  # line color
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    plot_line()

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
