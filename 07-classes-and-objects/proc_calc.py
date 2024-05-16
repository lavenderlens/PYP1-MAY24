total = 0

def add(num):
    global total
    total += num

def subtract(num):
    global total
    total -= num

def multiply(num):
    global total
    total *= num

def divide(num):
    global total
    total /= num

def equals():
    global total
    return_value = total
    total = 0
    return return_value
