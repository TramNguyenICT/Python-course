import random

# Task 1

diceNumber = int(input("How many dice to roll? "))
diceSum = 0
for i in range(1,diceNumber+1):
    dice = random.randint(1,6)
    print("Try",i,": dice is", dice)
    diceSum += dice

print("The sum of all the dice is",diceSum)

# Task 2
# 1. Using while-loop
numberList = list()
while True:
    userinput = input("Enter a number (or an empty string to stop): ")
    if userinput == "":
        break
    try:
        numberList.append(int(userinput))
    except ValueError:
        print("You have to enter a number or an empty string!")
numberList.sort(reverse = True)
print(f"Five greatest numbers are {numberList[0:5]}")
# 2. Using for-loop
numberList = list()
for userinput in iter(lambda: input("Enter a number (or an empty string to stop): "), ""):
    if userinput == "":
        break
    try:
        numberList.append(int(userinput))
    except ValueError:
        print("You have to enter a number or an empty string!")
numberList.sort(reverse=True)
print(f"Five greatest numbers are {numberList[0:5]}")

# Task 3
userInt = int(input("Enter an integer number: "))
primeNumber = True
for i in range(2,userInt):
    if userInt % i == 0:
        primeNumber = False
if primeNumber is True:
    print("Your number is a prime number")
else:
    print("Your number is not a prime number")

# Task 4
citiesList = list()
for i in range(5):
    userCity = input("Enter a city: ")
    citiesList.append(userCity)
for j in citiesList:
    print(j)
