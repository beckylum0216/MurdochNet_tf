import  tensorflow as tf
import numpy as np
import ImageHeader
import MathUtility

class NeuralNet(object):
    neuralInput = np.empty(1)
    neuralSize = 1
    imgHdr = ImageHeader.ImageHeader()

    def __init__(self, imageHdr = ImageHeader.ImageHeader(), neuralCount = 0):
        self.imgHdr = imageHdr
        self.neuralSize = neuralCount
        self.neuralInput = np.empty(shape = (self.imgHdr.imgWidth, self.imgHdr.imgHeight), dtype = np.object)

    def initXavier(self):
        inputSize = self.imgHdr.imgWidth * self.imgHdr.imgHeight
        popSize = (inputSize + self.neuralSize) / 2
        mt = MathUtility.MathUtility()

        constXavier = 1/popSize
        xavierResult = mt.boxmuller() * constXavier

        return xavierResult

    def setNeuralInput(self, imgInput):
        for ii in range(self.imgHdr.imgWidth):
            for jj in range(self.imgHdr.imgHeight):
                self.neuralInput[ii][jj] = imgInput[ii][jj]


