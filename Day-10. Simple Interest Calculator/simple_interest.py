def simple_interest(p, n, r):
    return  p * n * (r/100)

def get_valid_input(prompt):
    while True:
        try:
            value =  float(input(prompt))
            if value < 0 :
                print('Please enter valid input.')
            else: 
                return value
        except ValueError:
            print('Invalid Input! Enter only numbers.')

a = get_valid_input("Enter your principal amount: ")
b = get_valid_input("Enter your number of years: ")
c = get_valid_input("Enter your rate of interest: ")

interest = simple_interest(a,b,c)
print(f'The amount of simple interest is - {interest:.4f}')