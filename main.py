

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import Utility
import ImageHeader
import LabelHeader
import RenderImage

count = 0
width = 0
height =0
pixelX = 0
pixelY = 0
imgHdr = ImageHeader.ImageHeader()
lblHdr = LabelHeader.LabelHeader()
imgGrid = [[[0]]]
lblGrid = [0]

image = RenderImage.RenderImage()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    imgFile = "./mnist/train-images.idx3-ubyte"
    lblFile = "./mnist/train-labels.idx1-ubyte"

    fu = Utility.Utility()
    global imgHdr
    imgHdr = fu.readimageheader(imgFile)
    global imgGrid
    imgGrid = fu.readimagefile(imgFile)
    global lblHdr
    lblHdr = fu.readlabelheader(lblFile)
    global lblGrid
    lblGrid = fu.readlabelfile(lblFile)
    global pixelX
    pixelX = imgHdr.imgWidth
    global pixelY
    pixelY = imgHdr.imgHeight

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
    gluOrtho2D(0.0, (1.0 / width) * pixelX, 0.0, (1.0 / height) * pixelY)
    glMatrixMode(GL_MODELVIEW)


def display():
    global count
    global imgHdr
    count = count % imgHdr.maxImages
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    image.drawgrid(imgGrid[count], width, height)
    glutSwapBuffers()

    count += 1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"MurdochNet - Image Recognition")
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    #glutIdleFunc(change)
    init()
    glutMainLoop()






if __name__ == "__main__":
    main()