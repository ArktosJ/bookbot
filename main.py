from stats import get_number_of_words
from stats import chracter_counter
from stats import sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        book_as_string = f.read()
    return book_as_string

def printreport(list_with_dict):
    for i in range(len(list_with_dict)):
        dict_here = list_with_dict[i]
        current_char = dict_here["char"]
        current_number = dict_here["num"]
        character_report = f"{current_char}: {current_number}"
        print(character_report)

def printintro():
    print("============ BOOKBOT ============")

def printoutro():
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        printintro()
        path = sys.argv[1]
        print(f"Analyzing book found at {path}")
        text = get_book_text(path)
        number = get_number_of_words(text)
        print("----------- Word Count ----------")
        report_numbers = f"Found {number} total words"
        print(report_numbers)
        print("--------- Character Count -------")
        report_characters = chracter_counter(text)
        sorted = sort_dict(report_characters)
        printreport(sorted)
        printoutro()


main()