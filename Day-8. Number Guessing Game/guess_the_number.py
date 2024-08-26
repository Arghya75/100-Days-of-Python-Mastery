import random
user_name = input("Enter your first name: ")

def number_guessing_game():
    number_to_guess = random.randint(0,100)
    max_attempts = 10
    print("Welcome to the number guessing game. I'm thinking a number between 0 to 100.")
    print(f"Now guess the number within {max_attempts}")

    attempts = 0
    while attempts < max_attempts : 
        reply = int(input("Make a guess: "))
        attempts += 1

        if reply < number_to_guess:
            print("Number is too low. Guess another.")
        elif reply == number_to_guess:
            print(f"Congratulations, {user_name}! You've guessed the correct number.")
            break
        else:
            print("Number is too high. Guess another.")
        
        if attempts == max_attempts:
            print(f"Sorry, {user_name}! You've used all your attempts. The number is {number_to_guess}")
        
    play_again = input("Do you want to play again?(yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print('Thank you for playing!')

number_guessing_game()
