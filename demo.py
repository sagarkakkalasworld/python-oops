#class
#class is like a blue print of what it consists of, for example, car has chasis, enginer, you can think of it more like its specifications 
class car:
    pass

#pass simply means i created a class but i dont want to put anything here
car1 = car()

#here car1 becomes object
print(type(car1))

##__init_constructor()__

class car:
    def __init__(self, brand, model): #init constructor
        self.brand = brand ##attributes
        self.model = model

## self is putting current object car1 into car class = car("Tesla", "cybertruck") changes to car1 = car(car1.brand, car1.model)
car1 = car("Tesla", "cybertruck")

# also when you run the function python calls init function, more like initialize function
car2 = car("tata", "punch")

print(car1.model)
print(car2.brand)

##create attributes outside class
car2.engine = "4 stroke engine"
print(car2.engine)

##Function, methods inside class

class car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")

car3 = car("tesla","roadster")
car3.drive()

#Class
#|
# ├── Attributes → data
# |
# └── Methods    → behavior

##instance variable - each object has its own variable
# In our above examples, car3.model = roadster, car1.model = cybertruck.. these are instance variables

#Class Variables - these are defined in class
#Global variables - these are defined outside clas

class car:
    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model

    def drive(self):
        print(self.brand, "is driving")

# in above example , sagar kakkala becomes owner for any object called

car4=car("ferrari","sf90")
print(car4.owner)


##instance method

class car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.model, "is Amazing") ## instance method

car3 = car("tesla","roadster")
car3.drive()

##static method - @staticmethod does not require class or self

class car:

    @staticmethod
    def write(a,b):
        print(f"{a} has model named {b}")

car3=car()
car.write("tesla","roadster")

##class mehtod - used for fucntions in class

  
class car:
    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model

    @classmethod
    def get_owner(cls):
        print(cls.owner, "is the owner")

    def drive(self):
        print(self.brand, "is driving")

car7=car("sagar","car2")
car7.get_owner() 

##Encapsulation -- making attributes difficult to access
class car:
    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.__engine = "4 stroke engine" #before self.engine = "4 stroke engine"
        self.brand = brand #instance variable
        self.model = model

    @classmethod
    def get_owner(cls):
        print(cls.owner, "is the owner")

    def drive(self):
        print(self.brand, "is driving")
car1 = car("tesla","cybertruck")
#print(car1.engine) # without encapsulation, object is saved as obj.id
##whenever it is encapsulated , it is saved as obj._class__id
print(car1._car__engine)

#Inheritance - a child class can use properties from parent class

##simple inheritance
class car:

    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model

    def drive(self):
        print(self.brand ," is driving")


class roadster(car):  ##roadster class was able to inherit attributes in car 
    def fly(self):
        print(self.brand,"is flying")


car7=roadster("gta","flying car")

car7.fly()

##Multiple inheritance - child taking skills of both the parents, like mother and father along with having own skills
class car:

    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model

    def drive(self):
        print(self.brand ," is driving")


class roadster(car):  ##roadster class was able to inherit attributes in car 
    def fly(self):
        print(self.brand,"is flying")

class gta(roadster):  ##gta class was able to inherit attributes in roadset
    def swim(self):
        print(self.brand,"is swimming")

car7=gta("gta","swimming car")

car7.drive()
car7.fly()
car7.swim()


##Hierarichal inheritance - One parent having multiple children

class car:

    owner = "sagar kakkala" #class variable
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model

    def drive(self):
        print(self.brand ," is driving")


class roadster(car):  ##roadster class was able to inherit attributes in car 
    def fly(self):
        print(self.brand,"is flying")

class gta(car):  ##gta class was able to inherit attributes in car
    def swim(self):
        print(self.brand,"is swimming")

car7=gta("gta","swimming car")
car7.drive()
car7.swim()
#car7.fly() ## cannot fly as it did not inherit properties from roadster



##super() - to use parent attributes inside child class
class car:

    owner = "sagar kakkala"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")


class roadster(car):

    def __init__(self, brand, model, speed):
        super().__init__(brand, model)   # calls car.__init__()
        self.speed = speed

    def fly(self):
        print(self.brand, "is flying at", self.speed, "km/h")


car7 = roadster("tesla", "roadster", 300)

car7.drive()
car7.fly()

##Method overriding- child class using his own method if he has one.
class car:

    owner = "sagar kakkala"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")


class roadster(car):

    def __init__(self, brand, model, speed):
        super().__init__(brand, model)   # calls car.__init__()
        self.speed = speed

    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")


car7 = roadster("tesla", "roadster", 300)

car7.drive()

#### Hybrid inheritance - combination of multiple types of inheritance
class car:

    owner = "sagar kakkala"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")


# Child of car
class roadster(car):

    def fly(self):
        print(self.brand, "is flying")


# Another child of car
class gta(car):

    def swim(self):
        print(self.brand, "is swimming")


# Child inherits from BOTH roadster and gta
class supercar(roadster, gta):

    def race(self):
        print(self.brand, "is racing")


car7 = supercar("tesla", "flying swimming car")

car7.drive()   # inherited from car
car7.fly()     # inherited from roadster
car7.swim()    # inherited from gta
car7.race()    # its own method

# Polymorphism -Different classes have the same method, but the method behaves differently in each class.

class tesla:

    def drive(self):
        print("Tesla is driving on the road")


class gta:

    def drive(self):
        print("GTA is driving in the air")


car1 = tesla()
car2 = gta()

car1.drive()
car2.drive()

##MRO - Mehtod resolution order
class car:

    owner = "sagar kakkala"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")


# Child of car
class roadster(car):

    def fly(self):
        print(self.brand, "is flying gta")


# Another child of car
class gta(car):

    def fly(self):
        print(self.brand, "is flying gta")


# Child inherits from BOTH roadster and gta
class supercar(roadster, gta):

    def race(self):
        print(self.brand, "is racing")

print(supercar.mro()) ## to check in which order python takes if both the classes have same method




##Abstract method - a parent class telling child class that you must mandatory have these methods in you
from abc import ABC, abstractmethod
class car(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def drive(self):
        pass


class tesla(car):

    def drive(self):
        print(self.brand, "is driving on the road")


class gta(car):

    def drive(self):
        print(self.brand, "is driving in the air")


car1 = tesla("Tesla", "Model S")
car2 = gta("GTA", "Flying Car")

car1.drive()
car2.drive()

###
class MathUtils:

    @staticmethod
    def square(number):
        return number * number
####  
