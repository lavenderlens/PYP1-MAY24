'''
a list is a mutable, indexed (ordered by order of entry) container that permits duplicate elements
lists are commonly used to store groups of objects 0f the same sort, but need not be
'''

# creation
# nums = list()# an empty list # optional step
nums = [1,2,3]

# reference single elemnt
print(nums[2])

# reassign single element
nums[2] = 4
print(nums[2])

# slicing: the creation of a new list from parts of an initial list
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))

# slices: up to 3args, startIdx inclusive, endIdx exclusive, step
slice1 = fib[4:8]
print(slice1) # [3, 5, 8, 13]
# exclusive end index even works for last element
slice2 = fib[7:]
print(slice2)
slice3 = fib[7:10]#index 10 is out of bounds
print(slice3)
# print(fib[10])#IndexError: list index out of range
slice4 = fib[::-2]
# print(slice4)#34, 13, 5, 2, 1] backwards, from the end, in steps of 2

# builtin methods (not specific to list contaoners):
print(f"num_elements: {len(fib)}")
print(f"sum_elements: {sum(fib)}")
print(f"min_element: {min(fib)}")
print(f"max_element: {max(fib)}")

#  we may add lists
list3 = [10,20.30] + fib
print(list3)

# we may multiply lists
list4 = list3 * 10
print(list4)#this returns ten lists

# what if we wish to multiple individual elements and return a list of the same length?

#  list comprehension enables us to pass in a loop function to transform elemnts of a list and return new list with the transformations

scaled_list = [element * 2 for element in list3]#very shorthand and neat
print(scaled_list)

# this is basically shorthand for
new_scaled_list = []
for element in list3:
    new_scaled_list.append(element * 2)
print(new_scaled_list)

# the above produces a transformation for EVERY/EACH element of the list
# we may also use list comprehension to produce a FILTER for ONLY those elements of teh original list taht pass a test (PREDICATE)

list_of_numbers_under_10 = [element for element in list3 if element <= 10]
print(list_of_numbers_under_10)

