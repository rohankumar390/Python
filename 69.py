class Emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharrry.com"
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property
    def printemail(self):
        if self.fname or self.lname == None:
                print("Email is not set")
        return f"{self.fname}.{self.lname}@codewithharrry.com"
    
    @printemail.setter
    def printemail(self,string):
        names=string.split("@")[0]
        fname=names.split(".") [0]
        lname=names.split(".") [1]
        
    @printemail.deleter
    def printemail(self):
          self.fname=None
          self.lname=None  
          
        
rohan =Emp("Rohan","Kumar")
print(rohan.explain())

# print(rohan.email)

# rohan.fname="US"

# print(rohan.printemail)  

# rohan.fname="US"

# print(rohan.printemail)  

rohan.printemail="this.that@codewithharry.com"

print(rohan.printemail)  

del rohan.printemail
print(rohan.printemail)  
