# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos, pi, sin

WINDOW_TITLE = "Spiral"
WINDOW_SIZE = 500
PLANE_SIZE = 100
SPIRAL_RADII = [0.1]
X_CENTER = 0
Y_CENTER = 0


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_spirals():
    for radius in SPIRAL_RADII:
        glColor3f(0, 0, 1)
        glPointSize(3.0)
        glBegin(GL_POINTS)
        thetta = 0
        d_thetta = 1 / (10 * radius)
        while thetta < (pi / 4):
            x = radius * cos(thetta)
            y = radius * sin(thetta)
            glVertex2f((x + X_CENTER), (y + Y_CENTER))  # I - top
            glVertex2f((-x + X_CENTER), (-y + Y_CENTER))  # III - down
            glVertex2f((x + X_CENTER), (-y + Y_CENTER))  # IV - down
            glVertex2f((-x + X_CENTER), (y + Y_CENTER))  # II - top
            glVertex2f((y + X_CENTER), (x + Y_CENTER))  # I - down
            glVertex2f((-y + X_CENTER), (-x + Y_CENTER))  # III - top
            glVertex2f((y + X_CENTER), (-x + Y_CENTER))  # IV - top
            glVertex2f((-y + X_CENTER), (x + Y_CENTER))  # II - down
            thetta += d_thetta
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_spirals()
    glFlush()


def animator(x):
    global SPIRAL_RADII
    if len(SPIRAL_RADII) < 10:
        SPIRAL_RADII.append(SPIRAL_RADII[len(SPIRAL_RADII) - 1] + 10)
    glutTimerFunc(int(1000), animator, 0)
    glutPostRedisplay()


def main():
    init_glut()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, animator, 0)
    glutMainLoop()  # process events and triggers callback functions


main()
