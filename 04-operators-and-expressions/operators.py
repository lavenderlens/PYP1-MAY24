# an expression involves operators and operands. In the following:
x = 1
x = x + 1
# the first line initialises x with a single value
# the second line assigns x the result of an expression
# the expression has an operator, +
# and two operands, x (again), and 1

# arithmetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 cubed is 2 ** 3
# /
# %     - remainder, whole number division
# //    - quotient, whole number division (floor division)

print(10 / 2) #5
print(10 % 2) #0

print(10 / 3) #3.3333333333333335 *promotion going on
print(10 % 3) #1
print(10 // 3) #3

# *promotion;
print(9 + 2.0)#11.0

# non-numeric arithmetic
print("ho" * 3)
print("* " * 50)

# assignment operators

# =     - assignment
# +=    - compound assignment (addition)

print(y := 1) # the walrus operator assigns AND returns at the same time
y = y + 1
y += 1
print(y)
# note : there is NO increment/decrement operator in Python 
# these you will see in other languages as
# ++ or --
# Python contains a lot of optimisations, if we can call them that,
# where Guido looked at something and thought we don't need that

# += is overloaded to work with strings
# overloading is when a function, either builtin or custom,
# works with alternative arguments

my_sentence = ""
my_sentence += "I "
my_sentence += "love "
my_sentence += "Python. "
print(my_sentence)
#  worth noting as an aside: how many strings were created in the last few lOC?
# intuitively, 1
# actually, 6

# -=    - compound assignment (subtraction)
# *=    - compound assignment (multiply)
# /=    - compound assignment (division)
# %=    - compound assignment (modulus)
# **=   - compound assignment (exponent)
# //=   - compound assignment (floor division)

# multiple assignment (this is useful)
x = 1; y = 2; z = 3
# may be re-written as:
x, y, z = 1, 2, 3
# referred to in JS as a destructuring assignment
# useful when saving dictionary props or list elements to individual variables
my_dict = {"name": "Alan", "age": 21}
name, age = my_dict["name"], my_dict["age"] # this implies KNOWLEDGE of the dict structure
print(name, age)

# assignment operator chaining (more specialised, avoid if possible)
x = 1
y = 1
# may be re-written as:
x = y = 1

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
3 >= 4      #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as
my_list = [1,2,3]
my_other_list = [1,2,3]
my_copied_list = my_list

print(my_list is my_other_list)#False
print(my_list is my_copied_list)#True

# we could say:
my_copied_list = my_list = [1,2,3]
# in both sorts of declaration, my_list and my_copied_list both POINT TO the same list
# my_other_list points to a separate list that just happens to look the same, but isn't
# there isa  function builtin to Python that reveals this subtle but important difference
print(id(my_list))          #4336868160
print(id(my_other_list))    #4336769408 - different
print(id(my_copied_list))   #4336868160
# in these examples, the id() function refers to NESTED, COMPLEX, data in containers
# which are also MUTABLE

# in tests for MEMBERSHIP: is in same container as
my_list = [1,3,5,7,9]
print(3 in my_list)#True

# each of these last two operators has a inverted/flipped version:
# is not
# not in

# logical operators
# evaluate to either True or False

# and
# or
# not

is_year_end = True
is_taxable = True

if is_year_end and is_taxable:
    print("Time to do your tax return!")

# and requires BOTH operands to be true

if 1 and 1:
    print("Both numbers are true")
if 1 and 0:
    print("Both numbers are true")

# in this case, numbers are converted to their truthy/falsey values for the logical operator to work
# but the expression is not the result: the SECOND operand is
if 1:
    print("1 is true")
if 0:
    print("0 is false")

print(bool(1) and bool(0))#False, equivalent to saying
print(bool(0))#False

# operator precedence
print(10 + 10 * 2) # 30: * is higher precedence than + 
print((10 + 10) * 2) # 40: grouped expression evaluated first