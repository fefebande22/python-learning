import random
def dice_roll():
    total = 0
    operator = input("what type of dice would you like to roll (D4, D6, D12, D20, D100)? ")
    roll_amount = (int(input("how many times would you like me to roll this dice? ")))
    for counter in range(roll_amount):
        if operator.upper() == ("D6"):
            num = random.randint(1,6)
        elif operator == ("none"):
            print("ok")
        elif operator.upper() == ("D4"):
            num = random.randint(1,4)
        elif operator.upper() == ("D12"):
            num = random.randint(1,12)
        elif operator.upper() == ("D20"):
            num = random.randint(1,20)
        elif operator.upper() == ("D100"):
            num = random.randint(1,100)
        else:
            print("Try again")
    
        total = num + total
    return total

number = dice_roll()

print()
print(number)
