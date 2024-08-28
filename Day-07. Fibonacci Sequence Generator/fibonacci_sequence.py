def fibonacci_num(n, memo={0:0, 1:1}):
    sequence = []
    for i in range(n) :
        if i not in memo:
            memo[i] = memo[i-2] + memo[i-1]
        sequence.append(memo[i])
    return sequence

def valid_input(propmt):
    while True:
        try:
            return int(input(propmt))
        except ValueError:
            print("Please enter a valid integer.")

num = valid_input("Enter your number: ")
print(fibonacci_num(num))