class Car():
    pass

honda = Car()
tata = Car()

honda.modelname = "city"
honda.yearm = 2017
honda.price = 10000

tata.modelname = "Bolt"
tata.yearm = 2018
tata.price = 60000

print(honda.price)
print(tata.price)

class Cars():
    def __init__(self,modlename,yearn,price): # this is the constructer
        self.modlename = modlename
        self.yearn = yearn
        self.price = price
    def price_inc(self):  # this is function created in the class
        self.price = int(self.price*1.15)

honda = Cars('City',2017,20000)
tata = Cars('Tata',2016,300000)
honda.cc=1500

print(honda.price)
honda.price_inc()
print(honda.price)
print(honda.__dict__) # adding dictnary object

