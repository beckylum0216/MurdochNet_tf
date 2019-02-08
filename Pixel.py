class Pixel(object):
    positionX = 0
    positionY = 0
    state = False
    stateNext = False

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