# type conversion happens implicitly in Python but may be called explicitly as well.
# each data type has its wrapper function of the same name

# conversion to boolean (bool)
# every data type has its truthy and falsey values (converting to True or False)
# it's easier to remember the falsey values - most values are truthy
# falsey:
# Zero numbers
# empty collections/containers
    # collections include str (a collection of characters)
# None

print("Using bool() wrapper")
print(bool(1))
print(bool(0))
print(bool(-0))

print(bool("Hello"))
print(bool(""))

print(bool([1,2,3]))
print(bool([]))

#  to int
print("using int()")
print(int(True))
print(int(False))
print(int(1.0))
print(int(1.5))# no rounding, only truncation

#  to float
print("using float()")
print(float(1))
print(float(True))

print(str(float(1)))#can be nested

# to str
# the str() wrapper is a special case
# conversion of simple values like numbers is predictable
# the same cannot be said for complex objects
# for an object to have a str() conversion function
# the object's class must implement dunder method __str__
# as it must implement __eq__ to lay down business rules for equality

print("using str()")
print(type(True))
print(str(True))
print(type(str(True)))
print(type(123))
print(str(123))
print(type(str(123)))

# to list
print("using list()")
print(list("Hello"))
print(type(list("Hello")))

#  there exist methods for sets (set()), and dicts as well (dict())

