def get_num_text(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    small_text = book_text.lower()
    char_dict = {}
    unique = set()
    for i in small_text:
        if i in unique:
            char_dict[i] += 1
        if i not in unique:
            unique.add(i)
            char_dict[i] = 1
    return char_dict
    
