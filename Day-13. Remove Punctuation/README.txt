Punctuation Remover
Purpose
The Punctuation Remover program is designed to remove all punctuation characters from a given input string. It helps clean text by eliminating punctuation marks such as commas, periods, exclamation marks, etc., leaving only the words and spaces.

How It Works
The program uses Python's string module and the str.translate() method to achieve this. It creates a translation table that maps each punctuation character to None, effectively removing them from the text when the translation is applied.

Usage
Input: The user is prompted to enter a string of text that may contain punctuation.
Processing: The program processes the input string, removing all punctuation characters.
Output: The program returns and displays the cleaned text without any punctuation.
Example
Here is an example of how the program works:

Input: "Hello, world! This is a test."
Output: Hello world This is a test