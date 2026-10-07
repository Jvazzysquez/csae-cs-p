# print("PRE GAME QUESTIONS\n".center(128))
# name=input("What is your name? ")
# age=int(input("How old are you? "))
# if age > 30:
#     uncstatus=True
# else:
#     uncstatus=False
health=100
weapons=["Sword"]
def inventory():
    print("STATS".center(128))
    print(f"Health:{health}\nWeapons:{weapons}")
    wantstat=input("Would you like to see weapon stats? "
inventory()