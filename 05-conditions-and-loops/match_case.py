'''
PEP 634: Structural Pattern matching
for YEARS Python has had no equivalent of switch case
This is new since 3.10.
The MATCH statement uses pattern matching to test for equality
If a match is found for a value, the case for that value executes
there are lots of performance-based arguments for and against
two reasons for adopting this syntax:
performance:
that only come into play working with large datasets
readability:
readability is also a factor
syntax:
match <subject>:
case <pattern_1>:
    <action_1>
case <pattern_2>:
    <action_2>
    # and so on
case _:
    <default case>
'''

day_of_week = 1
match day_of_week:
    case 1 | 2 | 3 | 4 | 5:
        print("It's Monday")
    case 6 | 7:
        print("It's Sunday")
    case _:
        print("Choose a day, 1-7")