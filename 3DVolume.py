"""
3D Volume
Write a program that calculates the volume o of the three-dimensional shapes mentioned to the right. It should take as input the parameter(s) necessary to calculate the volume (A, r , h ). You should take in each variable you need in turn. Ie. for the cube, take in the length, for the sphere, take in the radius, etc…

The output should be USER FRIENDLY.
"""

# Author: Emma Sun
# Date modified: 2025/02/27
# Description: Calculates volume of a 3D shape with the values that the user provides.

import math
import time

# instructions for user
print("""
Let's find the volume of 3D shapes!
Enter the values (height, length, or radius depending on the shape) for your cube, sphere, cone, or cylinder, then press enter.
""")
time.sleep(3)

# asks user which shape they are calculating the volume for
shape = input("For which shape are you finding the volume?\n")
shape = shape.lower()

# questions and calculations depending on which shape the user chooses
if "cube" in shape:
      print("Great, we're going to calculate the volume of a cube!")
      time.sleep(1.5)
      l = float(input("What is the side length of your cube?\n"))
      v = l**3
      print(f"The volume of your cube is {v}!")
elif "sphere" in shape:
      print("Great, we're going to calculate the volume of a sphere!")
      time.sleep(1.5)
      r = float(input("What is the radius of your sphere?\n"))
      v = round(4/3*math.pi*r**3)
      print(f"The volume of your sphere is ~{v}!")
elif "cone" in shape:
      print("Great, we're going to calculate the volume of a cone!")
      time.sleep(1.5)
      r = float(input("What is the radius of the base of your cone?\n"))
      h = float(input("What is the height of your cone?\n"))
      v = round(1/3*math.pi*r**2*h)
      print(f"The volume of your cone is ~{v}!")
elif "cylinder" in shape:
      print("Great, we're going to calculate the volume of a cylinder!")
      time.sleep(1.5)
      r = float(input("What is the radius of the base of your cylinder?\n"))
      h = float(input("What is the height of your cylinder?\n"))
      v = round(math.pi*r**2*h)
      print(f"The volume of your cone is ~{v}!")
else:
      print("I don't know that shape yet!")