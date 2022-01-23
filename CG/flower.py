# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
PLANE_SIZE = 100

BOTTOM = [0, 0]
PET_LEN = 60
PET_ANGS = [90, 90, 90, 90, 90]
PET_MAX_ANGS = [30, 60, 90, 120, 150]


def init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.1, 1.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_circle(r, xc, yc):
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        glVertex2f(r * cos(radians(i)) + xc, r * sin(radians(i)) + yc)
    glEnd()


def plot_lines(start, end):
    glLineWidth(3.0)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(start[0], start[1])
    glVertex2f(end[0], end[1])
    glEnd()


def plot_petals():
    for ang in PET_ANGS:
        xfinal = PET_LEN * cos(radians(ang)) + BOTTOM[0]
        yfinal = PET_LEN * sin(radians(ang)) + BOTTOM[1]

        plot_lines(BOTTOM, [xfinal, yfinal])
        plot_circle(10, xfinal, yfinal)


def animator(x):
    global PET_ANGS
    SPEED = 1
    for i in range(len(PET_ANGS)):
        j = abs(i - int(len(PET_ANGS) / 2))  # [0, 1, 2, 0, 1, 2]
        if i < (len(PET_ANGS) / 2):
            if PET_ANGS[i] > PET_MAX_ANGS[i]:
                PET_ANGS[i] -= SPEED * (j / 10)
        elif i > (len(PET_ANGS) / 2):
            if PET_ANGS[i] < PET_MAX_ANGS[i]:
                PET_ANGS[i] += SPEED * (j / 10)
    glutTimerFunc(50, animator, 0)
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_petals()
    glFlush()


def main():
    init()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, animator, 0)
    glutMainLoop()  # process events and triggers callback functions


main()
