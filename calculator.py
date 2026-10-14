print("Welcome to the calculator program")
print("This program will help you calculate the total cost of your numeric values")
while True:
    print("What type of calculation would you like to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("What is your choice? (1/2/3/4/5)")
    choice = input()
    if choice == "1":
        print("You have chosen addition")
        print("Please enter the first number:")
        num1 = float(input())
        print("Please enter the second number:")
        num2 = float(input())
        result = num1 + num2
        print("The result of addition is:", result)
    elif choice == "2":
        print("You have chosen subtraction")
        print("Please enter the first number:")
        num1 = float(input())
        print("Please enter the second number:")
        num2 = float(input())
        result = num1 - num2
        print("The result of subtraction is:", result)
    elif choice == "3":
        print("You have chosen multiplication")
        print("Please enter the first number:")
        num1 = float(input())
        print("Please enter the second number:")
        num2 = float(input())
        result = num1 * num2
        print("The result of multiplication is:", result)
    elif choice == "4":
        print("You have chosen division")
        print("Please enter the first number:")
        num1 = float(input())
        print("Please enter the second number:")
        num2 = float(input())
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
        print("The result of division is:", result)
    elif choice == "5":
        print("You have chosen modulus")
        print("Please enter the first number:")
        num1 = float(input())
        print("Please enter the second number:")
        num2 = float(input())
        if num2 == 0:
            print("Error: Modulus by zero is not allowed.")
            continue
        result = num1 % num2
        print("The result of modulus is:", result)
    else:
        print("Invalid choice. Please try again.")
        continue

    print("Do you want to perform another calculation? (yes/no)")
    response = input().strip().lower()
    if response == "yes":
        continue
    elif response == "no":
        print("Thank you for using the calculator program.")
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        continue
