#CHAL:1
bill = 50
tip = 0.2*bill
print(f"Bill:{bill}\nTip:{tip}")

#CHAL:2
import math
students = 23
slices_per_student = 2
slices_per_pizza = 8
tot=slices_per_student*students
pizza=math.ceil(tot/slices_per_pizza)
left=tot%slices_per_pizza
print(f"Pizzas:{pizza}\nLeftover slices:{left}")

#CHAL:3
fahrenheit=212
c = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} degrees fahrenheit is {c} degrees celsius.")

#CHAL:4
score=84
if score>=90:
    print("You got an A")
elif score>=80:
    print("You got an B")
elif score>=70:
    print("You got an C")
elif score>=60:
    print("You got an D")
elif score<=59:
    print("You got an F")

#CHAL:5
password = "csaea2026"
attempt = "CSAEA2026"
if password==attempt:
    print("Access Granted")
else:
    print("Access Denied")

#CHAL:6
plate = 4827
cho=plate%2
if cho==1:
    print("Park on the west side")
else:
    print("Paek on the east side")

#CHAL:7
height = 50
age = 8
has_adult = True
if height>=48 and age>=10:
    print("You can ride")
elif has_adult==True:
    print("You can ride.")
else:
    print("You can't ride.")

#CHAL:8
first = "Ada"
last = "Lovelace"
school = "CSAEA"
print(f"Hello, my name is {first} {last} from {school}")

#CHAL:10
start = 10
print()
