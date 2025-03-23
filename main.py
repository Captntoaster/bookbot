def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    return len(book_text.split())

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    print(f"{word_count()} words found in the document")

main ()