def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero is not possible!"
    return a / b

while True:
    print("\nSelect any operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator.")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("Invalid choice. Please select from 1 to 5.")
