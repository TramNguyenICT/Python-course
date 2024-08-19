#1st question
lengthOfZander = float(input("What is the length of Zander? "))
if lengthOfZander < 42:
    print("Release the fish back to the lake.")
    print(f"The fish needs to be {42-lengthOfZander} centimeters longer. ")
else:
    print("Your fish meets the size limit, let's collect it.")
#2nd question
classType = input("What is the type of your cabin class? ")
if classType == "LUX":
    print("It is upper-deck cabin with a balcony.")
elif classType == "A":
    print("It is above the car deck, equipped with a window.")
elif classType == "B":
    print("It is the windowless cabin above the car deck.")
elif classType == "C":
    print("It is the windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#3rd question
gender = input("What is your biological gender? ")
hemoglobinValue = float(input("What is your hemoglobin value? "))
if gender == "Female" or gender == "female" or gender == "F" or gender == "f":
    if hemoglobinValue < 118:
        print("Your hemoglobin value is low.")
    elif 118 <= hemoglobinValue <= 155:
        print("Your hemoglobin value is normal.")
    elif hemoglobinValue > 155:
        print("Your hemoglobin value is high.")
    else:
        print("You enter an invalid value.")
elif gender == "Male" or gender == "male" or gender == "M" or gender == "m":
    if hemoglobinValue < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobinValue <= 167:
        print("Your hemoglobin value is normal.")
    elif hemoglobinValue > 167:
        print("Your hemoglobin value is high.")
    else:
        print("You enter an invalid value.")
else:
    print("You enter an invalid gender, it must be Male or Female")

#4th question
year = int(input("Enter a year: "))
if year%100 == 0:
    if year%400 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
elif year%4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")