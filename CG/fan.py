from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

from math import sin, cos, tan, radians

WINDOW_SIZE = 600
RADIUS = 200
POINT = RADIUS / 8
ANGLE = 0
SPEED = 2


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def get_inclined_points(vertice, INCLINATION):
    return [
        round(
            vertice[0] * cos(radians(INCLINATION))
            - vertice[1] * sin(radians(INCLINATION))
        ),
        round(
            vertice[0] * sin(radians(INCLINATION))
            + vertice[1] * cos(radians(INCLINATION))
        ),
    ]


def drawWings():
    global POINT, RADIUS
    glLineWidth(3.0)
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    wing = [[0, 0], [-POINT, RADIUS], [-POINT + RADIUS / 4, RADIUS]]

    for vertices in wing:
        glVertex2fv(get_inclined_points(vertices, ANGLE))

    for vertices in wing:
        glVertex2fv(get_inclined_points(vertices, ANGLE + 120))

    for vertices in wing:
        glVertex2fv(get_inclined_points(vertices, ANGLE + 240))

    glEnd()


def update(*args):
    global ANGLE, POINT, SPEED
    glutTimerFunc(int(1000 / 60), update, 0)
    ANGLE += 1 * SPEED
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawWings()
    glFlush()


def main():
    # Init line drawing based on the user input
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)

    # Init the window size
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)

    # Init the window position on your screen
    glutInitWindowPosition(0, 0)

    # Create a window
    glutCreateWindow("Fan")
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
