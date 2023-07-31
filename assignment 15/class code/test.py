class  Test:
    def __init__(self,a , b):
        self.a = a
        self.__b = b

t = Test(1, 1)
print(t.a)

#####################
# name mangling
