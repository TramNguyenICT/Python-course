import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flightgame',
    user = 'root',
    password = '180790',
    autocommit = True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci',
)


# Task 1
user_ICAO = input("Enter the ICAO code of the airport: ")

sql1 = f"SELECT name, municipality FROM airport WHERE ident = '{user_ICAO}'"
cursor = connection.cursor()
cursor.execute(sql1)
result1 = cursor.fetchall()
print(result1)

# Task 2
user_area_code = input("Enter the area code of the airport: ")

sql2 = f"SELECT name FROM airport WHERE iso_country = '{user_area_code}' ORDER BY type ASC"
cursor.execute(sql2)
result2 = cursor.fetchall()
for result in result2:
    print(result)

# Task 3
user_ICAO_1 = input("Enter the ICAO codes of the first airports: ")
user_ICAO_2 = input("Enter the ICAO codes of the second airports: ")

def get_deg_airport(ident):
    result3 = list()
    sql3 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}'"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    return result3

first_airport = get_deg_airport(user_ICAO_1)
second_airport = get_deg_airport(user_ICAO_2)
print(f"The distance between 2 airports is {(distance.distance(first_airport, second_airport).km):.2f} km")
