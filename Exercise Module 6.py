import random

# Task 1
def random_dice():
    value = random.randint(1,6)
    return value

while True:
    diceNumber = random_dice()
    if diceNumber == 6:
        print(f"Result of dice roll is {diceNumber}. Stop rolling here!")
        break
    print(f"Result of dice roll is {diceNumber}")

# Task 2
def random_dice_2(numberofsides):
    value = random.randint(1,numberofsides)
    return value

sidesFromUser = int(input("Enter the number of sides of the dice you would like to roll: "))
while True:
    diceNumber = random_dice_2(sidesFromUser)
    if diceNumber == sidesFromUser:
        print(f"Result of dice roll is {diceNumber}. Stop rolling here!")
        break
    print(f"Result of dice roll is {diceNumber}")

# Task 3
def convert_gallons_to_liters(gallons_value):
    liters_value = gallons_value * 3.78541178
    return liters_value
while True:
    gallonsInput = float(input("Enter the number of gallons (enter an negative value to quit): "))
    if gallonsInput < 0:
        break
    try:
        literValue = convert_gallons_to_liters(gallonsInput)
        print(f"The value in liter unit is {literValue}")
    except ValueError:
        print("You entered an invalid value. Please enter a value.")

# Task 4
def sum_integer(integer_list):
    sum_value = 0
    for i in integer_list:
        sum_value += i
    return sum_value
input_list = list()
while True:
    integer_input = input("Enter an integer (enter an empty string to quit): ")
    if integer_input == "":
        break
    else:
        try:
            integer_input_in_int = int(integer_input)
            input_list.append(integer_input_in_int)
        except ValueError:
            print("You entered an invalid value. Please enter an integer or an empty string.")

result = sum_integer(input_list)
print(f"The sum of all integers entered is {result}")

# Task 5
def relist(integer_list):
    new_list = list()
    for i in integer_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

user_list = list()
while True:
    user_list_input = input("Enter an integer number to add it to list (or an empty string to stop): ")
    if user_list_input == "":
        break
    else:
        try:
            user_list_input_in_int = int(user_list_input)
            user_list.append(user_list_input_in_int)
        except ValueError:
            print("You entered an invalid value. Please enter an integer or an empty string.")

even_list = relist(user_list)
print(f"Your original list is: {user_list}")
print(f"New list with all even integer is: {even_list}")

# Task 6
def pizza_unit_price_calculate(diameter, price):
    diameter_in_meter = diameter * 0.01
    pizza_area = 3.14 * ((diameter_in_meter/2)**2)
    unit_price = price/pizza_area
    return unit_price

pizza_diameter1 = float(input("Enter the diameter of the 1st pizza (in centimeters): "))
pizza_diameter2 = float(input("Enter the diameter of the 2nd pizza (in centimeters): "))
price1 = float(input("Enter the price of the 1st pizza: "))
price2 = float(input("Enter the price of the 2nd pizza: "))
unit_price1 = pizza_unit_price_calculate(price1,pizza_diameter1)
unit_price2 = pizza_unit_price_calculate(price2,pizza_diameter2)
if unit_price1 < unit_price2:
    print(f"Your 1st pizza provides better value for money! ({unit_price1:.2f} euros per meter compare to {unit_price2:.2f} euros per meter)")
elif unit_price2 < unit_price1:
    print(f"Your 2nd pizza provides better value for money! ({unit_price2:.2f} euros per meter compare to {unit_price1:.2f} euros per meter)")
else:
    print("Both of your two pizza values are equal!")