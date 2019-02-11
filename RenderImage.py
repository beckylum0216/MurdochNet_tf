import Pixel
import ImageHeader
from OpenGL.GL import *
from OpenGL.GLUT import *


class RenderImage(object):
    gridX = 0
    gridY = 0
    grid = [[0]]
    imgHdr = ImageHeader.ImageHeader()

    def __init__(self, inputHeader : ImageHeader.ImageHeader()):
        self.gridX = inputHeader.imgWidth
        self.gridY = inputHeader.imgHeight
        self.imgHdr = inputHeader

    def getgridx(self):
        return self.gridX

    def getgridy(self):
        return self.gridY

    def drawpixel(self, pixelcolour: float, coordX: int, coordY: int, width: float, height: float):
        #print("running draw pixel...")
        glPushMatrix()
        glBegin(GL_QUADS)
        tempRGB = pixelcolour / 255.00
        glColor3f(0.00, tempRGB, 0.0)
        glVertex(coordX / width, coordY / height, 1.0)
        glVertex(coordX / width, (coordY + 1) / height, 1.0)
        glVertex((coordX + 1) / width, (coordY + 1) / height, 1.0)
        glVertex((coordX + 1) / width, coordY / height, 1.0)
        glEnd()
        glPopMatrix()
        #print("finish running draw pixel...")

    def drawgrid(self, imgGrid, winWidth: float, winHeight: float):
        print("running drawgrid...")
        print("gridx: ", self.gridX, "gridy: ", self.gridY)
        for ii in range(self.gridX):
            for jj in range(self.gridY):
                #print("imgGrid: ", imgGrid[ii][jj])
                self.drawpixel(imgGrid[ii][jj], ii, jj, winWidth, winHeight)
        print("finished running drawgrid....")

    def renderlabel(self, posX: float, posY: float, font, text):
        glRasterPos2f(posX, posY)
        for ch in text:
            glutBitmapCharacter(font, ord(ch))




