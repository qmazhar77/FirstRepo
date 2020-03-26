#private variable can be access only within the methos
class myClass:
    __a=10 # this is the private variable

    def disp(self):  # created method with in the class to access private variable
        print(self.__a)


obj=myClass()
obj.disp()

#print(myClass.__a) # we cannot access becoz its private class

# create private method can be access only within the class

class myClassOne:
    def __dis(self): # this is private method
        print("This is private method")

    def dipone(self): #
        self.__dis()
        print("This is public method")


obj=myClassOne()
obj.dipone()
#obj.__dis() # we are calling private method out side the class which is not correct

# we can access private variables outside of class indirectly using methods
class myClassSec:
    __empid = 101

    def getempid(self,eid):
        self.__empid=eid

    def disempid(self):
        print(self.__empid)

obj=myClassSec()
obj.getempid(105)
obj.disempid()


