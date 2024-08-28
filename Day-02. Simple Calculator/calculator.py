addition = lambda a,b : a + b
subtraction = lambda a,b : a - b
multiplication = lambda a,b : a * b
division = lambda a,b : a/b if b!= 0 else "Undefined"

# Taking Valid input From the user
def validInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input! Give a valid number.")

# Taking valid operation
def getOperation():
    while True:
        reply = input("Enter what kind of operation do you want to do?\n (a) Addition\n (b) Subtraction\n (c) Multiplication\n (d) Division\n Enter your reply : ")
        if reply in ['a', 'b', 'c', 'd']:
            return reply
        else:
            print("Enter only a/b/c/d")

# Main Logic
def main():
    reply = getOperation()
    x = validInput("Enter your first number: ")
    y = validInput("Enter your second number: ")

    if reply=="a":
        print(f"Result for your required operation is {addition(x,y)}")
    elif reply == "b":
        print(f"Result for your required operation is {subtraction(x,y)}")
    elif reply == "c":
        print(f"Result for your required operation is {multiplication(x,y)}")
    else:
        print(f"Result for your required operation is {division(x,y)}")

if __name__ == "__main__":
    main()