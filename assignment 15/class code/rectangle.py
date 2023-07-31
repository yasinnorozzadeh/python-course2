class Rectangle():
    def __init__(self, t, a):
        self.t = t
        self.a = a
    def S(self):
        return self.a * self.t

    def P(self):
        return (self.t + self.a) * 2
    
class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)

rec = Rectangle(5, 2)
print(rec.S(), rec.P())
sq = Square(5)
print(sq.S(), sq.P())