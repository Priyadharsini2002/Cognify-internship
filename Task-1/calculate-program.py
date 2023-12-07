def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero is not allowed."
    return x % y

def calculator():
    print("Simple Calculator")
    try:
        # Get user input for numbers and operator
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, %): ")

        # Perform calculation based on the operator entered
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '%':
            result = modulus(num1, num2)
        else:
            result = "Invalid operator. Please enter +, -, *, /, or %."

        print(f"Result: {result}")

    except ValueError:
        print("Error! Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
