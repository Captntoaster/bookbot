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

def sort_on(listed):
    return listed['count']

def sort_chars(char_count):
    char_list = []
    for key, value in char_count.items():
            if key.isalpha():
                char_list.append({'char': key, 'count': value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list 




    


   