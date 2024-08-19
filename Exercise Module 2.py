
from random import randint

# 1st question
name = input("What is your name? ")
print(f"Hello, {name}!")

# 2nd question
radius = float(input("What is the radius? "))
area = radius*radius*3.14
print(f"The area is {area}.")

# 3rd question
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
rectangleArea = length*width
rectanglePerimeter = 2*(length+width)
print(f"The perimeter is {rectanglePerimeter} and the area is {rectangleArea}.")

# 4th question
number1 = int(input("What is the first integer number? "))
number2 = int(input("What is the second integer number? "))
number3 = int(input("What is the third integer number? "))
sumNumber = number1 + number2 + number3
product = number1 * number2 * number3
average = sumNumber/3
print(f"Sum is {sumNumber}.")
print(f"Product is {product}.")
print(f"Average is {average}.")

# 5th question
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

weightInGam = ((((talents*20)+pounds)*32)+lots)*13.3
print("The weight in modern units:")
print(f"{weightInGam//1000:.0f} kilograms and {weightInGam%1000:.2f} grams.")

# 6th question
number1_code1 = randint(0,9)
number2_code1 = randint(0,9)
number3_code1 = randint(0,9)
print(f"Fist lock code is {number1_code1}{number2_code1}{number3_code1}.")

number1_code2 = randint(1,6)
number2_code2 = randint(1,6)
number3_code2 = randint(1,6)
number4_code2 = randint(1,6)
print(f"Second lock code is {number1_code2}{number2_code2}{number3_code2}{number4_code2}.")
