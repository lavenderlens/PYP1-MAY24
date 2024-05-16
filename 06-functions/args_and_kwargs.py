'''
args - multiple positional arguments
denoted in parentheses as *args
the word args is arbitrary
the * is mandatory

kwargs - multiple named (keyword) arguments
denoted in parentheses as **kwargs
the word kwargs is arbitrary
the ** is mandatory
'''

def greet(name, *hobbies):
    print(f"Hello from {name}")
    print(f"My hobbies are {hobbies}")

greet("Alan", "music", "photography")
greet("Keith", "cycling", "drinking", "snooker")
greet("Billy No Mates")
# greet()#TypeError: greet() missing 1 required positional argument: 'name'

# what if we wish to pass named args, not positional?

def greet(name, *hobbies, **other_details):
    print(f"Hello from {name}")
    print(f"My hobbies are {hobbies}")
    print(f"I also have {other_details}")

greet("Alan", "music", "photography", county="Donegal", country="Ireland", eu_member = True)
greet("Keith", "cycling", "drinking", "snooker", city="Broxbourne", eu_member= False)
greet("Billy No Mates")
'''
so un-named args prefixed in the parameter list by a single *
are packed into a tuple
so named args prefixed in the parameter list by a name="value" *
are packed into a dictionary

the *args parameter MUST come AFTER any positional args
the **kwargs parameter list MUST come AFTER any *args
'''
# greet("music", "photography", county="Donegal", country="Ireland", eu_member = True, "Alan")#SyntaxError: positional argument follows keyword argument
# greet("Alan", county="Donegal", country="Ireland", eu_member = True, "music", "photography", )#SyntaxError: positional argument follows keyword argument


