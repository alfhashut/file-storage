import os

def list_files():
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}\n")
    files = os.listdir(current_directory)
    for file in files:
        if os.path.isdir(file):
            print(f"{file}/")
        else:
            print(file)

def calculator():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice(1/2/3/4/5):")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif choice == '4':
                print(num1, "/", num2, "=", num1 / num2)
        elif choice == '5':
            break
        else:
            print("Invalid Input. Try again.")

def print_menu():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("Welcome to Nanu (not another nsp updater)")
    print("------------------------------")
    print("1. Updater")
    print("2. Extra")
    print("3. List Files")
    print("4. About the script")
    print("5. Exit")

while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('./NspUpdaterRun')
    elif choice == "2":
        while True:
            print_menu()
            print("Welcome to Extra")
            print("------------------------------")
            print("1. Calculator")
            print("2. DLC Updater[Not Working]")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                calculator()
            elif choice == "2":
                # code for DLC Updater
                print("DLC Updater is still working on it, please check back later")
                input()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")
    elif choice == "3":
        list_files()
        input()
    elif choice == "4":
        print("NspUpdater(Nanu)_Script By Alfhashut (yenilmezoyuncuclub) Version:0.3")
        input()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
