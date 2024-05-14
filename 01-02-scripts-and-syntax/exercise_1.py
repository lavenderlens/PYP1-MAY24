print("Enter your name")
user_name = input()
print("Enter your age")
user_age = input()
# print("Name:", user_name, "Age next birthday:", user_age + 1) #TypeError: can only concatenate str (not "int") to str
print(type(user_name)) #<class 'str'>
print(type(user_age)) #<class 'str'>
# this is because the input() function always returns a string (str)

name = "Alan"
age = 57 # the data type is taken from the data
print("Name:", name, "Age next birthday:", age + 1)

# to get the input() function behaving like hardcoded variables we need to coerce data type
print("Enter your name")
name = input()
print("Enter your age")
age = input()
age = int(age)
print("Name:", name, "Age next birthday:", age + 1)#works
# but ONLY works because commas let you print out separate things

# print("Name: " + name + "\nAge next birthday:" + (age + 1))#as ONE string?
# TypeError: can only concatenate str (not "int") to str

print("Name: " + name + "\nAge next birthday:" + str(age + 1))#works, by concatenation (Python 3 <)

# placeholders, Python 3>
print("Using Python 3 > placeholders")
print("Name: {} \nAge next birthday: {}".format(name, age + 1))#placeholders must be same order, same number

# placeholders with f-strings, Python 3.5 >
print("Using Python 3.5 > placeholders with f-strings")
print(f"Name: {name} \nAge next birthday: {age + 1}")# the modern way

# placeholders with triple-quoted f-strings, Python 3.7 >
print("Using Python 3.7 > placeholders with triple-quoted f-strings")
print(f"""
Name: {name} 
Age next birthday: {age + 1}
""")# the ultra-modern way, preserves line breaks

