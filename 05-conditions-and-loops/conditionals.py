'''
conditional statements are very smilar in Python to other langauges,
they execute a block of code depending on whether a condition evaluates True or False
if True:
    code block, defined by indent, immediately following is executed
if False:
    skipped

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statement tests a single variable or expression for equality

'''

a = 3
b = 4
c = 5
d = 5
# one branch
# if False:
if a > b and c == d:
    print("IF block executed")

# two branches
if False:
# if a > b and c == d:
    print("SECOND IF block executed")
else:
    print("ELSE block executed")

# three or more branches
if False:
    print("FIRST IF-ELIF block executed")
elif True:
    print("SECOND IF-ELIF block executed")
else:
    print("ELSE block executed")

# there is NO LIMIT to the number of IF-ELIF statements that can be chained together

# Pythonesque syntax: an if else may be written on one line:
temp = "cold"
clothing = "jumper" if temp == "cold" else "T-shirt"
# note this is Python equivalent of the ternary operator in other languages
# think of it as an XOR gate: Either side may be true for the whole gate to be true
# but BOTH sides being true will not result
# either-or/exclusive or