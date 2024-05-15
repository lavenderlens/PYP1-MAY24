'''
functions, as in any otehr language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can afunction be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
'''

my_str = "hello"
print(my_str[0])#prints first character

def first_character_of_word():
    print(my_str[0])

first_character_of_word()#h

my_str = "goodbye"

first_character_of_word()#g

# as it stands, the function breaks principle of idempotence
# or, out another way, function is IMPURE
# all functions should be idempotent and pure
# the result should not change for the given input, including nothing
# the way to solve this is actually very simple
# if we provide a parameter to the function
# the function passes in a COPY of the data at runtime
# definition time: parameters
# runtime: arguments

def first_character_of_word_pure(word):
    print(word[0])

first_character_of_word_pure(my_str)

my_str = "Slàn"

first_character_of_word_pure(my_str)

# functions in Python are objects too, and may be passed as input OR returned as output to/from other functions
print(first_character_of_word_pure)#<function first_character_of_word_pure at 0x10069c860>
# ie, an object of type function

character = first_character_of_word_pure("word")#prints w
print(character)#but persists as None
# this is because the function doesn't have a return

def first_character_of_word_pure_return(word):
    return word[0]

first_character_of_word_pure_return("word")#see nothing - no print statement in function
# BUT function output may now be persisted
character = first_character_of_word_pure_return("sentence")#function result/return
print(character)

# point: output-independent
first_char = first_character_of_word_pure_return#function passed as data
# call it by the new name
print(first_char("weekend"))#output from our new function as input to print() function

# named vs. positional agruments, default arguments
# Python function parameters work in two ways:

# positional arguments
def open_account(name, balance):
    balance += 100
    return (name, balance)

account_info1 = open_account("Lavender", 100.00)
print(account_info1)
# the below doesn't run with arguments in the wrong order
# account_info2 = open_account(100.00, "lavender")
# print(account_info2)

# named (keyword) arguments
def open_account_named(name="John Doe", balance=0.0):#default values
    balance += 100
    return (name, balance)

print(open_account_named())
print(open_account_named(name="Alan Doe", balance=50.0))
print(open_account_named(balance=75.0, name="Jane Doe" ))#position doesn't matter, name does
# arguments are by default positional
# you can mix named and positional args
# but if so, named must come AFTER positional in parameter list,
# otherwise positional args must also be named - see **

# 1. no input, no output (means no return statement)
def greet1():
    print("Hello")
    print("World, from greet1")
    print("How are you today")

greet1()

# 2. no input, output (return statement)
def greet2():
    return "Hello \nWorld, from greet2 \nHow are you today"

print(greet2())

# 3. input, and output (return statement)
def greet3(name):
    return f"Hello \n{name}, from greet3 \nHow are you today"

print(greet3("Alan"))

# . input, no output (return statement)
def greet4(name):
    print(f"Hello \n{name}, from greet4 \nHow are you today")

print(greet4("Keith"))

# . input, no output (return statement)
def greet5(name):
    print(f"Hello \n{name}, from greet5 \nHow are you today")

# print(greet5())#no arg provided: TypeError: greet5() missing 1 required positional argument: 'name'

def greet6(name="person 1"):#this is now a named arg
    print(f"Hello \n{name}, from greet6 \nHow are you today")

print(greet6())
print(greet6("Fred"))#works either way, with or without arg

def greet7(age, name="person 1"):#this is now a mix of named and positional args
# def greet7(name="person 1", age):#SyntaxError: non-default argument follows default argument
    print(f"Hello \n{name}, from greet7 \nYou are {age} years old today")

greet7(21, "Alan")# named args must follow positional ones

    

