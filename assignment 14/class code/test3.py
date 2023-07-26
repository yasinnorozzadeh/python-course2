class Student():
    def __init__(self, name, score=None):
        self.d = {}
        self.d["name"] = name
        self.d["score"] = score
    def get_student(self):
        return self.d
student_list = []
l = Student("liana", 18.5)
a = Student("Arman")

student_list.append(l.get_student())
student_list.append(a.get_student())
print(student_list)