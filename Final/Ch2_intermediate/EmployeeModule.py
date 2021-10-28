class Employee(object):
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f"{first}.{last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Deleted employee")
        self.first = None
        self.last = None

if __name__ == "__main__":
    emp_1 = Employee("John", "Smith")
    print(emp_1.fullname())
    print(emp_1.email)