# USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---")

# Basic text input
name = input("Enter your name: ")
print("Hello,", name)

# Input is always stored as a string, even if you type a number
age = input("Enter your age: ")
print("You said your age is:", age, "(type:", type(age), ")")

# To use numbers, we must cast (convert) the string to int or float
age_number = int(age)
print("Next year, you will be:", age_number + 1)

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# ---------------------------------------------------------
# CHALLENGES
# ---------------------------------------------------------

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.
color=input("Whats your favorite color: ")
print(f"Your favorite color is {color}.")
# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.
a=int(input("First Number: "))
b=int(input("Second Number: "))
result=a+b
print(f"Result: {result}")
# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
dia=int(input("Whats the diamiter of the circle? "))
rad=dia/2
area=3.14*(rad**2)
print(f"The area of the circle is {area}")
# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
import random
a=int(input("How many sides does the die have? "))
result=random.randint(0, a)
print(f"The result is {result}")