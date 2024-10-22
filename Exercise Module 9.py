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

# Main program
car = Car("ABC-123", 142)
print(f"Car with registration number {car.reg_num} has the max speed of {car.max_speed}, current speed: {car.current_speed}, travelled disctance: {car.distance}.")
car.accelerated(30)
car.accelerated(70)
car.accelerated(50)
car.print_speed()
car.accelerated(-200)
car.print_speed()

# Car Race
cars = []
for i in range (10):
    car = Car(f"ABC-{i}",random.randint(100,200))
    cars.append(car)

max_distance = 0
while max_distance < 10000:
    for car in cars:
        car.accelerated(random.randint(-10,15))
        car.drive(1)
        if car.distance > max_distance:
            max_distance= car.distance

print("\n---------------------------------------------------------------------------------------")
print("", end="\t~~")
for i in ("Register Number", "Max Speed", "Current Speed", "Current Speed"):
    print(" ", i, end="  ~~ ")
print("\n---------------------------------------------------------------------------------------")
for car in cars:
    print("\t\t|\t", car.reg_num, "\t\t|\t", car.max_speed, "\t\t|\t\t", car.current_speed, "\t\t|\t\t", car.distance)
print("---------------------------------------------------------------------------------------")
