Fibonacci Sequence Program

What is a Fibonacci Number?

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

The Fibonacci sequence is named after Leonardo of Pisa, who is also known as Fibonacci. It appears in various natural phenomena, such as the arrangement of leaves on a stem or the branching of trees.

Program Overview

This Python program calculates and prints the Fibonacci sequence up to a specified number of terms. The program uses memoization to optimize the calculation, which means it stores previously computed values to avoid redundant calculations.

How the Program Works

1. Function fibonacci_num(n, memo={0:0, 1:1}):
    -Purpose: To generate the Fibonacci sequence up to the nth term.
    -Parameters:
        -n: The number of terms to generate.
        -memo: A dictionary that stores previously computed Fibonacci numbers to speed up the process.
    -Process:
        -It starts by checking if the Fibonacci number for the current term is already in memo.
        -If not, it computes the Fibonacci number using the two preceding numbers.
        -It appends each Fibonacci number to a list and returns the list after processing all terms.
2. Function valid_input(prompt):
    -Purpose: To ensure the user inputs a valid integer.
    -Process:
        -It repeatedly prompts the user until a valid integer is entered.
        -It handles input errors gracefully, asking the user to provide a valid integer if the input is not a number.
3. Main Execution:
    -Prompts the user to enter the number of terms they want in the Fibonacci sequence.
    -Calls the fibonacci_num function with the user's input to get the Fibonacci sequence.
    -Prints the resulting sequence.
Example: If the user enters 5, the program outputs the first five Fibonacci numbers: [0, 1, 1, 2, 3].