# Solution of Exercise 42 - Exercise_42.py
#
# Updated by Aurimas A. Nausedas on 11/03/21.

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Make a class Dog that is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## class Dog has-a __init__ with self and name parameters
        self.name = name

## Make a class Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a __init__ that takes parameters self and name
        self.name = name

## Make a class Person that is-a object
class Person(object):

    def __init__(self,name):
        ## class Person has-a __init__ that takes parameters self and name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Make a class Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name and salary (class Employee has-a __init__ that takes parameters self, name and salary)
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## Set rover to an instance of class Dog, which has-a attribute of name set to Rover.
rover = Dog("Rover")

## satan is-a Cat instance that has-a attribute name set to Satan
satan = Cat("Satan")

## Set mary to an instance of class Person and has-a attribute name set to Mary
mary = Person("Mary")

## From mary get pet attribute and set it to satan; mary has-a pet that is-a satan
mary.pet = satan

## frank is-a Employee instance has-a attribute name of Frank and attribute salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet attribute that is-a rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is-a  Halibut instance
harry = Haliut()
