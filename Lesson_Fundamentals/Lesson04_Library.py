# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(4.8)
print(f"Round down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANTS are variables that NEVER change. They are written in ALL CAPS
PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2
diameter=14
radius = diameter / 2
circle_area = (radius ** 2) * PI
print(f"The area of the circle is {circle_area}")

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator 

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.00. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

seed = 22
seed1=(seed*2) + (seed**(seed-4))
seed2=(seed1+seed1)/seed
seed3=math.ceil(seed2)
print(seed2)

# Change the seed, get a new, pseudorandom number

# for s in range(5):

#     step1 = seed / 6.7
#     # print(step1)
#     step2 = step1 - 800.33
#     # print(step2)
#     step3 = step2 ** 3 
#     # print(step3)
#     round_up = math.ceil(step3)  
#     result = round_up % 10 # remainder between 0 and 6 (never 6)
#     print("Your random num is:", result)

#     seed = seed * 3 

# Pythons random library 

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]

random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it with a message.

die_roll=random.randint(1, 6)
print(f"Your random 6 sided dice result is {die_roll}")

# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with the math library.

num=random.randint(1, 75)
sqrt=math.sqrt(num)
round=math.ceil(sqrt)
print(f"Number:{num}\nSquare Root:{sqrt}\nRounded Square Root:{round}")
# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, base to the POWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).
base=int(random.randint(1, 6))
exponent=int(random.randint(1,6))
result=int(base**exponent)
print(f"Number:{base}\nExponent:{exponent}\nResult:{result}")