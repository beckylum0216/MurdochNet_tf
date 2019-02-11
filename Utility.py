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

        imgHdr.magicNumber = int.from_bytes(file.read(4), byteorder='big')
        imgHdr.maxImages = int.from_bytes(file.read(4), byteorder='big')
        imgHdr.imgWidth = int.from_bytes(file.read(4), byteorder='big')
        imgHdr.imgHeight = int.from_bytes(file.read(4), byteorder='big')

        file.close()

        return imgHdr

    def readimagefile(self, fileName, inputHdr = ImageHeader.ImageHeader()):
        print("running imgfilereader...")
        imgHdr = ImageHeader.ImageHeader()

        imgMatrix = [[[0 for k in range(inputHdr.imgHeight)]for j in range(inputHdr.imgWidth)] for i in range(inputHdr.maxImages)]



        try:
            file = open(fileName, 'rb')

            imgHdr.magicNumber = int.from_bytes(file.read(4), byteorder='big')
            imgHdr.maxImages = int.from_bytes(file.read(4), byteorder='big')
            #print("max Images: ", imgHdr.maxImages)
            imgHdr.imgWidth = int.from_bytes(file.read(4), byteorder='big')
            #print("image width: ", imgHdr.imgWidth)
            imgHdr.imgHeight = int.from_bytes(file.read(4), byteorder='big')
            #print("Image height: ", imgHdr.imgHeight)

            for aa in range(imgHdr.maxImages):
                for bb in range(imgHdr.imgWidth):
                    for cc in range(imgHdr.imgWidth):
                        pixel = int.from_bytes(file.read(1), byteorder='big')
                        #print("pixel input: ", pixel)
                        imgMatrix[aa][bb][cc] = pixel
                        #print("imgMatrix: ", imgMatrix[aa][bb][cc])


            file.close()

        except IOError:
            print("Error - Could not find file")

        print("finish imgfilereader...")
        return imgMatrix

    def readlabelheader(self, fileName):
        print("running lblheader reader...")
        lblHdr = LabelHeader.LabelHeader()

        file = open(fileName, 'rb')

        lblHdr.magicNumber = int.from_bytes(file.read(4), byteorder='big')
        lblHdr.maxLabels = int.from_bytes(file.read(4), byteorder='big')

        file.close()
        print("finish running lblheader reader...")
        return lblHdr

    def readlabelfile(self, fileName):
        print("running read label file...")
        lblHdr = LabelHeader.LabelHeader()
        file = open(fileName, 'rb')

        lblHdr.magicNumber = int.from_bytes(file.read(4), byteorder='big')
        lblHdr.maxLabels = int.from_bytes(file.read(4), byteorder='big')

        lblMatrix = [0 for ii in range(lblHdr.maxLabels)]

        for ii in range(lblHdr.maxLabels):
            label = int.from_bytes(file.read(1), byteorder='big')
            lblMatrix[ii] = label

        file.close()
        print("finish running read label file...")

        return lblMatrix







