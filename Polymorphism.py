# overriding a variable

class praent:
    name="Azhar"

class Child(praent):
    pass
    #name=("Davide")
obj=Child()
print(obj.name) # David

class Bank:
    def rateofint(self):
        return 0
class ICICI(Bank):
    def rateofint(self):
        return 10.5
obj=ICICI()
print(obj.rateofint())
obj1=Bank()
print(obj1.rateofint())


# Overlodding Methods

class Human:
    def seyHello(self,name=None):
        if name is not None:
            print("Hello : "+ name)
        else:
            print("Hello")

obj=Human()
obj.seyHello("Muzzammil")
obj.seyHello()


class Bird:
    def fly(self,name=None):
        if name=="Parrot":
            print("Can fly")
        if name=="Penguin":
            print("Cannot fly")
        if name is None:
            print("No input")

obj=Bird()
obj.fly("Penguin")

