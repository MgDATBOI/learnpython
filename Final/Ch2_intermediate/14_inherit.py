class Box(object):
    pass


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_method(self):
        print("I am a person")


p1 = Person("Mike", 25)
print(p1.name)
p1.person_method()


class Worker(Person):
    def __init__(self, name, age, sal):
        self.sal = sal
        super().__init__(name, age)

    def person_method(self):
        print("I am a worker")

    def yearly_sal(self):
        return self.sal * 12


w1 = Worker("Bob", 33, 5000)
w1.person_method()
print(w1.sal)
print(w1.name)


class Programmer(Worker):
    def __init__(self, name, age, sal, lang):
        self.lang = lang
        super().__init__(name, age, sal)

    def person_method(self):
        print("I am a programmer")


pr1 = Programmer("James", 20, 100000, "Python")

pr1.person_method()

print(pr1.yearly_sal())
