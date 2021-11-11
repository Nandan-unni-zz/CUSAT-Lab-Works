# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy

WINDOW_SIZE = 1000
GLOBAL_X_POSTION = 10
GLOBAL_Y_POSTION = 10
TARGET_FPS = 60
STATE = 1

# Pendulam Settings
pend_length = float(input("\nPendulum Length: "))
BOB_RADIUS = float(input("\nBob Radius: "))
MAX_THETA = float(input("\nMax Displacement Angle: "))
THETA = MAX_THETA
TIME_PERIOD = 2 * math.pi * (math.sqrt(pend_length / 9.8))
SPEED_MULTIPLIER = float(input("\n\tSpeed Multiplier: "))
THETA_INCREMENT = (math.cos(math.radians(THETA)) * SPEED_MULTIPLIER) - (
    math.cos(math.radians(MAX_THETA)) * (SPEED_MULTIPLIER * 0.9)
)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def update(value):
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global pend_length
    global STATE
    global WINDOW_SIZE
    global THETA
    global MAX_THETA
    global THETA_INCREMENT
    glutPostRedisplay()
    glutTimerFunc(int(1000 / TARGET_FPS), update, int(0))
    if STATE == 1:
        if THETA < MAX_THETA:
            THETA = THETA + (THETA_INCREMENT)
        else:
            STATE = -1
    elif STATE == -1:
        if THETA >= -MAX_THETA:
            THETA = THETA - (THETA_INCREMENT)

        else:
            STATE = 1
    GLOBAL_X_POSTION = pend_length * math.sin(math.radians(THETA))
    GLOBAL_Y_POSTION = -(pend_length * math.cos(math.radians(THETA)))

    THETA_INCREMENT = (math.cos(math.radians(THETA)) * SPEED_MULTIPLIER) - (
        math.cos(math.radians(MAX_THETA)) * (SPEED_MULTIPLIER * 0.9)
    )


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POLYGON)
    glVertex2f(GLOBAL_X_POSTION, GLOBAL_Y_POSTION)
    glVertex2f(GLOBAL_X_POSTION + 200, GLOBAL_Y_POSTION)
    glVertex2f(GLOBAL_X_POSTION + 200, GLOBAL_Y_POSTION + 200)
    glVertex2f(GLOBAL_X_POSTION, GLOBAL_Y_POSTION + 200)
    glEnd()
    glutSwapBuffers()


def drawCircle(x, y):
    i = 0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in numpy.arange(0, 360.0, 1.0):
        glVertex2f(
            BOB_RADIUS * math.cos(math.pi * i / 180.0) + x,
            BOB_RADIUS * math.sin(math.pi * i / 180.0) + y,
        )
    glEnd()


def drawPendulam():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(GLOBAL_X_POSTION, GLOBAL_Y_POSTION)
    glEnd()
    drawCircle(GLOBAL_X_POSTION, GLOBAL_Y_POSTION)
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Pendulum ")
    glutDisplayFunc(drawPendulam)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(drawPendulam)

    init()
    glutMainLoop()


main()
