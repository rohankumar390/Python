class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        print(
            f"Name is {self.name},Salary is {self.salary},Role is {self.role}")

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
        
    def __add__(self,other):
        return self.salary+other.salary
        
emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")

print(emp1+emp2)