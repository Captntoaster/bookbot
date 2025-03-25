def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import get_num_text
from stats import get_char_count
from stats import sort_chars

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_num_text(book_text)
    char_count = get_char_count(book_text)
    listed = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in listed:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main ()