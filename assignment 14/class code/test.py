class Person:
    # constructor
    def __init__(self, n, a):
        # properties
        self.name = n
        self.age = a
    # methods
    def show_info(self):
        print(f"my name is {self.name} I am {self.age}")

name = input("your name: ")
age = int(input("your age: "))
person = Person(name, age)
person.show_info()


# isinstance
# donders
