# ABC is pre defined abstract class
from abc import ABC, abstractmethod
class A(ABC): # this is the abstract class
    @abstractmethod
    def display(self):
        None

class B(A): # we can not directly call abstract method we call it from child class
    def display(self):
        print("This is display method")

obj=B()
obj.display()

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("This is tiger eat Non Vage")

class Cow(Animal):
    def eat(self):
        print("Eat Veg")

t=Tiger()
t.eat()
C=Cow()
C.eat()

# Multiple abstract method
class X(ABC):

    @abstractmethod
    def M1(self):
        pass

    @abstractmethod
    def M2(self):
        pass

class Y(X):
    def M1(self):
        print("This is M1")
#    def M2(self):
#        print("This is M2")

class Z(Y):
    def M2(self):
        print("This is M2")
#y=Y()
#y.M1()
#y.M2()
z=Z()
z.M1()
z.M2()

# Create constractor in multiple abstraact class

class Cal(ABC):
    def __init__(self,value): # constractor
        self.value=value

    @abstractmethod  # abstract class
    def add(self):
        pass
    @abstractmethod # abstract class
    def sub(self):
        pass

class C(Cal):
    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-10)

cobj=C(100)
cobj.add() #200
cobj.sub() #90
