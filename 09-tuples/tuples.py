'''
a tuple is an IMMUTABLE, indexed (ordered by order of entry) container that permits duplicate elements
tuples are commonly used to store different types of data, returned from a function, 
to ensure that the data may not be modified
'''

my_tuple = ("name", 21, ["walking", "photography"], True)
print(my_tuple)
my_tuple_strings = ("name", "21", "['walking', \"photography\"]", "True")
print(my_tuple_strings)
my_tuple_numbers = (1,3,5,7,9,1,1)
print(my_tuple_numbers)
my_empty_tuple = tuple()
# my_empty_tuple[0] = "Hello"#error: TypeError: 'tuple' object does not support item assignment
# we must intialise tuples!
print(my_empty_tuple)

print(max(my_tuple_numbers))
print(min(my_tuple_numbers))
print(max(my_tuple_strings)) #name => ASCII: 110
print(min(my_tuple_strings)) #21

print(my_tuple_numbers.count(1))#num of instances
print(my_tuple_numbers.index(1))#index of first instance

print(type(my_tuple_strings))#<class 'tuple'>
my_single_value_tuple = ("Hello", "Goodbye")
my_single_value_tuple = ("Hello")
print(type(my_single_value_tuple))#<class 'str'>
# In the context of a single value, Python interprets the () as a the grouping operator, NOT the tuple constructor!
my_single_value_tuple = tuple("Goodbye")
print(type(my_single_value_tuple))#<class 'tuple'>

# we may also apply slicing to tuples as we would lists
my_slice_of_a_tuple = my_tuple_numbers[:4:-1]
print(my_slice_of_a_tuple)
print(type(my_slice_of_a_tuple))#<class 'tuple'>
# note that slicing a list returns a list
# note that slicing a tuple returns a tuple

# iterating through tuples with a for loop:

for element in my_tuple:
    print(element)

# yields values, not indices
# for index/value pairs use builtin enumerate function:

for index, element in enumerate(my_tuple):
    print(index, element)

# Tuple Arithemetic: the addition and multiplication operators may be used on tuples
print(my_tuple_numbers + (11,13))#yields another new tuple, originals unaffected
print(my_tuple_numbers * 2)#yields another new tuple, originals unaffected
# doesn't multiply elements by the factor, but yields two repeating tuples together
# same as multiplying lists