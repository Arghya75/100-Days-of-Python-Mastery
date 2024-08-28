# Even or Odd checker function
def is_odd_number(a):
    if a % 2 != 0:
        return "The given number is odd"
    else:
        return "The given number is even"

# Taking Valid Input 
def valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a valid number.")

x = valid_input("Enter your number: ")
print(is_odd_number(x))