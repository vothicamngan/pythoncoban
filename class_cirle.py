import math
class Cirle:
    radius = 0 
    color = ""
    def __init__(self,radius,color ):
        self.radius = radius
        self.color = color
    def getRadius(self):
        return f"{self.radius}"
    def getArea(self):
        s = math.pi*self.radius* self.radius
        return s
cirle = Cirle (50,"red")
print(Cirle.getArea)