name = input("Please type in a name: ")
year = int(input("Please type in a year: "))
print(f"{name} is a valiant knight, born in the year {year}. One \nmorning {name} woke up in an awful racket: a dragon \n was approaching the village. Only {name} could save \n the village's residents.")

numberOfDays = int(input("How many days? "))
print("Second in that many days:", numberOfDays*86400)

times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
moneyOnGroceries = float(input("How much money do you spend on groceries in a week? "))
print("Average food expenditure:")
moneyAWeek = times*price + moneyOnGroceries
print("Daily: " + str(moneyAWeek/7))
print("Weekly: " + str(moneyAWeek))