"""
Perform Each math operations you have been shown (store the result in a variable) and print the result to the screen.

Write a comment above each variable describing what the math operation does
"""

# Author: Emma Sun
# Date Modified: 2025/02/25
# Description: Perform math operations and print results; describe operation in comments.

import math
import time

addition = 2+3  # addition/"+" finds the sum of the numbers.
subtraction = 10-4  # subtraction/"-" finds the difference of the numbers.
multiplication = 5*4  # multiplication/"*" finds the product of the numbers.
division = 8/2  # division/"/" finds the quotient of the numbers.
modulus = 45%6  # modulus/"%" finds the remainder after dividing the numbers.
exponent = 3**3  # exponent/"**" multiplies the first number by itself [second number] amount of times.
squareRoot = math.sqrt(25)  # finds the square root of the number.

# These are the print statements .
print("These are some basic math operations!")
time.sleep(1.5)
print(f"2+3 is equal to {addition}! This is addition.")
time.sleep(1.5)
print(f"10-4 is equal to {subtraction}! This is subtraction.")
time.sleep(1.5)
print(f"5x4 is equal to {multiplication}! This is multiplication.")
time.sleep(1.5)
print(f"8÷2 is equal to {division}! This is division.")
time.sleep(1.5)
print(f"The remainder of 45/6 is {modulus}! This is modulus.")
time.sleep(1.5)
print(f"3³ is equal to {exponent}! This is exponentiation.")
time.sleep(1.5)
print(f"√25 is equal to {squareRoot}! This is square root.")
time.sleep(1.5)
print("The end!")