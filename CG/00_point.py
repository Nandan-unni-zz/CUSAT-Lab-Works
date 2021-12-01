# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Point"
WINDOW_SIZE = 500
PLANE_SIZE = 100
X = 0
Y = 0


def get_inputs():
    global X, Y
    X = float(input("Enter x co-ordinate: "))
    Y = float(input("Enter y co-ordinate: "))


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


def plot_point():
    glColor3f(0.5, 0.0, 0.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(X, Y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_x_y_axis()
    plot_point()
    glFlush()


def main():
    get_inputs()
    init_glut()
    glutDisplayFunc(lambda: display())  # display function
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
