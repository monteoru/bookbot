from stats import get_num_words, return_count_of_characters
import sys
from ntpath import extsep

def get_book_text(file_path):
   with open(file_path) as f:
        return f.read()

def main():
    path = sys.argv[1]

    text = get_book_text(path)
    num_words = len(get_num_words(text))
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('----------- Character Count ----------')
    result = return_count_of_characters(text)

    for item in result:
        print(f'{item["char"]}: {item["num"]}')

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
