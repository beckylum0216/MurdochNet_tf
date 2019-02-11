
import numpy as np

class MathUtility(object):

    def boxmuller(self):
        randomOne = 0.00
        randomTwo = 0.00
        boxResultX = 0.00
        boxResultY = 0.00

        randomOne = np.random.normal(10000)
        randomTwo = np.random.normal(10000)

        boxResultX = np.sqrt(-2 * np.log(randomOne)) * np.cos(2 * np.pi * randomTwo)
        boxResultY = np.sqrt(-2 * np.log(randomOne)) * np.sin(2 * np.pi * randomTwo)

        return boxResultX, boxResultY

    def sigmoidfunction(self, targetInput):

        tempResult = 1 / (1 + np.exp((-1 * targetInput) + 1))

        return tempResult

