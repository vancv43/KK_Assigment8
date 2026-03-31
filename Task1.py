class Elevator():
    def __init__(self, bottom, up):
        self.bottom = bottom
        self.up = up
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print(f"tầng {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"tầng {self.current_floor}")

    def move_to_floor(self, n):
        if n > self.current_floor:
            print(f"Đi lên tầng {n}")
        elif n < self.current_floor:
            print(f"Đi xuống tầng {n}")

        while self.current_floor < n:
            self.floor_up()

        while self.current_floor > n:
            self.floor_down()


# ✅ QUAN TRỌNG: Bọc vào run()
def run():
    E = Elevator(0, 19)
    print("Tòa nhà này có 18 tầng!")
    E.move_to_floor(int(input("Mời bạn nhập tầng mà bạn muốn tới: ")))