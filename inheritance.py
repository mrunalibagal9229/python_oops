class Father:
    def money(self):
        print("Father has money")

class Mother:
    def care(self):
        print("Mother cares")

class Child(Father, Mother):
    def study(self):
        print("Child studies")

c = Child()
c.money()
c.care()
c.study()