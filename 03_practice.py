class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is a minor")


student = Student("Rudra", 18)
student.is_adult()