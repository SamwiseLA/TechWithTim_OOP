# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#

# Static methods are methods in a CLASS, grouped together because they are a useful package of Methods

import OOPStaticMethods as Sa

print(Sa.Math.add5(5))
print(Sa.Math.add10(5))
Sa.Math.pr()

print(f"Type for Sa ----------->{type(Sa)}")
print(f"Type for Sa.Math ------>{type(Sa.Math)}")
print(f"Type for Sa.Math.add5-->{type(Sa.Math.add5)}")

