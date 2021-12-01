# A S Nandanunni
# Reg No: 20219023
# CS - A

from math import cos, pi, radians, sin, tan
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


WINDOW_TITLE = "Rolling Ball"
WINDOW_SIZE = 500
PLANE_SIZE = WINDOW_SIZE

INCLINATION = int(input("Enter the angle of inclination (in degree): "))
BALL_RADIUS = int(input("Enter the radius of the ball: "))
BALL_CENTER = [-PLANE_SIZE + BALL_RADIUS, BALL_RADIUS]
BALL_LINEAR_SPEED = 3
BALL_RADIAL_SPEED = -BALL_CENTER[0] / 8


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_road():
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(PLANE_SIZE, PLANE_SIZE * tan(radians(INCLINATION)))
    glVertex2f(-PLANE_SIZE, -PLANE_SIZE * tan(radians(INCLINATION)))
    glEnd()


def plot_ball():
    x = BALL_CENTER[0] * cos(radians(INCLINATION)) - BALL_CENTER[1] * sin(
        radians(INCLINATION)
    )
    y = BALL_CENTER[0] * sin(radians(INCLINATION)) + BALL_CENTER[1] * cos(
        radians(INCLINATION)
    )
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        if i >= 0 and i <= 180:
            glColor3f(1, 1, 0)
        elif i > 180 and i <= 360:
            glColor3f(1, 0, 0)
        glVertex2f(
            BALL_RADIUS * cos(BALL_RADIAL_SPEED + pi * i / 180) + x,
            BALL_RADIUS * sin(BALL_RADIAL_SPEED + pi * i / 180) + y,
        )
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_road()
    plot_ball()
    glFlush()


def animator(*args):
    global BALL_CENTER, BALL_LINEAR_SPEED, BALL_RADIAL_SPEED
    if BALL_CENTER[0] + BALL_RADIUS >= PLANE_SIZE:
        BALL_LINEAR_SPEED = -1
    elif BALL_CENTER[0] - BALL_RADIUS <= -PLANE_SIZE:
        BALL_LINEAR_SPEED = +1
    BALL_CENTER[0] += BALL_LINEAR_SPEED
    BALL_RADIAL_SPEED = -BALL_CENTER[0] / 8
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animator, 0)


def main():
    init_glut()
    glutDisplayFunc(lambda: display())  # display function
    glutTimerFunc(0, animator, 0)
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
