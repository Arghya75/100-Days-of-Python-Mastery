def pig_latin_converter(word):
    vowels = 'aeiou'
    word = word.lower() # This makes the characters of the word into lowercase

    if word[0] in vowels: # Checks the first letter is vowel or not
        return word + 'way'
    else: # If the first letter is not vowel
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'
        return word + 'ay' # In case the word has no vowels

input_txt = input('Enter your word: ')
converted_word = pig_latin_converter(input_txt)
print(converted_word)