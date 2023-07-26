class Test:
    '''
    This is Test class
    '''

    def set_var(self, a, b):
        self.a = a
        self.b = b 

    def get_var(self, a, b):
        return self.a , self.b

    def add(self):
        return self.a + self.b
t = Test()
t.set_var(3, 4)
print(t.add())
print(t.mul())
print(t.__dict__)
print(t.__doc__) # coment
del t
print(t.a)
