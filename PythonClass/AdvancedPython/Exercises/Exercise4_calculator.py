''' Exercise 4
In the spece below encode a series of math functions detailed below,
then copy them into a separate IDE to create a calculator.py program.

This program should contain a series of basic arithmatic functions for two numbers.

Specifically:
- 'add' should add two numbers and return the result
- 'subtract' should subtract the second number from the first and returns the result
- 'multiply' multiplies the two numbers together and returns the result
- 'divide' will divide the first number by the second and return the result.
    For this function if the second number is 0 instead return:
    "Error: Division by zero!"

Load this file into the session storage and run the code below to validate that
the module is being imported properly.

'''
#calculator.py functions start here:
#add()
def add(a, b):
    return a + b

#subtract()
def subtract(a, b):
    return a - b

#multiply()
def multiply(a, b):
    return a * b

#divide()
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


# main.py
import calculator

assert calculator.add(4, 5) == 9
assert calculator.subtract(8, 5) == 3
assert calculator.multiply(-2, 5) == -10
assert calculator.divide(20, 5) == 4
assert calculator.divide(20, 0) == "Error: Division by zero!"

print("Exercise 4 is correct.")
total_score += 5
