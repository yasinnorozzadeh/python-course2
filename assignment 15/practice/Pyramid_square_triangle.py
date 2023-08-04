class Square:
    def __init__(self, side):
        self.s = side

    def area(self):
        return (self.s ** 2)
    
    def perimeter(self):
        return 4 * self.s

class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return (2 * (self.s ** 2)) / 2
    
    def perimeter(self):
        return 3 * self.s

class Pyramid(Triangle, Square):
    def __init__(self, height, s_s, s_t):
        self.h = height
        self.s_s = s_s
        self.s_t = s_t
    def area(self):
        return Square(self.s_s).area() + (4 * (Triangle(self.s_t).area()))
    
    def side_area(self):
        return 4 * (Triangle(self.s_t).area())
    
    def volume(self):
        return (self.s_s * self.s_t * self.h) / 3
s_s = float(input("enter side of square: "))
t_s = float(input("enter side of triangle: "))
p_h = float(input("enter height of pyramid: "))
square = Square(s_s)
triangle = Triangle(t_s)
pyramid = Pyramid(p_h, s_s, t_s)
print("square=\narea:", square.area(), "\nperimeter:", square.perimeter())
print("triangle=\narea:", triangle.area(), "\nperimeter:", triangle.perimeter())
print("pyramid=\narea:", pyramid.area(), "\nvolume:", pyramid.volume(), "\nside_area:", pyramid.side_area())