class Student:
    def __init__(self, name, marks):
        self.name = name          # Public variable
        self.__marks = marks      # Private variable

    # Getter Method
    def get_marks(self):
        return self.__marks

    # Setter Method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)


# Object Creation
s1 = Student("Mrunali", 85)

s1.display()

print("Marks:", s1.get_marks())

s1.set_marks(95)

print("Updated Marks:", s1.get_marks())