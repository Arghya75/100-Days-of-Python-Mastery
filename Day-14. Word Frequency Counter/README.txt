Word Frequency Counter

Purpose
The Word Frequency Counter is a program designed to analyze a body of text and determine how frequently each word appears. This tool is commonly used in text analysis, natural language processing (NLP), and data science to gain insights into the most common words or phrases within a given text.

How It Works
The program processes a text input and counts the occurrence of each word. It then generates a frequency distribution, showing how many times each word appears in the text. This can be useful for identifying keywords, understanding the main topics of a document, or filtering out common words (also known as "stop words").

Key Features:
    -Case Insensitivity: The program typically treats words as case-insensitive, meaning "Word" and "word" are counted as the same word.
    -Punctuation Handling: The program usually removes punctuation before counting to ensure accurate word frequencies.
    -Sorting: The results can be sorted by frequency, showing the most common words first.

Usage
    -Input: The user provides a string of text or a document to be analyzed.
    -Processing: The program processes the text, breaking it down into individual words and counting the occurrences of each word.
    -Output: The program outputs a list or dictionary where each word is paired with its frequency count.

Example
Here is an example scenario of how the Word Frequency Counter might be used:

Input: "The quick brown fox jumps over the lazy dog. The dog barks back at the fox."

Output:
        the: 4
        dog: 2
        fox: 2
        quick: 1
        brown: 1
        jumps: 1
        over: 1
        lazy: 1
        barks: 1
        back: 1
        at: 1