from OpenGL.GLUT import*
from OpenGL.GLU import*
from OpenGL.GL import*
import math

control[]
def blendfunc(i,t)
    global control
    n=len(control) - 1
    t_factor1=t**i
    t_factor2=(1-t)**(n-i)
    return math.comb(n,i)*t_factor1*t_factor2

def Bezier():
    n=500
    global control

    delta=1/n
    
    for j in range(1,n)
        
