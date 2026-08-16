# Adds two numbers
def add(a, b):
    return a + b

# Subtracts second number from first
def subtract(a, b):
    return a - b

# Multiplies two numbers
def multiply(a, b):
    return a * b

# Divides first number by second
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b




def main():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            try:
                print("Result:", divide(num1, num2))
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
