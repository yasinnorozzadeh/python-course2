from math import pi

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * (self.r ** 2)
    def perimeter(self):
        return 2 * pi * self.r
    
class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)

    def area(self):
        return 4 * super().area()
    def perimeter(self):
        return super().area() * self.r  * (4/3)\
        

radius = float(input("enter radius: "))
circle = Circle(radius)
sphere = Sphere(radius)
print("circle\n1_area:", circle.area(), "\n2_perimeter:", circle.perimeter())
print("sphere\n1_area:", sphere.area(), "\n2_perimeter:", sphere.perimeter())