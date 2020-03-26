class Cars():  # Parent calss
    def __init__(self,modlename,yearn,price): # this is the constructer
        self.modlename = modlename
        self.yearn = yearn
        self.price = price
    def price_inc(self):  # this is function created in the class
        self.price = int(self.price*1.15)

class SuperCar(Cars):  # This is the child class drive from parent class
    pass
honda = Cars('City',2017,20000)
tata = Cars('Bolt',2016,300000)
honda.cc=1500

print(honda.price)
#print(help(honda))
honda.price_inc()
print(honda.price)


class Car():  # Parent calss
    def __init__(self,modlename,yearn,price): # this is the constructer
        self.modlename = modlename
        self.yearn = yearn
        self.price = price
    def price_inc(self):  # this is function created in the class
        self.price = int(self.price*1.15)

class SuperCar(Car):  # This is the child class drive from parent class
    def __init__(self,modlename,yearn,price,cc):
        super.__init__(modlename,yearn,price)
        self.cc=cc # adding the parameter in existing class
honda = Car('Civic',2018,22000)
tata = Car('Indica',2017,600000)
honda.cc=1500

print(honda.price)
print(honda.__dict__)