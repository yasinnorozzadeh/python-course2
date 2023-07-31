from math import pi , pow
class Circle:
    # Properties
    radius = None
    def __init__(self, r):
        self.radius = r
        
    def set_radius(self, r):
        self.radius = r

    def Area(self):
        return pow(self.radius , 2) * pi

    def Perimeter(self):
        return 2 * self.radius * pi