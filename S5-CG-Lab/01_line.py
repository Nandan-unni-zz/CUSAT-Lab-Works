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


def plot_line(x1, y1, x2, y2):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    plot_point(x1, y1)
    plot_point(x2, y2)
    glEnd()


def display(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_line(x1, y1, x2, y2)
    plot_x_y_axis()

    glFlush()  # clean buffer


def main():
    choice = 0
    while not choice == 4:
        print("_____________________________________\n")
        print("1. Draw a horizontal line")
        print("2. Draw a vertical line")
        print("3. Draw a diagonal line")
        print("4. Exit")
        choice = int(input("\nSelect : "))
        if choice in [1, 2, 3]:
            if choice == 1:
                x1 = int(input("Enter the initial x coordinate: "))
                x2 = int(input("Enter the final x coordinate: "))
                y1 = int(input("Enter the y coordinate: "))
                y2 = y1
            elif choice == 2:
                x1 = int(input("Enter the x coordinate: "))
                x2 = x1
                y1 = int(input("Enter the initial y coordinate: "))
                y2 = int(input("Enter the final y coordinate: "))
            elif choice == 3:
                x1 = int(input("Enter the initial x coordinate: "))
                x2 = int(input("Enter the final x coordinate: "))
                y1 = x1
                y2 = x2
            init_glut()
            glutCreateWindow("Plot Point")  # create window
            glutInitWindowSize(size, size)  # window size
            glutInitWindowPosition(100, 100)  # window position
            glutDisplayFunc(lambda: display(x1, y1, x2, y2))
            init_window()
        else:
            print("\nInvalid choice !")


if __name__ == "__main__":
    main()
