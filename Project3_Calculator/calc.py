class Calculator:
    def __init__(self):
        self.history = [] #this list will store history for all the previous operations performed.
    #each function will return the result of the operation as well as add that result to the history of operations
    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero is invalid."
        result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            return "No history available."
        return "\n".join(self.history)


class SimpleCalculatorApp:
    def __init__(self):
        self.calculator = Calculator()  #creating an object of Calculator class
    
    def run(self):
        while True:
          #Menu for user choice
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Show History")
            print("6. Exit")
            
            choice = input("Enter choice(1/2/3/4/5/6): ")

            if choice == '6':
                print("Exiting the calculator. Goodbye!")
                break
            elif choice == '5':
                print("History of calculations:")
                print(self.calculator.show_history())
                continue
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input! Please select a valid operation.")
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                continue
            if choice == '1':
                result = self.calculator.add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = self.calculator.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = self.calculator.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = self.calculator.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            print()

if __name__ == '__main__':
    app = SimpleCalculatorApp() 
    app.run()  
