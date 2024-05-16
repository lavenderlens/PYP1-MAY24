class Calculator:
    # the global procedural variable is STATE
    # state becomes the object propin __init__
    def __init__(self) :
        self.total = 0
        
    def add(self, num):
        self.total += num

    def subtract(self, num):
        self.total -= num

    def multiply(self, num):
        self.total *= num

    def divide(self, num):
        # problem: divide by zero
        self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value