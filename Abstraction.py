from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Child Class
class Car(Vehicle):

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


# Object Creation
c = Car()
c.start()
c.stop()