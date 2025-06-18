from pickle import EMPTY_DICT
from string import printable
def get_num_words(text):
    return text.split()

def return_count_of_characters(text):
    characters = text.lower()
    total_of_characters = {}

    for character in characters:
        if character in total_of_characters:
            total_of_characters[character] += 1
        else:
            total_of_characters[character] = 1
    return total_of_characters
