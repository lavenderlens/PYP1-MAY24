'''
strings are immutable containers of characters, 
they may contain duplicate characters
string methods return a new string
the original is unaffected but the same reference may be updated 
to point to the new string
'''

s1 = "Hello"
s2 = "Hello"
print(s1, id(s1))#Hello 4344631728
print(s2, id(s2))#Hello 4344631728
print(s1 == s2)#True

s3 = str("Goodbye")
s4 = str("Goodbye")
print(s3, id(s3))#Goodbye 4363690992
print(s4, id(s4))#Goodbye 4363690992
print(s3 == s4)#True

s1 = s4
print(s1, id(s1))#Goodbye 4307051504 # NOTE: NEW ID, FRESH CONTAINER

# loads of string methods,

# number formatting

import math
print(math.pi)
print(f'PI to two dec.places = {math.pi:.2f}')
print(f'price to two dec.places = {19.994:.2f}')
price = 19.999
print(f'price to two dec.places = {price:.2f}')#does rounding as well
print(f'price to two dec.places = {20:.2f}')#
