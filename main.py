def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import get_num_text
from stats import get_char_count

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_num_text(book_text)
    char_count = get_char_count(book_text)
    print(f"{word_count} words found in the document")
    print(char_count)

main ()