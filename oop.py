class simpleClass:
    pass
class Animal:
    pass
class Classey:
    varia =2

    def method(self):
        print(self.varia)

object_one = Classey()
object_two = Classey()

object_one.varia =3
object_two.varia =5

# print(object_one.varia)
# print(object_two.varia)

class Transport:
    def __init__(self,air,water):
        self.air =air
        self.water = water

obj_transport =Transport("Beluga","Hovercraft")
obj2= Transport("jet","boat")
print(obj_transport.air,obj_transport.water)
print(obj2.air,obj2.water)


class Person:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname

    def printName(self):
        print(self.fname,self.lname)

# x=Person("John","Doe")
# y= Person("Mary","Doe")
# x.printName()
# y.printName()

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item_name,quantity):
        itm = {item_name,quantity}
        self.items.append(item)

    def remove_item(self,item_name,quantity):
        for item in self.items:
            if item[0]==item_name