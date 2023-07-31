class Person:
    def __init__(self, n):
        self.name = n

    def show_name(self):
        print(self.name)

class Employee(Person):
    def __init__(self, n, s):
        super().__init__(n)
        self.salary = s

    def welcome(self):
        print("welcome " + self.name)

ob = Employee("yasin", 3)
ob.welcome()
ob.show_name()
