# the standard built-in data types

# bool
# values: True or False (OR some expression that evaluates to them)
# immutable type
my_bool = True

# int
# values: whole numbers, positive or negative (OR some expression that evaluates to them)
# immutable type
my_int = 1

# float
# values: any fractional number, positive or negative (OR some expression that evaluates to them)
# immutable type
my_float = 1.0

# str
# values: any text of zero or more characters
# immutable
# single or double quotes (or triple as in f-strings and docstrings
# indexed from zero (first character)
# have inbuilt length property referenced by len()
my_str = 'Hello'
first_character = my_str[0]
print(my_str[0])#H
print(len(my_str))#5

# containers (in brief)
# a Python container holds or references multiple elements

# list (loosely equivalent to array in other languages)
# values: the elements of a list can be of any type
# but usually for predictability are of one
# mutable (can be modified in-place)
# indexed (from zero)
my_list = ["bat", 'ball', "gloves"]#sgl or dbl quoted
print("Type", type(my_list))

# 1. reading whole list
print(my_list)#this is actually leveraging the __str__ dunder method of the list class
# you do hear dunder methods referred to as "magic methods" because they're not explicit
# you may specify your own dunder method overrides in your own classes

# 2. loop through my_list as it is iterable
for el in my_list:
    print(el.upper())

print(my_list)#['bat', 'ball', 'gloves'] original unchanged

# Q: what if we wanted to start from n elements in the list and go to the end?
# A: list comprehensions/slicing enable this - see list chapter
# list COMPREHENSIONS (later) return a NEW LIST with changes
# list SLICING: returns a PARTIAL LIST with selections
# BOTH methods do not mutate original list

print("using list slicing")
#  three arguments
# from index inclusive:
# end index exclusive:
# step:
# [::] prints whole list

for el in my_list[1:]:#take from 2nd element to end
    print(el.upper())
# output:
# BALL
# GLOVES

for el in my_list[::-1]:#go backwards from end
    print(el.upper())
# output:
# GLOVES
# BALL
# BAT

# lists are MUTABLE:
my_list[0] = "box"
print(my_list)

# tuples
# values: the elements of a tuple can be of any type
# indexed from 0
# immutable (the MAIN difference)
my_tuple = (42, "The ultimate answer")
print(my_tuple[0])
print(my_tuple[1])
print("Type", type(my_tuple))
# my_tuple[0] = 43 #TypeError: 'tuple' object does not support item assignment
# tuples often used in Python as return values from functions 
# whose data we wish to treat as if it were immutable

# sets
# values: the elements of a set can be of any type
# sets are NOT ORDERED
# sets may NOT CONTAIN DUPLICATES
# set methods compare and combine sets on things like overlap, difference
my_set = {1,2,2,3,4,5,5}
print(my_set) #{1, 2, 3, 4, 5}
my_str_set = {"one", "two", "two", "forty-four", "ninety-none", "a-one"}
print(my_str_set) #{'forty-four', 'two', 'a-one', 'ninety-none', 'one'}
print("Type", type(my_set))

# dict
# values: key: value pairs
# the keys MAY BE of any type but are commonly strings (meaningful)
# keys MUST BE unique
# values may be of any type and can be duplicated
# mutable
# note: a Python dict IS NOT an object literal 
# (even though the key-value pairs look like object prop names and prop values)
# objects in Python are made by classes
# theoretically EVERYTHING is an object in Python
my_dict = {"name": "fred", "age": 33, "employed": True}
print(my_dict)#the whole of my_dict using the dunder __str__ method
print("Type", type(my_dict))
print(my_dict["employed"])

# none (null equivalent)
my_none = None
print(my_none)
print(type(my_none)) #<class 'NoneType'>

# number base encoding
# binary: prefix the expression with 0b
# octal: prefix the expression with 0o
# hex: prefix the expression with 0x

# underscores in number values
my_big_number = 1_000_000




