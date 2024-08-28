# This function will calculate the factorial for a valid input
def factorial(n):
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# taking input untill user enter a valid input and then calculating factorial
while True:
    user_input = input("Enter your number: ")
    if not user_input.isdigit(): #Check if the number is a positive integer
        print("Invalid input! Please enter only non-negative integer number.")
        continue
    a = int(user_input)
    print(f"{a}! = {factorial(a)}")
    break #Exit from the loop after calculating factorial
