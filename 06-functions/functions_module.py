'''
a module is a Python script that contains only a mix of:
functions,
variables,
and classes
These may be called from a runtime that would then be uncoupled from the declarations
'''
def add(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        return None
    # print(type(num1))
    # print(type(num2))

# print(add(1,1))
# print(add("x",1))

def sub(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 - num2
    else:
        return None
    
def mul(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 * num2
    else:
        return None
    
def div(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 / num2
    else:
        return None
    
# generally, there is no runtime code here
# HOWEVER if you want to run stuff here, we do this:
if __name__ == '__main__':
    print("You only see me if you run the module")
    print(add(1,1))
    print(add("x",1))