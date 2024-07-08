def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Enter A for addition")
print("Enter S for subtraction")
print("Enter M for multiplication")
print("Enter D for division", '\n')

while True:
    choice = input("Enter Choice (A,S,M,D): ")

    if choice in ["A", "a", "ADD", "add", "S", "s", "SUBTRACT", "subtract", "M", "m", "MULTIPLY", "multiply", "D", "d",
                  "DIVIDE", "divide"]:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice in ["A", "ADD", "a", "add"]:
            print("Result: ", num1, '+', num2, '=', add(num1, num2))

        elif choice in ["S", "s", "SUBTRACT", "subtract"]:
            print("'Result: ", num1, "-", num2, "=", subtract(num1, num2))

        elif choice in ["M", "m", "MULTIPLY", "multiply"]:
            print("Result: ", num1, "*", num2, "=", multiply(num1, num2))

        elif choice in ["D", "d", "DIVIDE", "divide"]:
            print("Result: ", num1, "/", num2, "=", divide(num1, num2))

        else:
            print("Please input a correct choice")

        next_calculation = input("Would you like to continue ? (yes/no) : ")

        if next_calculation in ["NO", "No", "no", "n"]:
            break

        elif next_calculation in ["YES", "Yes", "yes", "y"]:
            continue

        else:
            print("please input yes or no")
