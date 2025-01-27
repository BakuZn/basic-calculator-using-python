def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error: Division by zero" if y == 0 else x / y

def calculator():
    print("Python Calculator")
    print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Exit")

    while True:
        choice = input("Choose an operation (1/2/3/4/5): ")
        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Enter numbers only.")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    calculator()
