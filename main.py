from stats import get_number_of_words

def get_book_text(path):
    with open(path) as f:
        book_as_string = f.read()
    return book_as_string

def main():
    frankenstein_path = "books/frankenstein.txt"
    text = get_book_text(frankenstein_path)
    number = get_number_of_words(text)
    report_numbers = f"{number} words found in the document"
    print(report_numbers)


main()