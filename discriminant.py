# Author: Emma Sun
# Date modified: 2025/02/26
# Description: Find the discriminant and deteremine the number of real solutions.

import time

# Explains what the discriminant does and how to input values.
print("""Let's find the discriminant!
The discriminant tells us how many real solutions there are: one, two, or none.
It takes values from an equation in the form ax^2+bx+c.
When asked, input your value for each varible, then press Enter.
""")
time.sleep(3)

# user inputs values for a, b, and c.
a = float(input("What is your a value?\n"))
time.sleep(1)
b = float(input("What is your b value?\n"))
time.sleep(1)
c = float(input("What is your c value?\n"))
time.sleep(1)

discriminant = float(b**2-4*a*c) # Calculates discriminant
print(f"The discriminant is {discriminant}.") # Tells user what the discriminant is

# Tells user how many real solutions there are based on the discriminant.
if discriminant > 0:
    print("There are two real solutions!")
elif discriminant == 0:
    print("There is one real solution!")
elif discriminant < 0:
    print("There are no real solutions!")