class Calculator:
    # Constructor to initialize attributes
    def __init__(self, number):
        self.number = number
    
    # Method to add a value to the number
    def add(self, value):
        self.number += value
        return self.number

    # Method to multiply the number
    def multiply(self, value):
        self.number *= value
        return self.number

# Creating an object
calc = Calculator(10)  # Constructor called with number = 10

# Using methods
print(calc.add(5))       # Output: 15 (10 + 5)
print(calc.multiply(3))  # Output: 45 (15 * 3)


class Calculator:
    def __init__(self, number):
        self.number = number
        print(self.number)
        

# Object তৈরি হলে constructor call হবে
calc = Calculator(10)  # Constructor is called
print(calc.number)