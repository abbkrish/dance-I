# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos
import sys
nFPS=30
RotateAngle=0.0
time=0
paused=0

def init():
    glClearColor(0.1, 0.2, 0.1, 1.0) #RGBA
    gluOrtho2D(-150.0, 150.0, -150.0, 150.0)

def keyboard(key,x,y):
    global time, paused
    if (key=='d'):#dance
        time=0
    elif (key=='p'):#pause
        paused=1
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
    a=1.2*sin(time-6.5)
    b=1.2*sin(time-5.5)
    c=1.2*cos(time-6.5)
    d=1.2*cos(time-6.5)
    #PLOT I
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND); 
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    glBegin(GL_TRIANGLE_FAN)
    #1st triangle-top left corner
    glVertex2f(-30+cos(c),80+sin(a))
    glVertex2f(-60+cos(d),80+sin(a))
    glVertex2f(-60+cos(d),60+sin(b))
    glColor3f(1.0,0.0,0.4)
    glVertex2f(-40+cos(d),60+sin(b))
    glVertex2f(-40+cos(d),10+sin(a))
    glVertex2f(-20+cos(c),10+sin(b))
    glVertex2f(-20+cos(c),60+sin(b))
    glVertex2f(0+cos(d),60+sin(b))
    glVertex2f(0+cos(d),80+sin(a))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,1.2,0.2)
    glVertex2f(0+cos(d),-10+sin(b))
    glVertex2f(0+cos(d),10+sin(b))
    glVertex2f(-20+cos(c),10+sin(b))
    glColor3f(1.0,0.0,0.4)
    glVertex2f(-40+cos(d),10+sin(a))
    glVertex2f(-60+cos(d),10+sin(a))
    glVertex2f(-60+cos(d),-10+sin(a))
    glEnd()
    #PLOT L
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,1.2,0.2)
    glVertex2f(40+cos(d),10+sin(b))
    glVertex2f(70+cos(c),10+sin(b))
    glVertex2f(70+cos(c),-10+sin(a))
    glColor3f(1.0,0.0,0.4)
    glVertex2f(20+cos(d),-10+sin(a))
    glVertex2f(20+cos(d),80+sin(b))
    glVertex2f(40+cos(d),80+sin(b))
    glEnd()
    glutSwapBuffers() #dwap front/back framebuffer to avoid flickering


    
def reshape(width,height):
    glViewport(0,0,width,height)
    Aspect=float(width)/float(height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0,Aspect,0.001,30.0)
    
def timer(v):
    global RotateAngle, time, paused
    if (not(paused)):
              time+=0.2
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
    glutTimerFunc(17,timer,nFPS) #timer- to update animation 
    init()
    glutMainLoop()

main()
# End of Pro
