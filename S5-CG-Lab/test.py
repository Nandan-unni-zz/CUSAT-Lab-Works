from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

WIND_SIZE = 500
XC = 0
YC = 0
ANGLE = 0
OFFSET = 0


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WIND_SIZE, WIND_SIZE, -WIND_SIZE, WIND_SIZE)


def drawCircle(xc, yc, r):
    theta = 0
    dtheta = 1 / r
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    while theta <= 22 / 28:
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        glVertex2f(xc + y, yc + x)
        glVertex2f(xc + y, yc - x)
        glVertex2f(xc - y, yc + x)
        glVertex2f(xc - y, yc - x)
        theta = theta + dtheta
    glEnd()


def drawOrbit(xc, yc, r):
    theta = 0
    dtheta = 1 / r
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    while theta <= 22 / 28:
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        glVertex2f(xc + y, yc + x)
        glVertex2f(xc + y, yc - x)
        glVertex2f(xc - y, yc + x)
        glVertex2f(xc - y, yc - x)

        theta = theta + dtheta
    glEnd()


def drawPlanet(xc, yc, r):
    global OFFSET
    glPointSize(3.0)
    glBegin(GL_TRIANGLE_FAN)
    I = 0.0
    while I < 360.0:
        if I < 360:
            glColor3f(0, 1, 0)
        else:
            glColor3f(0, 0, 1)
        x = r * math.cos(math.radians(I) + OFFSET)
        y = r * math.sin(math.radians(I) + OFFSET)
        glVertex2f(xc + x, yc + y)
        I += 1
    glEnd()


def display():
    global XC, YC
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(1, 100):
        drawCircle(0, 0, i)

    drawOrbit(0, 0, 400)
    for i in range(1, 50):
        drawPlanet(XC, YC, i)
    glFlush()


def update(args):
    global XC, YC, ANGLE, OFFSET
    XC = 400 * math.cos(math.radians(ANGLE))
    YC = 400 * math.sin(math.radians(ANGLE))

    ANGLE += 1
    OFFSET += 0.1
    # if ANGLE == 360:
    #     ANGLE = 0
    glutTimerFunc(100, update, 0)
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(WIND_SIZE, WIND_SIZE)
glutInitWindowPosition(0, 0)
glutCreateWindow("Solar")
glutDisplayFunc(display)
# glutKeyboardFunc(control)
glutTimerFunc(0, update, 0)
init()
glutMainLoop()
