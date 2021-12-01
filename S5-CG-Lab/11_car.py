# A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from playsound import playsound

from math import radians, sin, cos, pi, tan

WINDOW_TITLE = "Nandanunni's Car"
WINDOW_SIZE = 750
PLANE_SIZE = 500

INCLINATION = int(input("Enter the angle (in degree): "))
CAR_LENGTH = 200
CAR_HEIGHT = 80
CAR_TYRE_RADIUS = 22
CAR_BOTTOM_LEFT = [-PLANE_SIZE, CAR_TYRE_RADIUS]
CAR_TYRE_SPEED = -CAR_BOTTOM_LEFT[0] / 4
CAR_SPEED = 1
TO_RIGHT = True


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


def get_inclined_y(r):
    return r * sin(radians(INCLINATION))


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # window background
    gluOrtho2D(-PLANE_SIZE, PLANE_SIZE, -PLANE_SIZE, PLANE_SIZE)


def plot_car():
    global CAR_BOTTOM_LEFT

    car_body_vertices = [
        [CAR_BOTTOM_LEFT[0], CAR_BOTTOM_LEFT[1]],
        [CAR_BOTTOM_LEFT[0], CAR_BOTTOM_LEFT[1] + CAR_HEIGHT],
        [CAR_BOTTOM_LEFT[0] + (3 * CAR_LENGTH) / 5, CAR_BOTTOM_LEFT[1] + CAR_HEIGHT],
        [
            CAR_BOTTOM_LEFT[0] + (4 * CAR_LENGTH) / 5,
            CAR_BOTTOM_LEFT[1] + CAR_HEIGHT / 2,
        ],
        [CAR_BOTTOM_LEFT[0] + CAR_LENGTH, CAR_BOTTOM_LEFT[1] + CAR_HEIGHT / 2],
        [CAR_BOTTOM_LEFT[0] + CAR_LENGTH, CAR_BOTTOM_LEFT[1]],
    ]

    if not TO_RIGHT:
        car_body_vertices = [
            [CAR_BOTTOM_LEFT[0], CAR_BOTTOM_LEFT[1]],
            [CAR_BOTTOM_LEFT[0], CAR_BOTTOM_LEFT[1] + CAR_HEIGHT / 2],
            [
                CAR_BOTTOM_LEFT[0] + (1 * CAR_LENGTH) / 5,
                CAR_BOTTOM_LEFT[1] + CAR_HEIGHT / 2,
            ],
            [
                CAR_BOTTOM_LEFT[0] + (2 * CAR_LENGTH) / 5,
                CAR_BOTTOM_LEFT[1] + CAR_HEIGHT,
            ],
            [CAR_BOTTOM_LEFT[0] + CAR_LENGTH, CAR_BOTTOM_LEFT[1] + CAR_HEIGHT],
            [CAR_BOTTOM_LEFT[0] + CAR_LENGTH, CAR_BOTTOM_LEFT[1]],
        ]

    glColor3f(1.0, 1.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_POLYGON)

    for vertice in car_body_vertices:
        glVertex2fv(get_inclined_points(vertice))

    glEnd()

    car_tyre_vertices = [
        [CAR_BOTTOM_LEFT[0] + 0.2 * CAR_LENGTH, CAR_BOTTOM_LEFT[1]],
        [CAR_BOTTOM_LEFT[0] + 0.8 * CAR_LENGTH, CAR_BOTTOM_LEFT[1]],
    ]

    for tyre_vertice in car_tyre_vertices:
        glBegin(GL_TRIANGLE_FAN)
        for i in range(361):
            if i >= 0 and i <= 180:
                glColor3f(1, 1, 1)
            elif i > 180 and i <= 360:
                glColor3f(0, 0, 0)
            glVertex2f(
                CAR_TYRE_RADIUS * cos(CAR_TYRE_SPEED + pi * i / 180)
                + get_inclined_points(tyre_vertice)[0],
                CAR_TYRE_RADIUS * sin(CAR_TYRE_SPEED + pi * i / 180)
                + get_inclined_points(tyre_vertice)[1],
            )
        glEnd()


def plot_road():
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-PLANE_SIZE, -PLANE_SIZE * tan(radians(INCLINATION)))
    glVertex2f(PLANE_SIZE, PLANE_SIZE * tan(radians(INCLINATION)))
    glEnd()


def animator(*args):
    global CAR_BOTTOM_LEFT, CAR_SPEED, CAR_TYRE_SPEED, TO_RIGHT
    if CAR_BOTTOM_LEFT[0] + CAR_LENGTH >= PLANE_SIZE:
        CAR_SPEED = -1
        TO_RIGHT = False
    elif CAR_BOTTOM_LEFT[0] <= -PLANE_SIZE:
        CAR_SPEED = +1
        TO_RIGHT = True
    CAR_BOTTOM_LEFT[0] += CAR_SPEED
    CAR_TYRE_SPEED = -CAR_BOTTOM_LEFT[0] / 4
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animator, 0)


def car_controller(key, *args):
    global CAR_SPEED
    if key == b"a":
        CAR_SPEED -= 1
    elif key == b"d":
        CAR_SPEED += 1
    elif key == b"h":
        playsound("./horn.wav", block=False)
    elif key == b" ":
        if CAR_SPEED == 0:
            CAR_SPEED = 1
        else:
            CAR_SPEED = 0


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_car()
    plot_road()
    glFlush()


def main():
    init_glut()
    glutDisplayFunc(lambda: display())  # display function
    glutTimerFunc(0, animator, 0)
    glutKeyboardFunc(car_controller)
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
