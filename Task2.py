class Elevator():
    def __init__(self, bottom, up):
        self.bottom = bottom
        self.up = up
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print(f"Tầng {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Tầng {self.current_floor}")

    def move_to_floor(self, n):
        if n > self.current_floor:
            print(f"Đi lên tầng {n}")
        elif n < self.current_floor:
            print(f"Đi xuống tầng {n}")
        else:
            print(f"Thang máy đang ở tầng {n}")

        while self.current_floor < n:
            self.floor_up()
        while self.current_floor > n:
            self.floor_down()


class Building():
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, elevator_number, floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"--- Thang máy số {elevator_number} ---")
        elevator.move_to_floor(floor)
        print()


def run():
    b = Building(0, 19, 3)
    print("Tòa nhà này có 18 tầng!\n")

    tang1 = int(input("Thang máy 1 - Nhập tầng muốn tới: "))
    b.run_elevator(1, tang1)

    tang2 = int(input("Thang máy 2 - Nhập tầng muốn tới: "))
    b.run_elevator(2, tang2)

    # Quay về tầng 0
    b.run_elevator(1, 0)
    b.run_elevator(2, 0)


if __name__ == "__main__":
    run()