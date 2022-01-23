from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from datetime import datetime

WINDOW_TITLE = "Unni Clock"
WINDOW_SIZE = 500
PLANE_SIZE = 100

CLOCK_CENTER = [500, 350]
CLOCK_RAD = 200

SEC_LEN = CLOCK_RAD - 10
SEC_ANG = -90

MIN_LEN = CLOCK_RAD - 20
MIN_ANG = -90

HR_LEN = CLOCK_RAD - 80
HR_ANG = -90


def init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(1024, 768)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # window background
    gluOrtho2D(0, 1024, 768, 0)


def plot_clock():
    glPointSize(5.0)
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    for thetta in range(361):
        x = CLOCK_RAD * cos(radians(thetta))
        y = CLOCK_RAD * sin(radians(thetta))
        glVertex2f(x + CLOCK_CENTER[0], y + CLOCK_CENTER[1])
    glEnd()


def plot_second():
    glLineWidth(3.0)
    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    x = CLOCK_CENTER[0] + SEC_LEN * cos(radians(SEC_ANG))
    y = CLOCK_CENTER[1] + SEC_LEN * sin(radians(SEC_ANG))
    glVertex2f(x, y)
    glEnd()


def plot_minute():
    glLineWidth(5.0)
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    x = CLOCK_CENTER[0] + MIN_LEN * cos(radians(MIN_ANG))
    y = CLOCK_CENTER[1] + MIN_LEN * sin(radians(MIN_ANG))
    glVertex2f(x, y)
    glEnd()


def plot_hour():
    glLineWidth(10.0)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    x = CLOCK_CENTER[0] + HR_LEN * cos(radians(HR_ANG))
    y = CLOCK_CENTER[1] + HR_LEN * sin(radians(HR_ANG))
    glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_clock()
    plot_second()
    plot_minute()
    plot_hour()
    glFlush()


def animator(x):
    global HR_ANG, SEC_ANG, MIN_ANG
    SEC_ANG = SEC_ANG + 6
    MIN_ANG = MIN_ANG + (6 / 60)
    HR_ANG = HR_ANG + (6 / 720)
    glutTimerFunc(1000, animator, 0)
    glutPostRedisplay()


def main():
    cur_time = datetime.now()
    cur_hr = cur_time.strftime("%H")
    cur_min = cur_time.strftime("%M")
    cur_sec = cur_time.strftime("%S")
    global SEC_ANG, MIN_ANG, HR_ANG
    SEC_ANG = (int(cur_sec) * 6) - 90
    MIN_ANG = (int(cur_min) * 6) - 90
    HR_ANG = (int(cur_hr) * 30) - 90
    print(cur_hr, cur_min, cur_sec)
    init()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, animator, 0)
    glutMainLoop()  # process events and triggers callback functions


main()
