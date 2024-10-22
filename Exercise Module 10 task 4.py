import random

#Class
class Car:
    def __init__(self, reg_num, max_speed: int, current_speed = 0, distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance
    def accelerated(self,change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
    def print_speed(self):
        print(f"The current speed of car with registration number {self.reg_num} is {self.current_speed}")
    def drive(self,hours: int):
        add_distance = self.current_speed * hours
        self.distance = self.distance + add_distance
        #print(f"The travelled distance now is {self.distance}.")

class Race():
    def __init__(self,name, distance_in_km: int, carlist: list):
        self.name = name
        self.distance_in_km = distance_in_km
        self.carlist = carlist
    def hour_passes(self):
        for car in self.carlist:
            car.accelerated(random.randint(-10, 15))
            car.drive(1)
    def print_status(self):
        self.sorted_carlist = sorted(self.carlist, key=lambda car: car.distance,reverse=True)
        print("")
        print("---------------------------------------------------------------------------------")
        print(f"\t{"Register Number":<14}\t|\t{"Max Speed":<12}\t|\t{"Current Speed":<15}\t|\t{"Current Distance":<16}")
        print("---------------------------------------------------------------------------------")
        for car in self.sorted_carlist:
            print(
                f"|\t\t{car.reg_num:<10}\t|\t\t{car.max_speed:<8}\t|\t\t{car.current_speed:<11}\t|\t\t{car.distance:<11}\t|")
        print("---------------------------------------------------------------------------------")
    def race_finished(self):
        for car in self.carlist:
            if car.distance >= self.distance_in_km:
                return True
# Main program
if __name__ == "__main__":
    # Car Race
    cars = []
    for i in range(1,11):
        car = Car(f"ABC-{i}", random.randint(100, 200))
        cars.append(car)
race = Race("Grand Demolition Derby",8000,cars)

while True:
    for i in range (10):
        race.race_finished()
        if race.race_finished() == True:
            break
        else:
            race.hour_passes()
    race.print_status()
    if race.race_finished() == True:
        break
print(f"The Race has finnished! The winner is car {race.sorted_carlist[0].reg_num}")


