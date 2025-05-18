def sort_on(dict):
    return dict["num"]

def get_book_text(file):
    with open(file) as book:
        book_contents = book.read()

    return book_contents, file

def word_count(text):
    text = text.split()
    return len(text)

def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_count(char_count_dict):
    char_count_list = []
    temp_dict = {}
    for i in char_count_dict:
        temp_dict = { "char" : [i],"num": char_count_dict[i]}
        char_count_list.append(temp_dict)

    char_count_list.sort(reverse=True, key = sort_on)
    return char_count_list

