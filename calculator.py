def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero not allowed."
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "**":
        return num1 ** num2
    else:
        return "Invalid operator"


def calculator():
    print("===== Advanced Calculator =====")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /, %, **): ")
            num2 = float(input("Enter second number: "))
            
            result = calculate(num1, num2, operator)
            print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")

        choice = input("\nDo you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Calculator closed.")
            break


calculator()
