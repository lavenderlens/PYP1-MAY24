'''Circle module'''

from math import pi as PI #to demonstrate aliasing

def area(radius):
    return PI * radius**2

def circumference(radius):
    return 2 * PI * radius