# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
RAD = 0
XC = 10
YC = 10
SPEED = 5


def get_inputs():
    global RAD
    RAD = float(input("Enter radius: "))


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(1024, 768)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(-720, 720, -500, 500)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-720, 0)
    glVertex2f(720, 0)
    glVertex2f(0, 500)
    glVertex2f(0, -500)
    glEnd()

    glPointSize(5.0)
    glBegin(GL_POINTS)
    for thetta in range(45):
        x = RAD * cos(radians(thetta))
        y = RAD * sin(radians(thetta))
        glColor3f(0.0, 1.0, 1.0)
        glVertex2f(x + XC, y + YC)
        glVertex2f(y + XC, x + YC)
        glVertex2f(-x + XC, y + YC)
        glVertex2f(y + XC, -x + YC)
        glVertex2f(x + XC, -y + YC)
        glVertex2f(-y + XC, x + YC)
        glVertex2f(-x + XC, -y + YC)
        glVertex2f(-y + XC, -x + YC)
    glEnd()

    glFlush()


def animator(x):
    global XC, SPEED
    XC = XC + SPEED
    if XC + RAD >= 720:
        SPEED = -SPEED
    if XC - RAD <= -720:
        SPEED = -SPEED
    glutTimerFunc(int(1000 / 60), animator, 0)
    glutPostRedisplay()


def keyboard(key, x, y):
    global SPEED
    if key == b"f":
        SPEED = 0


def main():
    get_inputs()
    init_glut()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, animator, 0)
    glutKeyboardFunc(keyboard)
    glutMainLoop()  # process events and triggers callback functions


main()
