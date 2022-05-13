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

class Programmer(Emp):
        no_of_holidays=59
        def __init__(self, aname, asalary, arole,alanguages):
             self.name = aname
             self.salary = asalary
             self.role = arole
             self.languages=alanguages
    
    
        def printprog(self):
         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

# Rohan = Emp("Rohan", 132, "Instructor")

# print(harry.salary)
# Rohan.change_leaves(99)

# print(Rohan.no_of_leaves) 
# print(Rohan.print_details())

# karan = Emp.from_dashes("karan-480-Student")

# print(karan.print_details())

# print(karan.no_of_leaves)

# print(Rohan.printgood("YO"))

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
# print(karan.no_of_holiday)
print(karan.printprog())