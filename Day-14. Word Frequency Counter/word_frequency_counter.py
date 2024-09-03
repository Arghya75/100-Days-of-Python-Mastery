import string

def remove_punctuation(text):
    translator = str.maketrans("","",string.punctuation)
    return text.translate(translator)

def counter(text):
    # First it will remove the puntuations from the given text
    cleaned_text = remove_punctuation(text)

    # Then it will convert the text into lowercase
    cleaned_text = cleaned_text.lower()

    # Then it will split the text and create a list of words used in the text
    words = cleaned_text.split()

    # Count the frequency of the words
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

input_text = input("Enter your text: ")
word_frequencies = counter(input_text)

for word, frequencies in word_frequencies.items():
    print(f"{word} : {frequencies}")