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
      l = float(input("What is the side length of your cube?\n")) # user inputs side length
      v = l**3 # calculates volume of cube
      print(f"The volume of your cube is {v}!") # prints volume of sphere
elif "sphere" in shape:
      print("Great, we're going to calculate the volume of a sphere!")
      time.sleep(1.5)
      r = float(input("What is the radius of your sphere?\n")) # user inputs radius
      v = round(4/3*math.pi*r**3) # calculates volume of sphere
      print(f"The volume of your sphere is ~{v}!") # prints volume of sphere
elif "cone" in shape:
      print("Great, we're going to calculate the volume of a cone!")
      time.sleep(1.5)
      r = float(input("What is the radius of the base of your cone?\n")) # user inputs radius
      h = float(input("What is the height of your cone?\n")) # user inputs height
      v = round(1/3*math.pi*r**2*h) # calculates volume of cone
      print(f"The volume of your cone is ~{v}!") # prints volume of cone
elif "cylinder" in shape:
      print("Great, we're going to calculate the volume of a cylinder!")
      time.sleep(1.5)
      r = float(input("What is the radius of the base of your cylinder?\n")) # user inputs radius
      h = float(input("What is the height of your cylinder?\n")) # user inputs height
      v = round(math.pi*r**2*h) # calculates volume of cylinder
      print(f"The volume of your cone is ~{v}!") # prints volume of cylinder
else: # print if user enters something that isn't one of the given shapes
      print("I don't know that shape yet!")