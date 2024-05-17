'''handling specific exceptions'''
try:
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter a number:"))
    total = num1 / num2
    print(f"sum of {num1} and {num2} is {total}")
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")
except:
    print("ERROR: something went wrong")
else: #if no errors, code will run here (like after a for loop runs to completion)
    # put code here intended to run ONLY if normal execution, no exceptions
    print(f'{num1} / {num2} = {total}')
finally:
    # put code here intended to run EITHER if normal execution, OR exceptions caught
    # for instance, closing a database connection
    print("thankyou and goodbye")


# ValueError: could not convert string to float: 'two'
# ZeroDivisionError: float division by zero