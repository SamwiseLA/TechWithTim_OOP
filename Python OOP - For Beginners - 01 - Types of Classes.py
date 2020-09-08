# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#


p01 = False
if p01:
    x = 1
    y = "Fred"
    print(f"{type(x)} is the Class type of x ")
    print(f"{type(y)} is the Class type of y ")

    # Classes have Methods, which is one of the attributes that is associated with those classes, like str has Upper
    print("-----------")
    print(y)
    print(y.upper())
    print("-----------")

p02 = False
if p02:
    def hello():
        print("hello")

    hello()
    print(type(hello))

# How Classes Interact
p03 = False
if p03:
    x = 1
    y = "hello"
    print(x + y)
    # Look at the error!
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # MEANS: + is not supported between 'int' and 'str' types

# Methods
p04 = False
if p04:
    string = "hello"
    print(string.upper())
    # The Method upper() is working on the Object "string"
