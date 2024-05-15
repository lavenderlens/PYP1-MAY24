'''
Loops come in two sorts: the while loop and the for loop
# while loops are commonly used for console IO
# there may be no obvious end to the process
# for loops are commonly used to iterate over containers
# the length of the container is known in advance
The for loop in Python is syntactic sugar for a while loop, 
usually when the number of iterations is known in advance.
There are no for loops at runtime, only while loops that the code is compiled into.
While loops in source code are useful when the number of iterations is not known in advance.

In Python, an optional else clause may be added to the end of both types of loop, for and while.
It is executed if the loop completes and doesn't hit a break statement.
In other words, if the loop completes normally.
To make this clearly readable, add a comment "# no break" next to the else clause.
'''

# for is used for iterating through an ireable object, typically a container
# remember, lists, sets, and tuples have a len() length prop

names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson']

print("\nas LIST:")
for name in names:
    print(name)
# first variable, name, is arbitrarily-named
# it's on us: it just should be a SINGULAR word
# second variable name is actual reference to a container
# it should be a PLURAL word

# can we go for a range of values within?
# we could certainly using list comprehensions
# we may also apply a slice to the list variable name

print("\nas sliced LIST:")
for name in names[2:4]:
    print(name)

# the for loop works for sets and tuples as well, but sets are not ordered, 
# and we cannot use slicing on sets asa result
names_as_set = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson'}

print("\nas SET:")
# for name in names_as_set[2:4]: #TypeError: 'set' object is not subscriptable
for name in names_as_set: #TypeError: 'set' object is not subscriptable
    print(name)
''' run once:
Gordon Brown
David Hume
Janet Jackson
James Brown
Michael Jackson
David Bowie'''
''' run twice:
David Bowie
Gordon Brown
Michael Jackson
David Hume
Janet Jackson
James Brown'''

names_as_tuple = ('Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson')

print("\nas TUPLE:")
for name in names_as_tuple[2:4]: #TypeError: 'set' object is not subscriptable
# for name in names_as_tuple: 
    print(name)

# more complex: looping through dictionaries
coords = {"x": 12, "y": 12, "z": 12}
# both keys AND values OR keys and values TOGETHER are iterable

# for keys
for key in coords.keys():
    print(key)

# for values
for value in coords.values():
    print(value)

item_tuples = []
item_lists = []
# for both keys and values
for key, value in coords.items():
    # print(key, value)
    item_tuples.append((key, value))# double brackets as only one arg to append()
    item_lists.append([key, value])# double brackets as only one arg to append()
item_tuples[2] = ("z", 13)#overall structure is list: therefore mutable
# item_tuples[2][0] = ("zz")#internal structure is tuple: therefore immutable
# TypeError: 'tuple' object does not support item assignment
print(item_tuples)# a list of tuples - EACH tuple is immutable
print(item_lists)# a list of lists/2D list - mutable
# tuples are very often returned from Python functions

# we may use a for loop to loop through a string, character by character
word = "opposition"
for character in word:
    print(character)

# we can use a range function (builtin) to iterate n times
# range() takes up to 3 args, startIndex, andIndex exclusive, and step
# for example loop from 5 to 50 in steps of 5
for i in range(5, 51, 5):
    print(i)

# we may also chain an optional else
# this will only execute of the loop completes

for name in names:
    print(name)
    if name == "James Crown":
        print(f"ERROR - {name} too funky for my code")
        break
else:
    print("list processed with no errors")

# WHILE loops
# while loops may be tweaked to iterate through containers (of known length)
# but are best suited to other iterative scenarios
# where the call to the interrupt the loop comes after an unknown number of iterations

band = ["Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

counter = 0
while counter < len(band):
    print(band[counter])
    counter += 1

list_of_names = []
while True:
    name = input("Enter a name or X to quit")
    # name = input("Enter a name or ß to quit")
    if name.lower() != "x":
    # if name.casefold() != "ss":#locale-specific function for converting to lower case
        print(name)
        list_of_names.append(name)
    else:
        break
print(list_of_names)

print("using break with a container")
counter2 = 0
while counter2 < len(band):
    if band[counter2] == "Clarence":
        break
    print(band[counter2])
    counter2 += 1
print("using continue with a container")
counter3 = 0
while counter3 < len(band):
    if band[counter3] == "Clarence":
        counter3 += 1
        continue
    print(band[counter3])
    counter3 += 1
