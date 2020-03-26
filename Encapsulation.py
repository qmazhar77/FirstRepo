for abs import ABC, abstractmethod #crated abstract calss

class Car(ABC):  # abstract class
    @abstractmethod
    def price_inc(self):  # this is function created andd just pass it
        pass

class SuperCar(Car):  # This is the child class drive from parent class
    def __init__(self,modlename,yearn,price,cc):
        super.__init__(modlename,yearn,price)
        self.cc=cc # adding the parameter in existing class
    def price_inc(self):  # this is function created in the class
        self.price = int(self.price*2)

honda = Car('Civic',2018,22000)
tata = Car('Indica',2017,600000)
honda.cc=1500

print(honda.price)
print(honda.__dict__)