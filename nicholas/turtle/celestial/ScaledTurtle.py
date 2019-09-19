from turtle import Turtle, TNavigator, Vec2D

# A ScaledTurtle accepts distances and coordinates in real-world units such as feet, inches, or meters.
class ScaledTurtle(Turtle):

    # Number of pixels per real-world unit.
    _scaleFactor = 1.0

    # Returns the number of pixels per real-world unit.
    def pixelsPerUnit(self):
        return self._scaleFactor

    # Returns the number of real-world units per pixel.
    def unitsPerPixel(self):
        return 1 / self._scaleFactor
    
    # Sets the number of pixels per real-world unit.
    def setPixelsPerUnit(self, pixelsPerUnit):
        self._scaleFactor = pixelsPerUnit

    # Sets the number of real-world units per pixel.
    def setUnitsPerPixel(self, unitsPerPixel):
        self._scaleFactor = 1 / unitsPerPixel

    def pos(self):
        return super().pos() * self.unitsPerPixel()

    def xcor(self):
        return super().xcor() * self.unitsPerPixel()

    def ycor(self):
        return super().ycor() * self.unitsPerPixel()

    def setx(self, x):
        super().setx(x * self.pixelsPerUnit())

    def sety(self, y):
        super().setx(y * self.pixelsPerUnit())

    def goto(self, x, y=None):
        if y is not None:
            super().goto(x * self.pixelsPerUnit(), y * self.pixelsPerUnit())
        elif isinstance(x, Vec2D):
            super().goto(x * self.pixelsPerUnit())
        else:
            super().goto(x[0] * self.pixelsPerUnit(), x[1] * self.pixelsPerUnit())

    def forward(self, distance):
        super().forward(distance * self.pixelsPerUnit())
    
    def back(self, distance):
        super().back(distance * self.pixelsPerUnit())

    def distance(self, x, y=None):
        if y is not None:
            distanceInPixels = super().distance(x * self.pixelsPerUnit(), y * self.pixelsPerUnit())
        elif isinstance(x, TNavigator):
            distanceInPixels = super().distance(x)
        elif isinstance(x, Vec2D):
            distanceInPixels = super().distance(x * self.pixelsPerUnit())
        else:
            distanceInPixels = super().distance(x[0] * self.pixelsPerUnit(), x[1] * self.pixelsPerUnit())

        return distanceInPixels * self.unitsPerPixel()
    
    fd = forward
    bk = back
    backward = back
    position = pos
    setpos = goto
    setposition = goto