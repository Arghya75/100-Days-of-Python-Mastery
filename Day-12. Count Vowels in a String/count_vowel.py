def vowel_counter(my_str):
    vowels = [] # List to store the vowels
    j = 0 # counter for the number of vowels
    for char in my_str:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            j += 1 # increment the vowel count
            vowels.append(char) # add the vowel in vowels set
    return j, vowels # return both number of vowels and the vowels also

entry = input('Enter your string: ')
count, found_vowels = vowel_counter(entry)
print(f"There are {count} vowels in '{entry}' and the vowels are {found_vowels}")