#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 7 / 2
print("Float division:", float_divide)

integer_divide = 7 // 2
print("Integer division:", integer_divide)

mod = 7 % 2
print("Modulus: ", mod) 

exponent = 7 ** 2
print("Exponent:", exponent)

#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
width=8
height=5
area=width * height
print(area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.) 
r=7
pi=3.14
area = pi * r ** 2
print(area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
books=3
notebooks=4
bookc=12.99
cbook=bookc * books
notebookc=3.5
cnotebook=notebookc * notebooks
print(f"Book: ${cbook}\nNotebook: ${cnotebook}\nTotal: ${cnotebook+cbook}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
num=57
rem=num%2
if rem==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

