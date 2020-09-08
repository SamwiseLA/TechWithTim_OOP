# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#


# Creating a Class
p05 = True
if p05:
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print(f"*** {self.name} has been instantiated! ***")

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age

        def set_age(self, age):
            self.age = age

        def meow(self):
            return "Meow?"

        def bark(self):
            print("BARK!")

        def add_one(self, n):
            return n + 1

    d = Dog("Spot", 3)
    d2 = Dog("Bill", 4)

    print(type(d))
    d.bark()
    print(d.meow())
    print(d.add_one(5))  # Called Method
    print(d.name)
    print(d2.name)
    print("=v=v=v=v=v=")  # Called Method
    print(d2.get_name())
    print(" ---> Before and After Set Age <---")
    print(d2.get_age())
    d2.set_age(7)
    print(d2.get_age())
