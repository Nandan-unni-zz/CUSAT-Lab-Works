# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import pi, sin, cos

WINDOW_SIZE = 500
PLANE_SIZE = 100
SPEED = 5
BOB_CENTER_X = 0
BOB_CENTER_Y = 0
# STRING_RADIUS = 200
# BOB_RADIUS = 100
# MAX_ANGLE = 60
# ANGLE =


def init_glut():
    # initiate GLUT
    glutInit()
    # initiate the display mode with RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


def init_window():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # background color
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)  # foreground color
    glutMainLoop()  # process events and triggers callback functions


def plot_string():
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glEnd()


def plot_bob(bob_radius):
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(BOB_CENTER_X, BOB_CENTER_Y)
    for i in range(0, 360):
        glVertex2f(
            bob_radius * cos(pi * i / 180.0) + BOB_CENTER_X,
            bob_radius * sin(pi * i / 180.0) + BOB_CENTER_Y,
        )
    glEnd()


def display(bob_radius):
    glClear(GL_COLOR_BUFFER_BIT)

    plot_bob(bob_radius)

    glFlush()  # clean buffer


def main():
    string_length = 500
    bob_radius = 200
    max_angle = 60
    # string_length = float(input("Enter the length of the string of the pendulum : "))
    # bob_radius = float(input("Enter the radius of the bob of the pendulum : "))
    # max_angle = float(input("Enter the max angular displacement of pendulum : "))
    init_glut()
    glutCreateWindow("Pendulum")  # create window
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutDisplayFunc(lambda: display(bob_radius))
    init_window()


if __name__ == "__main__":
    main()
