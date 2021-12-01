# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Line"
WINDOW_SIZE = 500
PLANE_SIZE = 100
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0


def get_inputs():
    global X1, Y1, X2, Y2
    choice = 0
    print("_____________________________________\n")
    print("1. Draw a horizontal line")
    print("2. Draw a vertical line")
    print("3. Draw a diagonal line")
    print("4. Exit")
    while choice not in [1, 2, 3]:
        choice = int(input("\nSelect : "))
        if choice in [1, 2, 3]:
            if choice == 1:
                X1 = int(input("Enter the initial x coordinate: "))
                X2 = int(input("Enter the final x coordinate: "))
                Y1 = int(input("Enter the y coordinate: "))
                Y2 = Y1
            elif choice == 2:
                X1 = int(input("Enter the x coordinate: "))
                X2 = X1
                Y1 = int(input("Enter the initial y coordinate: "))
                Y2 = int(input("Enter the final y coordinate: "))
            elif choice == 3:
                X1 = int(input("Enter the initial x coordinate: "))
                X2 = int(input("Enter the final x coordinate: "))
                Y1 = X1
                Y2 = X2
        else:
            print("\nEnter a valid option\n")


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


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


def plot_line():
    glColor3f(0.5, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(X1, Y1)
    glVertex2f(X2, Y2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_x_y_axis()
    plot_line()
    glFlush()


def main():
    get_inputs()
    init_glut()
    glutDisplayFunc(lambda: display())  # display function
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
