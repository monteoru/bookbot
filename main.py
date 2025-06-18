from stats import get_num_words, return_count_of_characters

def get_book_text(file_path):
   with open(file_path) as f:
        return f.read()

def main():
    path = './books/frankenstein.txt'
    #print(get_book_text(path))
    text = get_book_text(path)
    num_words = len(get_num_words(text))
    print(f'{num_words} words found in the document')

    print(return_count_of_characters(text))
main()
