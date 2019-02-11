

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_10

import sys
import Utility
import ImageHeader
import LabelHeader
import RenderImage


count = 0
width = 0
height = 0
pixelX = 0
pixelY = 0
imgHdr = ImageHeader.ImageHeader()
lblHdr = LabelHeader.LabelHeader()
imgGrid = [[[]]]
lblGrid = []
font = GLUT_BITMAP_HELVETICA_10

def init():
    print("running init...")
    glClearColor(0.0, 1.0, 0.0, 0.0)

    imgFile = "./mnist/train-images.idx3-ubyte"
    lblFile = "./mnist/train-labels.idx1-ubyte"

    fu = Utility.Utility()
    global imgHdr
    imgHdr = fu.readimageheader(imgFile)
    global imgGrid
    imgGrid = [[[0 for kk in range(imgHdr.imgHeight)] for jj in range(imgHdr.imgWidth)]for ii in range(imgHdr.maxImages)]
    imgGrid = fu.readimagefile(imgFile, imgHdr)

    global lblHdr
    lblHdr = fu.readlabelheader(lblFile)
    global lblGrid
    lblGrid = fu.readlabelfile(lblFile)
    global pixelX
    pixelX = imgHdr.imgWidth
    global pixelY
    pixelY = imgHdr.imgHeight

    global image
    image = RenderImage.RenderImage(imgHdr)

    print("finish running init...")


def reshape(w, h):
    global width
    width = w
    global height
    height = h
    glViewport(0, 0, w, h)
    if h == 0:
        h = 1

    ratio = float(w/h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, pixelX/width, 0.0, pixelY / height)
    glMatrixMode(GL_MODELVIEW)


def display():
    global count
    print("display count: ", count)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    image.drawgrid(imgGrid[count], width, height)
    imgLbl = "Label: " + str(lblGrid[count])
    image.renderlabel(0, 28, font, imgLbl)
    print("label: ", lblGrid[count])

    glutSwapBuffers()

def animate():
    print("running animate...")
    global count
    count += 1
    print("change count:", count)
    image.drawgrid(imgGrid[count], width, height)
    imgLbl = "Label: " + str(lblGrid[count])
    image.renderlabel(0, 25, font, imgLbl)
    glutPostRedisplay()
    print("finish running animate...")

def change(self, value):
    print("blah")
    global count
    count += 1
    print("change count:", count)
    image.drawgrid(imgGrid[count], width, height)
    imgLbl = "Label: " + str(lblGrid[count])
    image.renderlabel(0, 25, font, imgLbl)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"MurdochNet - Image Recognition")
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(animate)
    #glutTimerFunc(50, change, 0)
    init()
    glutMainLoop()






if __name__ == "__main__":
    main()