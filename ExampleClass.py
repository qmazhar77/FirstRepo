# Types of Inheritance
# 1) Single Inheritance
# 2) Multiple Inheritance
# 3) Multilevel Inheritance
# 4) Hierarchical Inheritance
# 5) Hyprid Inheritance

# Single Inheritance Example
# when the inheritance involves one child class and one parent class
class Parent:
    def func1(self):
        print("This is a parent class")

class Childone(Parent):
    def func2(self):
        print("This is a child class")

ob = Childone()
ob.func1()
ob.func2()


class Parent1:
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name,self.age)

class Childtow(Parent1):
        def __init__(self,fname,fage):
            Parent1.__init__(self,fname,fage)
            self.lastname = "edureka"

        def view(self):
            print (self.lastname,self.name,self.age)

ob = Childtow('Python',23)
ob.view()

# Multiple Inheritance Example
# It involves more then one parent class
class Parent1:
    def finc1(self):
        print("This is a first MP parent class")

class Parent2:
    def func3(self):
        print("This is a second MP parent class")

class Child1(Parent1,Parent2):
    def func2(self):
        print("This is a MP child class")

ob = Child1()
ob.finc1()
ob.func3()

# Multilevel Inheritance Example
# The child class acts as parent class of another child class
class MParent1:
    def Mfinc1(self):
        print("This is a first ML parent class")

class MParent2(MParent1):
    def Mfunc3(self):
        print("This is a second ML parent class")

class MChild1(MParent2):
    def Mfunc2(self):
        print("This is a ML child class")

ob = MChild1()
ob.Mfinc1()
ob.Mfunc3()

# Herarchical Inheritance Example
# More then one type of inheritance
class HParent1:
    def Hfinc1(self):
        print("This is a first H parent class")

class HParent2(HParent1):
    def Hfunc3(self):
        print("This is a second H parent class")

class HChild1(HParent1):
    def Hfunc2(self):
        print("This is a H child class")

ob = HChild1()
ob.Hfinc1()
ob.Hfunc2()
ob = HParent2()
ob.Hfunc3()

# Supper Function

class superP:
    def sf1(self):
        print ("This is supper 1")

class supperC:
    def sf2(self):
        superP().sf1()
        print ("This is supper 2")

ob = supperC()
ob.sf2()

# Method overriding

class MethodoverriddingParent:
    def f1(self):
        print ("This is method over riding 1")

class MethodoverriddingChild:
    def f1(self):
        print ("This is method over riding 2")

ob = MethodoverriddingChild()
ob.f1()