# because there is no keyword (with a couple of exceptions) in Python for declaring variables
# we MUST initialise them (give them an initial value using single = of assignment)
name = "Alan"
print(name)
print("Alan Lavender")
# print(x)#we cannot do this
# a_function()#or this
x = 1#declaring and initialising

x = 3#re-declaring
y = 4
z = 5

print(x + y + z)

# functions (in brief) DO have a keyword - def (definition)
def a_function(a:int, b:int) -> int:
    # a doctring appears HERE (first line(s) inside a function)
    # it describes the function and is accessed when the developer runs help() on the function
    """returns sum of two numbers

    Args:
        a (int): number1
        b (int): number2

    Returns:
        int: number1 + number2
    """
    # TODO
    # pass

    # print(a + b)
    return a + b

print("Carrying on...")

# things to note:
# def keyword
# function name follows naming best practice
# include parameter brackets even if nothing in them
# colon at end of declaration line
# MOST importantly, and indent
#   indents describe code blocks
# what is indented belongs only to the line before the indent
# when we want to come out of the block
# we return one tab space back
# editor (VS Code) will automatically indent after a colon
# default is 4 spaces/ 1 tab
# character limit on one line of Python (not mandatory) 79 characters 
# this is not a theoretical limit but best practice
# PEP stands for Python Enhancement Program
# PEP 8, early on, was the style bible for the langauge
# it is still followed, despite fact we are on PEP x100s

# persisting output from a_function as a variable
total = a_function(42,1)#data
print(total)
# persisting output from a_function as input to another function (print)
print(a_function(x,y))#variables

# pretty much the on eplace you will see a semi-colon in Python is to separate multiple statements on one line
s = 20; t = 21
# however best to avoid this if you can

# indenting with conditionals similar to indenting when defining functions:
if t >= 21:
    print("t is greater than or equal to 21")
# nothing to do with the if
print("Carrying on ...")
# if(this_thing_with_a-very-long_name 
#    == that_thing_with_a-very-long_name)

# if{this_thing_with_a-very-long_name 
#    == that_thing_with_a-very-long_name}

# if this_thing_with_a-very-long_name \
#    == that_thing_with_a-very-long_name

# naming conventions 
# name must start with a letter or an underscore
# remainder of name may be composed of letters, digits, and underscores 
# names are case-sensitive
# in all variable names they should be lower case
#  apart froom class names which should start with an upeprcase letter
my_number = 1
def my_function():
    pass
class My_class:
    pass

# this is to alert devs after us that a class may exist for this function
my_instance = My_class()

# in other languages, for instance Java, we have the new keyword to denote a new instance
# JAVA:
# MyClass myInstance = new MyClass();
# var myInstance = new MyClass();

# constants in Python
# there is formally no such thing
# so again, naming conventions are super-important
# SCREAMING_SNAKE_CASE
MY_CONSTANT = 1
MY_CONSTANT = 2 #can still be changed

# module and package names
# should be ALL lowercase and no underscores
# mymodule
# mypackage

# do not use lower case L or uppercase o for clarity

# the input() function - builtin

# print("Enter a name")
# name = input()
# print(name)

# can be abbreviated to one line
name = input("Enter your name")

# to eexecute this script, my_first_script.py, either press play arrow in IDE
# OR
# call interpreter and pass script
# python3 my_first_script.py