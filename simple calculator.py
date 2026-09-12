operator = (input("what operator would you like? (+, -, /, *, %) "))
if operator == ("+"):
    num1 = (float(input("what is your number? ")))
    num2 = (float(input("what would you like to add to that number? ")))
    print("your total is:")
    print(num1 + num2)
elif operator == ("-") :
    num1 = (float(input("what is your number? ")))
    num2 = (float(input("what would you like to subtract from that number? ")))
    print("your total is:")
    print(num1 - num2)
elif operator == ("/") :
    num1 = (float(input("what is your number? ")))
    num2 = (float(input("what would you like to divide from that number? ")))
    print("your total is:")
    print(num1 / num2)
elif operator == ("*") :
    num1 = (float(input("what is your number? ")))
    num2 = (float(input("what would you like to multiply that number by? ")))
    print("your total is:")
    print(num1 * num2)
elif operator == ("%") :
    num1 = (float(input("what is your number? ")))
    num2 = (float(input("what percentage of that number would you like? ")))
    print("your total is:")
    print(num1 * (num2 / 100))
answer = input("was I correct? ")
if answer == ("yes"):
    print("thank you")
elif answer == ("no"):
    print("dang")
else:
    print("I don't understand, try again later")
