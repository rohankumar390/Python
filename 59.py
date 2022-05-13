class Emp:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        print(
            f"Name is {self.name},Salary is {self.salary},Role is {self.role}")
        return 

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dashes(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("HEY GUYZ "+string)

Rohan = Emp("Rohan", 132, "Instructor")

# print(harry.salary)
Rohan.change_leaves(99)

print(Rohan.no_of_leaves)
# print(Rohan.print_details())

karan = Emp.from_dashes("karan-480-Student")

print(karan.print_details())

print(karan.no_of_leaves)

print(Rohan.printgood("YO"))