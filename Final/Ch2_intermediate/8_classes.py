# basics -> object
class Box:
    pass


print(Box)

box = Box()
print(box)
box.value = 0
print(box.value)


class Person:
    pass


p1 = Person()
p1.name = "John"
p1.age = 25

print(p1.name, p1.age)

# __init__


class Person2:
    # def __init__(self, name):
    #     print("Person created:", name)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = Person2("Mike", 78534)

# methods


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


p3 = Person3("James", -1532)
p3.display_person()


# Overriding operations
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __list__(self):
        return [self.x, self.y]

    def __dict__(self):
        return {"x": self.x, "y": self.y}

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


v1 = Vector(1, 6)
print(v1.magnitude())

# @properity

# from ..Ch2_intermediate.EmployeeModule import Employee
import EmployeeModule

e1 = EmployeeModule.Employee("John", "Smith")
print(e1.fullname())
print(e1.email)
e1.first = "Jonathan"
print(e1.first)
print(e1.email)



# @staticmethod

# @classmethod
