2  # A S Nandanunni
# Reg No: 20219023
# CS - A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = "Template"
WINDOW_SIZE = 500
PLANE_SIZE = 100
X = 0
Y = 300
X2 = 768
Y2 = 300
speed = 1
oldspeed = 1


def get_inputs():
    global X
    X = float(input("Enter X: "))


def drawLine():
    global X, Y, X2, Y2
    glLineWidth(10.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(X, Y)
    glVertex2f(X2, Y2)
    glEnd()


def animate(z):
    global X, Y, X2, Y2, speed
    glutTimerFunc(int(1000 / 60), animate, 0)
    Y += speed
    Y2 += speed
    if Y >= 768:
        speed = -1
    if Y <= 0:
        speed = 1
    glutPostRedisplay()


def control(key, x, y):
    global speed, oldspeed
    if key == b"s":
        oldspeed = speed
        speed = 0
    if key == b"d":
        speed = oldspeed


def init_glut():
    print(f"\nOpening {WINDOW_TITLE}...")  # Opening message
    glutInitDisplayMode(GLUT_RGB)
    glutInit()  # Initiating glut
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)  # window size
    glutCreateWindow(WINDOW_TITLE)  # window title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # window background
    gluOrtho2D(0, 1024, 768, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    glFlush()


def main():
    # get_inputs()
    init_glut()
    glutDisplayFunc(display)  # display function
    glutKeyboardFunc(control)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()  # process events and triggers callback functions


if __name__ == "__main__":
    main()
