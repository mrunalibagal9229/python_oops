class BusDriver:
    busname = 'PMPML'

    def __init__(self, deponame, drivername, busno):
        self.deponame = deponame
        self.drivername = drivername
        self.__busno = busno

    def show(self):
        print(f"Depo Name: {self.deponame}\nDriver Name: {self.drivername}\nBus No: {self.__busno}")


b = BusDriver("Pune", "Mrunali Bagal", "MH9229")
b.show()


'''
A default constructor in Python is a constructor that does not take any parameters except self. 
It initializes an object with default values.

Default Constructor ->

class BusDriver:
    def __init__(self):
        self.deponame = "Pune"
        self.drivername = "Mrunali Bagal"
        self.busno = "MH9229"

    def show(self):
        print("Depo Name:", self.deponame)
        print("Driver Name:", self.drivername)
        print("Bus No:", self.busno)

b = BusDriver()   # No arguments required
b.show()





type ->
        Default Constructor –> Takes only self and initializes default values.

        Parameterized Constructor –> Takes self and additional parameters to 
        initialize the object with user-provided values.




The __str__() method in Python is a special method that defines the 
string representation of an object. It is automatically called when you use print(object) or str(object).
'''


class busDeiver:
    def __init__(self, nm, sal, bno):
        self.nm
        


'''

setter -> 

each thing happen in program called behaviour

setter and getter are behaviuos



desctuctor -> 





type of mehtod

class level  -> static level - by using class name



self keyword use then need object
 not static or intance



 depende on onject called instance


 instance -> 


 @static
static ->  chnage the state of object then use static method 
deponame - static variable 




desturctor is used to destroy the object mean free the memory 
or unused method , variable 
garbeg collectio
automatic memory manager
automatically call at the end of the program

'''