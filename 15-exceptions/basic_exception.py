'''handling basic exceptions'''
# from a user POV, exception handling enables the code to recover and carry on from a catastrophic failure
# from a dev POV, it enables us to create and raise errors, preventing certian for completing, according to business logic
try:
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter a number:"))
    total = num1 + num2
    print(f"sum of {num1} and {num2} is {total}")
except:
    print("ERROR: something went wrong")

print("Carrying on...")#unreachable unless exception handled