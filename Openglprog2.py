# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
nFPS=30
RotateAngle=0.0


def init():
    glClearColor(0.1, 0.2, 0.1, 1.0) #RGBA
    gluOrtho2D(-150.0, 150.0, -150.0, 150.0)

def keyboard(key,x,y):
    if (key=='d'):#dance
        ######
        1==1
    elif (key=='l'):
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        plotpoints(GL_TRIANGLE_FAN)
    elif (key=='f'):
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
        plotpoints(GL_LINE_LOOP)
    

#def Style():
 #   if (

def plotpoints(style=GL_LINE_LOOP):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.2 ,0.2)
    #PLOT I
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND); 
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    glBegin(GL_TRIANGLE_FAN)
    #1st triangle-top left corner
    glVertex2f(-30,80)
    glVertex2f(-60,80)
    glVertex2f(-60,60)
    glVertex2f(-40,60)
    glVertex2f(-40,10)
    glVertex2f(-20,10)
    glVertex2f(-20,60)
    glVertex2f(0,60)
    glVertex2f(0,80)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,-10)
    glVertex2f(0,10)
    glVertex2f(-20,10)
    glVertex2f(-40,10)
    glVertex2f(-60,10)
    glVertex2f(-60,-10)
    glEnd()
    #PLOT L
    '''glBegin(GL_TRIANGLE_FAN)
    glVertex2f(40,10)
    glVertex2f(70,10)
    glVertex2f(70,-10)
    glVertex2f(20,-10)
    glVertex2f(20,80)
    glVertex2f(40,80)
    glEnd()'''
    glFlush()
    glutSwapBuffers() #dwap front/back framebuffer to avoid flickering


    
def reshape(width,height):
    glViewport(0,0,width,height)
    Aspect=float(width)/float(height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0,Aspect,0.001,30.0)
    
def timer(v):
    global RotateAngle
    RotateAngle+=1.0
    glutPostRedisplay()
    glutTimerFunc(1000/nFPS,timer,v)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB )
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("MP1")
    glutDisplayFunc(plotpoints) #drawing the I
    glutKeyboardFunc(keyboard)
    #glutReshapeFunc(reshape)
    glutTimerFunc(100,timer,nFPS) #timer- to update animation 
    init()
    glutMainLoop()

main()
# End of Pro
