from basic_operations import *

#Simple Calculator

print("Please, select your operation")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiplication")
print("4 - Division")

while True:
    choice = input("Please, enter your choice (1 | 2 |3 | 4): ")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Please, enter your FIRST number: "))
        num2 = float(input("Please, enter your SECOND number: "))
        if choice == "1":
            print(f"{num1} + {num2} = ", add(num1, num2))
        elif choice == "2":
            print(f"{num1} - {num2} = ", subtract(num1, num2))
        elif choice == "3":
            print(f"{num1} * {num2} = ", multiplication(num1, num2))
        elif choice == "4":
            print(f"{num1} / {num2} = ", divison(num1, num2))
        else:
            print("Your choice isn't valid")

        keep_running = input("Would you like to continue? yes or no? ")
        if keep_running in ("yes", "y", "YES", "Y"):
            continue
        else:
            break