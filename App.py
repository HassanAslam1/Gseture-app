# Function to perform arithmetic operations
def calculate():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    while True:
        # Take user input for the operation and numbers
        operation = input("Enter operation (+, -, *, /) or 'quit' to exit: ").strip()

        if operation.lower() == 'quit':
            print("Exiting calculator...")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter a valid operation.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                continue
            result = num1 / num2
        
        # Output the result
        print(f"The result of {num1} {operation} {num2} is: {result}\n")

# Run the calculator function
calculate()
