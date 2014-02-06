# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
def init():
    glClearColor(0.1, 0.2, 0.1, 1.0) #RGBA
    gluOrtho2D(-150.0, 150.0, -150.0, 150.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.2 ,0.2)
    #PLOT I
    glBegin(GL_TRIANGLE_FAN)
    #glEnable(GL_BLEND)
    #glBlendFunc(0.8,0.2)
    #1st triangle-top left corner
    glVertex2f(-40,60) #vertex 3
    glVertex2f(-60,60) #vertex 2
    glVertex2f(-60,80) #vertex 1
    glColor3f(1.0,0.0,0.4)
    glVertex2f(0,80)   #verte
    glVertex2f(-20,60)
    glVertex2f(-20,10)
    glVertex2f(-40,10)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,1.2,0.2)
    glVertex2f(0,-10)
    glVertex2f(0,10)
    glVertex2f(-20,10)
    glColor3f(1.0,0.0,0.4)
    glVertex2f(-40,10)
    glVertex2f(-60,10)
    glVertex2f(-60,-10)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(-20,60)
    glVertex2f(0,80)
    glVertex2f(0,60)
    glEnd()

    #PLOT L
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(40,10)
    glVertex2f(70,10)
    glVertex2f(70,-10)
    glVertex2f(20,-10)
    glVertex2f(20,80)
    glVertex2f(40,80)
    glEnd()
    
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()
# End of Pro
