#task 1
season = ("spring","summer","autumn","winter")

month_input = int(input("Enter a month number: "))
if month_input in (12,1,2):
    print(f"You are enter a month in {season[3]}")
elif month_input in (3,4,5):
    print(f"You are enter a month in {season[0]}")
elif month_input in (6,7,8):
    print(f"You are enter a month in {season[1]}")
elif month_input in (9,10,11):
    print(f"You are enter a month in {season[2]}")
else:
    print("You are enter an invalid month number!")

#task 2
name_set = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        print("Stop adding name!")
        break
    else:
        if name not in name_set:
            print("New name.")
            name_set.add(name)
            print(f"{name} added to the list.")
        else:
            print("Existing name.")
print("Your name list is:")
for i in name_set:
    print(i)

#task 3
airport_data = {}
while True:
    choice = int(input("Enter a number to choose your option:\n\
    1. Enter a new airport.\n\
    2. Fetch an existing airport.\n\
    3. Quit\n\
    Your choice: "))
    if choice == 1:
        airport_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[airport_code] = airport_name
    if choice == 2:
        user_code = input("Enter the ICAO code of the airport you want to fetch: ")
        print(f"The airport with ICAO code {user_code} is: {airport_data[user_code]}")
    if choice == 3:
        print("The program ends here!")
        break






