class ArithmeticModel:

    def calculate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Invalid Operation"

def main():
    model = ArithmeticModel()

    print("--- Python Arithmetic Model ---")

    while True:
        try:
            print("\nAvailable operations: +, -, *, / (or type 'exit' to quit)")
            op = input("Choose operation: ").strip()

            if op.lower() == 'exit':
                print("Goodbye!")
                break

            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            result = model.calculate(n1, n2, op)
            print("-" * 30)
            print(f"RESULT: {n1} {op} {n2} = {result}")
            print("-" * 30)

        except ValueError:
            print("Error: Please enter valid numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
