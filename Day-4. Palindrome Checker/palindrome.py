# function to check palindrome or not
def is_palindrome(a):
    return 'It is Palindrome' if str(a)==str(a)[::-1] else 'It is not Palindrome'

# taking valid input
def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")

num = get_valid_input("Enter your number: ")
print(is_palindrome(num))