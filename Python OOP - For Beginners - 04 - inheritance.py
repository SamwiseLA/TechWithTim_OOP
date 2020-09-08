# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#

# Inheritance - Ability to use & KEEP an existing class as a parent (or foundational structure) of another class (child)
#
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I speak, I'm just a Pet!")


class Cat(Pet):  # Cat class Inherits attributes and methods from the PET class
    def __init__(self, name, age, color):
        super().__init__(name, age)  # super() references the super or parent class in THIS() class statement
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and {self.color}.")


class Dog(Pet):  # Dog class Inherits attributes and methods from the PET class
    def speak(self):
        print("Woof")


class Fish(Pet):
    pass


pet = Pet("Kombucha", 67)
cat = Cat("Fluffy", 7, "Orange")
dog = Dog("Ralph", 4)
fish = Fish("Dori", 1)

print(f"{pet.name} says...")
pet.speak()

print(f"{cat.name} and I'm {cat.color} and says...")
cat.speak()

print(f"{dog.name} says...")
dog.speak()

print(f"{fish.name} says...")
fish.speak()

print("\n--- Speak!!! ---\n")

pet.show()
cat.show()
dog.show()
fish.show()
