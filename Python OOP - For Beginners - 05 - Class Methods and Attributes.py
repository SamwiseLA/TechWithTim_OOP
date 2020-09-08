# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#

# Class attributes and Methods are specific to a CLASS and NOT the instantiated Object

class Person:
    number_of_people = 0  # Class Level Attribute

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # Class Level Method aka Function
    def get_number_of_people(cls):  # Class Level Methods reference (cls) the class not the instance
        return cls.number_of_people

    @classmethod  # Class Level Method aka Function
    def add_person(cls):  # Class Level Methods reference (cls) the class not the instance
        cls.number_of_people += 1


print("Add Tim")
p1 = Person("Tim")

print(f"Attribute from Class   : number_of_persons: {Person.number_of_people}")
print(Person.get_number_of_people())

print("Add Sam")
p2 = Person("Sam")

print(f"Attribute from Class   : number_of_persons: {Person.number_of_people}")
print(Person.get_number_of_people())
