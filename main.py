import Task1
import Task2
import Task3
import Task4

def show_menu():
    print("\n========== MENU ==========")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("4. Task 4")
    print("0. Exit")
    print("==========================")

def main():
    while True:
        show_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            Task1.run()

        elif choice == "2":
            Task2.run()

        elif choice == "3":
            Task3.run()

        elif choice == "4":
            Task4.run()

        elif choice == "0":
            print("Bye Teacher 👋")
            break

        else:
            print("❌ Sai lựa chọn!")

if __name__ == "__main__":
    main()