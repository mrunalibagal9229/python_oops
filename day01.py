class Emp:
    def __init__(self,id,name ,sal):
          self.id=id
          self.name=name  
          self.sal=sal

    def getid(self):
     return self.id

    def setId (self,id):
       self.id=id

    def display(self):
     print(f"ID={self.id}\tName = {self.name} \tSalary = {self.sal}")

e1 = Emp(101,"sonali",1234589)
print (id(e1))
e1.display()
