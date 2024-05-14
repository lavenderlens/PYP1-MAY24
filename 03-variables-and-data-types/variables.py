# variables must always (almost) be initialised
# this is because there is *almost* no keyword used
x = 1
print(type(x)) #<class 'int'>

#variable re-assignment
x = 2.5
print(type(x)) #<class 'float'>

x = "two"
print(type(x)) #<class 'str'>

# assign one variable to another
# x -> "two" <- y
y = x #the value of x at the moment y was instantiated
x = 3
print(y)#two
print(type(y))#<class 'str'>
