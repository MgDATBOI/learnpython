class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"


if __name__ == "__main__":
    emp_1 = Employee("John", "Smith")
    print(emp_1.fullname())
    print(emp_1.email)
