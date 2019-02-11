class Pixel(object):
    positionX = 0
    positionY = 0
    state = 0.00
    stateNext = 0.00

    def setpositionx(self, inputX):
        self.positionX = inputX

    def getpositionx(self):
        return self.positionX

    def  setpositiony(self, inputY):
        self.positionY = inputY

    def getpositiony(self):
        return self.positionY

    def setstate(self, inputState):
        self.state = inputState

    def getstate(self):
        return self.state

    def setstatenext(self, inputStateNext):
        self.stateNext = inputStateNext

    def getstatenext(self):
        return  self.stateNext