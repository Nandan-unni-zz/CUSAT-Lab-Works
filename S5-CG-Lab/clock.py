# A S Nandanunni
# Reg No: 20219023
# CS - A
from math import cos, pi, radians, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
PLANE_SIZE = 100

CLOCK_CENTER = [0, 0]
CLOCK_RADIUS = 50

SECOND_END = [0, CLOCK_RADIUS]
MINUTE_END = [0, CLOCK_RADIUS * 0.75]
HOUR_END = [0, CLOCK_RADIUS * 0.5]

SECOND_ANG = 90
MINUTE_ANG = 0
HOUR_ANG = 0


def get_inclined_points(vertice, angle):
    return [
        round(vertice[0] * cos(radians(angle)) - vertice[1] * sin(radians(angle))),
        round(vertice[0] * sin(radians(angle)) + vertice[1] * cos(radians(angle))),
    ]


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_circle():
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        glColor3f(0.2, 0.4, 0.8)
        glVertex2f(
            CLOCK_RADIUS * cos(radians(i)) + CLOCK_CENTER[0],
            CLOCK_RADIUS * sin(radians(i)) + CLOCK_CENTER[1],
        )
    glEnd()


def second_hand():
    glColor3f(1, 1, 0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    glVertex2f(SECOND_END[0], SECOND_END[1])
    glEnd()


def minute_hand():
    glColor3f(1, 0, 1)
    glLineWidth(7.5)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    glVertex2f(
        get_inclined_points([MINUTE_END[0], MINUTE_END[1]], MINUTE_ANG)[0],
        get_inclined_points([MINUTE_END[0], MINUTE_END[1]], MINUTE_ANG)[1],
    )
    glEnd()


def hour_hand():
    glColor3f(0, 1, 1)
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(CLOCK_CENTER[0], CLOCK_CENTER[1])
    glVertex2f(HOUR_END[0], HOUR_END[1])
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_circle()
    second_hand()
    minute_hand()
    hour_hand()
    glFlush()


def main():
    init_glut()
    glutDisplayFunc(display)  # display function
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
