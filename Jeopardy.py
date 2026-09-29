import random
money=0
print("THIS\nIS\nJEOPARDY!\nYour first question...\n")
Dict = {
    "Olympus Mons, the largest volcano in our solar system, can be found on this planet, named for the Roman god of war.": "Mars",
    "This South American civilization built Machu Picchu, but its empire fell to Spanish conquistadors in the 1500s.": "Inca",
    "Ag is the chemical symbol for this precious metal, whose name comes from the Latin word argentum.": "Silver",
    "Before Pennsylvania, New Jersey, and Georgia could join the Union, this state became the first to ratify the U.S. Constitution.": "Delaware",
    "Making up about 84% of Earth's volume, this layer lies between the crust and the outer core.": "Mantle",
    "After supposedly watching an apple fall, this English scientist developed laws describing both motion and gravity.": "Issac Newton",
    "Covering more of Earth's surface than all the continents combined, this is the largest of the world's oceans.": "Pacific Ocean",
    "Located behind the stomach, this organ has an important role in both digestion and controlling blood sugar.": "Pancreas",
    "'That's one small step for man...' was spoken during this 1969 NASA mission.": "Apollo 11",
    "Beginning in Peru and eventually reaching the Atlantic, this South American river carries more water than any other river on Earth.": "Amazon River",
    "'To be, or not to be' is the famous question asked by the title character of this Shakespeare tragedy.": "Hamlet",
    "If you're looking for the smallest prime number greater than 10, look no further than this number.": "11",
    "Nicknamed the 'universal donor' for red blood cell transfusions, this blood type lacks A, B, and Rh antigens.": "O Negative",
    "'We the People' are the first three words of this foundational U.S. document.": "Constitution",
    "With six protons and usually six neutrons, this element is the fourth-most abundant element in the universe.": "Carbon",
    "Swirling stars over a quiet village appear in this famous painting by a Dutch artist who also created Sunflowers.": "Starry Night",
    "In geometry, this irrational number is essential for calculating the circumference and area of a circle": "Pi",
    "Making up about 78% of Earth's atmosphere, this element is essential for proteins and DNA.": "Nitrogen"
}

one=random.choice(list(Dict.keys()))

onea=input(f"{one} ")

if onea == Dict[one]:
    print("Nice Job, you made $100\nYour second question...")
    money += 100
else:
    print(f"Incorrect, the answer was {Dict[one]}\nYour second question...")
Dict.pop(one)



two=random.choice(list(Dict.keys()))

twoa=input(f"{two} ")

if twoa == Dict[two]:
    print("Nice Job, you made $200\nYour third question...")
    money += 200
else:
    print(f"Incorrect, the answer was {Dict[two]}\nYour third question...")
Dict.pop(two)



three=random.choice(list(Dict.keys()))

threea=input(f"{three} ")

if threea == Dict[three]:
    print("Nice Job, you made $300\nYour fourth question...")
    money += 300
else:
    print(f"Incorrect, the answer was {Dict[three]}\nYour fourth question...")
Dict.pop(three)



four=random.choice(list(Dict.keys()))

foura=input(f"{four} ")

if foura == Dict[four]:
    print("Nice Job, you made $400\nYour fifth question...")
    money += 400
else:
    print(f"Incorrect, the answer was {Dict[four]}\nYour fifth question...")
Dict.pop(four)



five=random.choice(list(Dict.keys()))

fivea=input(f"{five} ")

if fivea == Dict[five]:
    print("Nice Job, you made $400")
    money += 400
else:
    print(f"Incorrect, the answer was {Dict[five]}")
Dict.pop(five)
print(f"Your total bank was ${money}\nThanks for Playing!")