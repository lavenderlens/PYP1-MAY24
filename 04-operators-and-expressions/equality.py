# the == operator is used to test for equality
# when using builtin types/classes, the behaviour of the == operator
# is specified by the __eq__ dunder method in the class
# when using our own user-defined object types/classes
# we may wish to override this method ourselves to provide the desired result
# overriding means to do the same thing differently, different implementation
# whenever the == operator is used with objects/dicts/lists etc
# it DIRECTLY CALLS the __eq__ method 
# if there is no overridden version of this method, the default implementation will be used

num1 = 1
print("id of num1", id(num1)) #4334494888
num2 = 1
print("id of num2", id(num2)) #4334494888 same
# in these examples, the id() function refers to single values, which are also IMMUTABLE

print(num1 == num2)

my_list1 = [1,3,5,7,9]
my_list2 = [1,3,5,7,9]

print(my_list1 == my_list2)#this comparison works because the __eq__ method of list is implemented here
# it says, if the length, order, and elements of list a match those of list b, 
# then a and b are equal
print("id of list1", id(my_list1)) #4300297344 4377564288 after reload
print("id of list2", id(my_list2)) #4300396928 4377663872 after reload

