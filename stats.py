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

    result = []
    for char, count in total_of_characters.items():
        result.append({'char': char, 'num': count})
    return sorted(result, key=lambda x: x['num'], reverse=True)
    #return total_of_characters
