# A S Nandanunni
# Reg No: 20219023
# CS - A

from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
PLANE_SIZE = 100
X = 0
RAD = 10
CAR_POINT = [0, 2 * RAD]
LEN = 50
SPEED = 0.1


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_box():
    glLineWidth(5.0)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(CAR_POINT[0], CAR_POINT[1])
    glVertex2f(CAR_POINT[0], CAR_POINT[1] + 30)
    glVertex2f(CAR_POINT[0] + LEN, CAR_POINT[1] + 30)
    glVertex2f(CAR_POINT[0] + LEN, CAR_POINT[1])
    glEnd()


def plot_tyre():
    tyre_vertices = [
        [CAR_POINT[0] + (LEN * 0.25), RAD],
        [CAR_POINT[0] + (LEN * 0.75), RAD],
    ]
    for ver in tyre_vertices:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0, 1.0, 1.0)
        for i in range(361):
            glVertex2f(RAD * cos(i) + ver[0], RAD * sin(i) + ver[1])
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_box()
    plot_tyre()
    glFlush()


def animator(x):
    global CAR_POINT, SPEED
    if CAR_POINT[0] + LEN >= PLANE_SIZE:
        SPEED = -SPEED
    if CAR_POINT[0] < -PLANE_SIZE:
        SPEED = -SPEED
    CAR_POINT[0] = CAR_POINT[0] + SPEED
    glutTimerFunc(int(1000 / 60), animator, 0)
    glutPostRedisplay()


def controls(key, x, y):
    global SPEED
    if key == b"d":
        SPEED = SPEED + 0.2


def main():
    init_glut()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, animator, 0)
    glutKeyboardFunc(controls)
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
