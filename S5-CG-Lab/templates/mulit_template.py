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


def plot_():
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    plot_()
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    choice = 0
    while not choice == 3:
        print("_____________________________________\n")
        x = int(input(""))
        print("1. ")
        print("2. ")
        print("3. Exit")
        choice = int(input("\nSelect : "))
        if choice in [1, 2]:
            init_glut()
            glutCreateWindow("Title")  # create window
            glutInitWindowSize(size, size)  # window size
            glutInitWindowPosition(100, 100)  # window position
            glutDisplayFunc(lambda: display(x))
            init_window()
        else:
            print("\nInvalid choice !")


if __name__ == "__main__":
    main()
