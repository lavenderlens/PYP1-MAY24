'''
scope defines the visibility and lifespan of a variable
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   lives whilst the whole script is executing

'''

next_num = 1

def get_next_num():
    return next_num

print(get_next_num())

def increment_next_num():
    next_num += 1 # UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
    return next_num

# print(increment_next_num())

# when we attempt to ASSIGN anything to next_num we cannot
# this is because Python assumes any assignment to be to a LOCAL variable
# they are DIFFERENT variables in DIFFERENT scopes, with the SAME name

def increment_next_local_num():
    next_num = 2 # a new LOCAL variable is declared
    next_num += 1 # will no longer error
    return next_num

print(increment_next_local_num())#3

print(next_num)#1 still

# what if we wish to modify the global variable?
# we must explicitly bind it inside the function

def increment_global():
    global next_num # yes! a keyword! and no! no initialisation
    next_num += 1 # now refers to next_num in the global scope
    return next_num

print(increment_global())# 2

print(next_num)# 2

'''
now, our latest function, increment_global, REMEMBERS STATE of global variable between executions
BUT other functions in the module may ALSO affect the global by binding to it themselves!
what if we wished to encapsulate this behaviour within a single function, so that ONLY that function has its OWN state?

remember functions in Python may be passed to and returned from other functions...
'''
# stage 1: define an inner function, which then takes the outer function as its effective global scope
# here is global scope
def increment_with_closure():
    # this scope is now the effective global scope for the inner function below
    # here is now effectively global for get_next_num
    next_num = 1
    def get_next_num():
        print(next_num)
        #
    get_next_num()

increment_with_closure()#prints 1

# stage 2:
def increment_with_closure():
    next_num = 1
    def get_next_num():
        next_num += 1 #UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
        # same error as non-bound global!
        return next_num
    get_next_num()

# increment_with_closure()#prints error

# REMINDER:
def my_func():
    pass

# I can pass the function code to another reference variable:
my_new_func = my_func
# I can then execute the new function
my_new_func()

# stage 3:
def increment_with_closure():
    next_num = 1 # a lexically-scoped variable
    def get_next_num():
        nonlocal next_num
        next_num += 1 
        return next_num
    return get_next_num # outer func returns inner func code, NOT output

# create a closure from the outer function
# a closure captures the value of the nonlocal variable
my_closure = increment_with_closure()# we do run the outer function to create the closure:
# it now has a stateful memory of next_num = 1
print(my_closure())#2
print(my_closure())#3
print(my_closure())#4
print(my_closure())#5
'''
what's happening is the value for next_num is remembered from one execution to the next of the closure
effectively, the value of next_num is encapsulated within the outer function
it becomes the effective global scope for the inner function
by doing this, the variable is removed from the actual global scope and so protected from other functions
what if we want to refresh/reset the inner function's state?
we make a new fresh closure

basically, closures rely on two principles:
lexical scope, which measn a variable is scoped to a function but referenced from another inner function
and returning a function from a function
'''
my_closure = increment_with_closure()
print(my_closure())#2
print(my_closure())#3
print(my_closure())#4
print(my_closure())#5

