from stats import count_words
from stats import count_characters
from stats import sorted_dictionaries
import sys

def get_book_text(filepath):

    with open(filepath) as file:
        contents = file.read()
    file.close()
    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    num_words = count_words(content)

    frequencies = count_characters(content)

    #print(frequencies)
    dlist = sorted_dictionaries(frequencies)
    
    print("\n\n")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for list in dlist:
        if list['char'].isalpha():
            print(f"{list['char']}: {list['num']}")
        else:
            continue
    print("============ END ============")
main()