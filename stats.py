def get_word_count(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_characters(dict):
    sort_list = []
    for item in dict:
        sort_list.append({"char": item, "num": dict[item]})

    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
