# WAY 1
# import functions_module

# print(functions_module.add(1,1))
# print(functions_module.sub(1,1))

# arguably the clearest
# every time you call a function you must reference the module from whence it came

# WAY 2
# from functions_module import add, sub, mul, div
# print(add(2,2))
# print(sub(2,2))
# but when you use these functions in this script, 
# you don't necessarily know that they are NOT FROM this script

# WAY 3 (possibly the worst way of all!) - the wildcard
from functions_module import *

print(add(1,1))# usage same as way 2 - no qualifier
