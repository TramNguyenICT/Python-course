import random
# 1st task
number = 0
while number<= 1000:
    number = number + 1
    if number % 3 == 0:
        print(number)

#2nd task
valueInInches = float(input("Enter the value in inches: "))
while valueInInches > 0:
    valueInCentimeters = valueInInches * 0.39370
    print(f"Value in centimeters is: {valueInCentimeters}")
    valueInInches = float(input("Enter the value in inches: "))

#3rd task
smallest = largest = None
while True:
    userInput = input("Enter a number (or an empty string to stop): ")
    if userInput == "":
        break
    try:
        userNumberInFloat = float(userInput)
        if smallest is None or userNumberInFloat <= smallest:
            smallest = userNumberInFloat
        if largest is None or userNumberInFloat >= largest:
            largest = userNumberInFloat
    except ValueError:
        print("You have enter an invalid value, only numbers or empty string are accepted")
print("Smallest number: ", smallest)
print("Largest number: ", largest)


#4th task
result = random.randint(1, 10)
while True:
    userGuess = int(input("Enter a number between 1 and 10: "))
    if userGuess == result:
        print("Correct")
        break
    elif userGuess < result:
        print("Too low")
    else:
        print("Too high")

#5th task
username = "python"
password = "rules"
loginSuccessful = False
i = 0
while i < 5:
    usernameInput = input("Enter a username: ")
    passwordInput = input("Enter a password: ")
    if usernameInput == username and passwordInput == password:
        print("Welcome!")
        loginSuccessful = True
        break
    elif usernameInput != username and passwordInput != password:
        print("The username and password did not match. Try again.")
    i += 1

if not loginSuccessful:
    print("Access denied")

#6th task
import random

randomPoints = int(input("How many random points to generate? "))
i = 0
pointsInsideCircle = 0
while i < randomPoints:
    xValue = random.uniform(-1, 1)
    yValue = random.uniform(-1, 1)
    if xValue**2 + yValue** 2 < 1:
        pointsInsideCircle += 1
    i+=1
print(f"Approximation of pi is {4*(pointsInsideCircle/randomPoints)}")

