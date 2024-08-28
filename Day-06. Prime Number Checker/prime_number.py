import math

# Prime Number checking function
def is_Prime(n):
    if (n <= 1):
        return f"{n} is not a prime number."
    if(n == 2 or n == 3):
        return f'{n} is a prime number.'
    if(n % 2 == 0 or n % 3 == 0):
        return f"{n} is not a prime number."
    
    for i in range(5, int(math.sqrt(n))+1, 6):
        if (n % i == 0 or n %(i+2) == 0):
            return f'{n} is not a prime number.'
    return f'{n} is a prime number'


# Taking valid input from the user
def isValid(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer")

num = isValid("Enter your number: ")
print(is_Prime(num))