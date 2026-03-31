import random

# ================= class Car từ bài trước =================
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# ================= Race =================
class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for c in self.car_list:
            change = random.randint(-10, 15)
            c.accelerate(change)
            c.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10} {'Speed (km/h)':<15} {'Distance (km)':<15}")
        print("-" * 45)
        for c in self.car_list:
            print(f"{c.registration_number:<10} {c.current_speed:<15} {c.travelled_distance:<15.2f}")

    def race_finished(self):
        for c in self.car_list:
            if c.travelled_distance >= self.kilometers:
                return True
        return False


# ================= run =================
def run():
    cars = []
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\nHour {hours}")
            race.print_status()

    print("\nRace finished")
    race.print_status()


if __name__ == "__main__":
    run()