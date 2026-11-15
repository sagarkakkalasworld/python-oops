class Car:

    owner = "Sagar Kakkala"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, "is driving")


class Roadster(Car):

    def fly(self):
        print(self.brand, "is flying at")

    def drive(self):
        print(self.brand, "is driving at")


class GTA(Car):

    def swim(self):
        print(self.brand, "is swimming")


class SuperCar(Roadster, GTA):

    def race(self):
        print(self.brand, "is racing")


class MathUtils:

    @staticmethod
    def square(number):
        return number * number


def main():

    # Object example
    car1 = Car("Tesla", "Cybertruck")
    print(car1.model)

    # Instance method
    car1.drive()

    # Class variable
    print(car1.owner)

    # Inheritance
    car2 = Roadster("Tesla", "Roadster")

    car2.drive()
    car2.fly()

    # Multiple inheritance
    car3 = SuperCar("Tesla", "Flying Car")

    car3.drive()
    car3.fly()
    car3.swim()
    car3.race()

    # Static method
    print(MathUtils.square(10))


if __name__ == "__main__":  ## if the main function is not there, it defaults calls all the classes and variables, here this means class is main function only runs when
                            ##when python3 main_example.py is run and for remaining whenever this class is imported, only that particular function is run, to understand it better
                            ##run python3 en.py by changing example.py first line to from demo import MathUtils
    main()