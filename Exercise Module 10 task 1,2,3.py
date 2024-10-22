class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def go_to_floor(self,floor_number):
        differ_floor = floor_number - self.current_floor
        if differ_floor < 0:
            for i in range(abs(differ_floor)):
                self.floor_down()
                print(f"We are currently at floor {self.current_floor}.")
        elif differ_floor > 0:
            for i in range(differ_floor):
                self.floor_up()
                print(f"We are currently at floor {self.current_floor}.")
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        else:
            self.current_floor = top_floor
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        else:
            self.current_floor = bottom_floor

class Building:
    def __init__(self,bottom_floor, top_floor, elevator_quantity):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_quantity = elevator_quantity
        self.elevators=[]
        for i in range(self.elevator_quantity):
            i = Elevator(self.bottom_floor, self.top_floor)
            self.elevators.append(i)
    def run_elevator(self,elevator_number,destination_floor):
        self.elevators[elevator_number-1].go_to_floor(destination_floor)
    def fire_alarm(self):
        for elevator in self.elevators:
           elevator.go_to_floor(self.bottom_floor)

if __name__ == "__main__":
    h=Elevator(1,10)
    h.go_to_floor(5)
    hoas1 = Building(1,10,3)
    print(hoas1.elevators)
    hoas1.run_elevator(2,5)
    hoas1.run_elevator(3,8)
    hoas1.fire_alarm()