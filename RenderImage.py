import Pixel
import ImageHeader
from OpenGL.GL import *

class RenderImage(object):
    gridX = 0
    gridY =0
    grid = [[Pixel.Pixel()]]

    def __init__(self, inputHeader = ImageHeader.ImageHeader()):
        gridX = inputHeader.imgWidth
        gridY = inputHeader.imgWidth

    def getgridx(self):
        return self.gridX

    def getgridy(self):
        return self.gridY

    def drawpixel(self, pixelcolour = 0.00, coordX = 0, coordY = 0, width = 0.00, height = 0.00):
        glPushMatrix()
        glBegin(GL_QUADS)
        tempRGB = pixelcolour / 255.00
        glColor3f(pixelcolour, 0, 0)
        glVertex(coordX / width, coordY / height, 1.0)
        glVertex(coordX / width, (coordY + 1) / height, 1.0)
        glVertex((coordX + 1) / width, (coordY + 1) / height, 1.0)
        glVertex((coordX + 1) / width, coordY / height, 1.0)
        glEnd()
        glPopMatrix()

    def drawgrid(self, imgGrid = [[0]], winWidth = 0.00, winHeight = 0.00):
        for ii in range(self.gridX):
            for jj in range(self.gridY):
                glDrawPixels(imgGrid[ii][jj], ii, jj, winWidth, winHeight)


