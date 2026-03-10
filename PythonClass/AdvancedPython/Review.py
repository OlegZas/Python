#3/9/26
# Variable to track your progress and score you on this assignment. Run this cell first
total_score = 0

"""## Variable Definition"""

# Example problem:
# Uncomment the line below and run this cell.
# The hashtag "#" character in a line of Python code is the comment character.
doing_python_right_now = True

# The lines below will test your answer. If you see an error, then it means that your answer is incorrect or incomplete.
assert doing_python_right_now == True, "If you see a NameError, it means that the variable is not created and assigned a value. An 'Assertion Error' means that the value of the variable is incorrect."
print("Exercise 0 is correct") # This line will print if your solution passes the assertion above.

# Exercise 1
# On the line below, create a variable named on_mars_right_now and assign it the boolean value of False

on_mars_right_now = False
assert on_mars_right_now == False, "If you see a Name Error, be sure to create the variable and assign it a value."
print("Exercise 1 is correct.")
total_score += 1

# Exercise 2
# Create a variable named fruits and assign it a list of fruits containing the following fruit names as strings:
# mango, banana, guava, kiwi, and strawberry.

fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"], "If you see an Assert Error, ensure the variable contains all the strings in the provided order"
print("Exercise 2 is correct.")
total_score += 1

# Exercise 3
# Create a variable named numbers and assign it a list of numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Ensure the variable contains the numbers 1-10 in order."
print("Exercise 3 is correct.")
total_score += 1

"""## List Operations
**Hint** Recommend finding and using built-in Python functionality whenever possible.
"""

# Exercise 4
# Given the following assigment of the list of fruits, add "tomato" to the end of the list.
fruits = ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]




assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"], "Ensure the variable contains all the strings in the right order"
print("Exercise 4 is correct")
total_score += 1

# Exercise 5
# Given the list of numbers defined below, reverse the list of numbers that you created above.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()


assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Assert Error means that the answer is incorrect."
print("Exercise 5 is correct.")
total_score += 1

# Exercise 6
# Write the code necessary to sort the fruits in reverse alphabetical order
fruits = ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
fruits.sort(reverse=True)

assert fruits == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
print("Exercise 6 is correct.")
total_score += 1

# Exercise 7
# Write the code necessary to produce a single list that holds all fruits then all vegetables in the order as they were sorted above.
vegetables = ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
fruits = ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
fruits_and_veggies = fruits + vegetables


assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 7 is correct")
total_score += 1

"""## Basic Functions
![](http://)**Hint** Be sure to `return` values from your function definitions. The assert statements will call your function(s) for you.
"""

# Run this cell in order to generate some numbers to use in our functions after this.
import random

positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)

# Exercise 8
# Write a function definition for a function named add_one that takes in a number and returns that number plus one.
def add_one(num):
  return num+1

assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 8 is correct.")
total_score += 1

# Exercise 9
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.
def is_positive(num):
  if num > 0:
    return True
  else:
    return False



assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
print("Exercise 9 is correct.")
total_score += 1

# Exercise 10
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.
def is_odd(num):
  if num % 2 == 0:
    return False
  else:
    return True



assert is_odd(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 10 is correct.")
total_score += 1

# Exercise 11
# Write a function definition named is_positive_odd that takes in a number and returns True or False if the value is both greater than zero and odd
def is_positive_odd(num):
  if num % 2 != 0 and num > 0:
    return True
  else:
    return False

assert is_positive_odd(3) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_odd_number) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 11 is correct.")
total_score += 1

# Exercise 12
# Write a function definition named reverse_sign that takes in a number and returns the provided number but with the sign reversed.
def reverse_sign(num):
  return num *-1



assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5

print("Exercise 12 is correct.")
total_score += 1

# Exercise 13
# Write a function definition named absolute_value that takes in a number and returns the absolute value of the provided number
def absolute_value(num):
  return abs(num)



assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(positive_odd_number) == positive_odd_number
assert absolute_value(positive_even_number) == positive_even_number
assert absolute_value(negative_odd_number) == negative_odd_number * -1
assert absolute_value(negative_even_number) == negative_even_number * -1
print("Exercise 13 is correct.")
total_score += 1

# Exercise 14
# Write a function definition named is_multiple_of_both_three_and_five that takes in a number and returns True or False if the number is evenly divisible by both 3 and 5.
def is_multiple_of_both_three_and_five(num):
  if num % 3 == 0 and num % 5 == 0:
    return True
  else:
    return False



assert is_multiple_of_both_three_and_five(15) == True
assert is_multiple_of_both_three_and_five(45) == True
assert is_multiple_of_both_three_and_five(3) == False
assert is_multiple_of_both_three_and_five(9) == False
assert is_multiple_of_both_three_and_five(4) == False
print("Exercise 14 is correct.")
total_score += 1

# Exercise 15
# Write a function definition named add that takes in two numbers and returns the sum.

def add(num, num2):
  return num + num2



assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercise 15 is correct.")
total_score += 1

# Exercise 16
# Write a function definition named square_root that takes in a number and returns the square root of the provided number
import math
def square_root(num):
  return math.sqrt(num)



assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercise 16 is correct.")
total_score += 1

import math
# Exercise 17
# Write a function definition named area_of_circle that takes in a number representing a circle's radius and returns the area of the circl
def area_of_circle(num):
  return math.pi * (num ** 2)



assert area_of_circle(3) == 28.274333882308138
assert area_of_circle(5) == 78.53981633974483
assert area_of_circle(7) == 153.93804002589985
print("Exercise 17 is correct.")
total_score += 1
