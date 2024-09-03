import string

def remove_punctuation(text):
    # Create a translation table that maps the each punctuation character to none
    translator = str.maketrans("","",string.punctuation)
    return text.translate(translator)

input_text = input('Enter your text: ')
clear_text = remove_punctuation(input_text)
print(clear_text)