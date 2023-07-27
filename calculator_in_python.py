def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot perform modulus with zero."
    return x % y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    while True:
        choice = input("Enter operation number (1-6): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", modulus(num1, num2))

        elif choice == '6':
            print("Calculator closed.")
            break
        else:
            print("Invalid input. Please enter a valid operation number (1-6).")

if __name__ == "__main__":
    calculator()
