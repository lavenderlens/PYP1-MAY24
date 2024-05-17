'''
sets are mutable, unordered containers that do not permit duplicates
as such, they are often used for converting lists with duplicates into lists with unique values
'''

# creation
unique_nums_1 = {4,4,5,5,6,6}
unique_nums_2 = set((1,1,2,2,3,3))#grouped in ANY WAY, but must be grouped
unique_nums_2 = set({1,1,2,2,3,3})#set
unique_nums_2 = set([1,1,2,2,3,3])#list
# unique_nums_2 = set(1,1,2,2,3,3)#error
# grouping brackets not retained internally
print(unique_nums_1)
print(unique_nums_2)
# TODO unordered?

# convert from list to set:
my_list = [7,7,8,8,9,9]
my_converted_set = set(my_list)
print(my_converted_set)

# convert back to list:
my_list_unique_values = list(my_converted_set)
print(my_list_unique_values)

# Note: sets DO NOT work with dicts

# set methods for Venn-diagram-style transformations:
set_in_common = unique_nums_1.intersection(unique_nums_2)
print(set_in_common)#nothing in common
set_difference_from_other = unique_nums_1.difference(unique_nums_2)
print(set_difference_from_other)#{4, 5, 6}
set_difference_from_other_reversed = unique_nums_2.difference(unique_nums_1)
print(set_difference_from_other_reversed)#{1, 2, 3}
both_differences = unique_nums_1.symmetric_difference(unique_nums_2)
print(both_differences)#{1, 2, 3, 4, 5, 6}
both_differences_inverted = unique_nums_1.symmetric_difference_update(unique_nums_2)
print(both_differences_inverted)#None, but mutates original!
print(unique_nums_1)#{1, 2, 3, 4, 5, 6}#MUTATED!
print(unique_nums_2)#{1, 2, 3}

# two sets where there is overlap:
nums_1 = {1,2,3,4,5}
nums_2 = {4,5,6,7,8}

print("two sets where there is overlap:")
set_in_common = nums_1.intersection(nums_2)
print(set_in_common)#{4, 5}
set_difference_from_other = nums_1.difference(nums_2)
print(set_difference_from_other)#{1, 2, 3}
set_difference_from_other_reversed = nums_2.difference(nums_1)
print(set_difference_from_other_reversed)#{8, 6, 7}
both_differences = nums_1.symmetric_difference(nums_2)
print(both_differences)#{1, 2, 3, 6, 7, 8}
both_differences_inverted = nums_1.symmetric_difference_update(nums_2)
print(both_differences_inverted)#None, but mutates original!
print(nums_1)#{1, 2, 3, 6, 7, 8}#MUTATED!
print(nums_2)#{4, 5, 6, 7, 8}


