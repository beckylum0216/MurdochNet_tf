from OpenGL.GL import *

import ImageHeader
import LabelHeader

class Utility:

    def reversebyte(self, inputBit):
        channel0 = inputBit & 255
        channel1 = (inputBit >> 8) & 255
        channel2 = (inputBit >> 16) & 255
        channel3 = (inputBit >> 24) & 255

        return (int (channel0 << 24)) + (int (channel1 << 16)) + (int( channel2 << 8)) +(int( channel3))

    def readimageheader(self, fileName):
        imgHdr = ImageHeader.ImageHeader()
        file = open(fileName, 'rb')

        imgHdr.magicNumber = int.from_bytes(self.reversebyte(file.read(1)), byteorder='big')
        imgHdr.maxImages = int.from_bytes(file.read(1), byteorder='big')
        imgHdr.imgWidth = int.from_bytes(file.read(1), byteorder='big')
        imgHdr.imgHeight = int.from_bytes(file.read(1), byteorder='big')

        file.close()

        return imgHdr

    def readimagefile(self, fileName):

        imgHdr = ImageHeader.ImageHeader()
        imgMatrix = [[[]]]
        try:
            file = open(fileName, 'rb')

            imgHdr.magicNumber = int.from_bytes(file.read(1), byteorder='big')
            imgHdr.maxImages = int.from_bytes(file.read(1), byteorder='big')
            imgHdr.imgWidth = int.from_bytes(file.read(1), byteorder='big')
            imgHdr.imgHeight = int.from_bytes(file.read(1), byteorder='big')



            for ii in range(imgHdr.maxImages):
                for jj in range(imgHdr.imgWidth):
                    for kk in range(imgHdr.imgHeight):
                        pixel = int.from_bytes(file.read(1), byteorder='big')
                        imgMatrix[ii][jj][kk] = pixel
                        print(imgMatrix[ii][jj][kk])

            file.close()

        except IOError:
            print("Error - Could not find file")

        return imgMatrix

    def readlabelheader(self, fileName):
        lblHdr = LabelHeader.LabelHeader()

        file = open(fileName, 'rb')

        lblHdr.magicNumber = int.from_bytes(file.read(1), byteorder='big')
        lblHdr.maxLabels = int.from_bytes(file.read(1), byteorder='big')

        file.close()

        return lblHdr

    def readlabelfile(self, fileName):

        lblHdr = LabelHeader.LabelHeader()
        file = open(fileName, 'rb')

        lblHdr.magicNumber = int.from_bytes(file.read(1), byteorder='big')
        lblHdr.maxLabels = int.from_bytes(file.read(1), byteorder='big')

        lblMatrix = []

        for ii in range(lblHdr.maxLabels):
            label = int.from_bytes(file.read(1), byteorder='big')
            lblMatrix[ii] = label

        file.close()

        return lblMatrix







