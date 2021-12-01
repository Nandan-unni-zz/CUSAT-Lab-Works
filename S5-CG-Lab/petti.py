from math import cos, radians, sin, tan
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
PLANE_SIZE = 100
BOTTOM_LEFT_PETTI = [0, 5]
PETTI_SPEED = 0.5
INCLINATION = 0
TYRE_RADIUS = 5


def get_inclined_points(vertice):
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


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_petti():
    glColor3f(1, 1, 0)
    glLineWidth(5.0)
    glBegin(GL_POLYGON)
    petti_vertices = [
        BOTTOM_LEFT_PETTI,
        [BOTTOM_LEFT_PETTI[0] + 25, BOTTOM_LEFT_PETTI[1]],
        [BOTTOM_LEFT_PETTI[0] + 25, BOTTOM_LEFT_PETTI[1] + 10],
        [BOTTOM_LEFT_PETTI[0], BOTTOM_LEFT_PETTI[1] + 10],
    ]
    for item in petti_vertices:
        glVertex2fv(get_inclined_points(item))
    glEnd()


def plot_road():
    glColor3f(1, 1, 1)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-PLANE_SIZE, -PLANE_SIZE * tan(radians(INCLINATION)))
    glVertex2f(PLANE_SIZE, PLANE_SIZE * tan(radians(INCLINATION)))
    glEnd()


def plot_circle():
    tyre_points = [
        [BOTTOM_LEFT_PETTI[0] + 2.5, BOTTOM_LEFT_PETTI[1]],
        [BOTTOM_LEFT_PETTI[0] + 22.5, BOTTOM_LEFT_PETTI[1]],
    ]
    for item in tyre_points:
        glBegin(GL_TRIANGLE_FAN)
        for i in range(361):
            glColor3f(0.2, 0.4, 0.8)
            glVertex2f(
                TYRE_RADIUS * cos(radians(i)) + item[0],
                TYRE_RADIUS * sin(radians(i)) + item[1],
            )
        glEnd()


def updater(x):
    global BOTTOM_LEFT_PETTI, PETTI_SPEED
    if BOTTOM_LEFT_PETTI[0] + 25 >= PLANE_SIZE:
        PETTI_SPEED = -PETTI_SPEED
    elif BOTTOM_LEFT_PETTI[0] <= -PLANE_SIZE:
        PETTI_SPEED = -PETTI_SPEED
    BOTTOM_LEFT_PETTI[0] += PETTI_SPEED
    glutTimerFunc(int(1000 / 60), updater, 0)
    glutPostRedisplay()


def controller(key, x, y):
    global PETTI_SPEED
    if key == b"s":
        PETTI_SPEED -= 0.5
    elif key == b"w":
        PETTI_SPEED += 0.5
    elif key == b" ":
        if PETTI_SPEED == 0:
            PETTI_SPEED = 1
        else:
            PETTI_SPEED = 0


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_petti()
    plot_road()
    plot_circle()
    glFlush()


def main():
    init_glut()
    glutDisplayFunc(display)  # display function
    glutTimerFunc(0, updater, 0)
    glutKeyboardFunc(controller)
    glutMainLoop()  # process events and triggers callback functions


main()
