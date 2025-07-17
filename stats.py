def get_number_of_words(text):
    return len(text.split())

def chracter_counter(text):
    text_lower = text.lower()
    dictionary_of_characters = {}
    for word in text_lower:
        for character in word:
            if character in dictionary_of_characters:
                dictionary_of_characters[character] += 1
            else: 
                dictionary_of_characters[character] = 1
    return dictionary_of_characters

def sort_dict(dictionary_to_sort):
    list_of_dict = []
    for item in dictionary_to_sort:
        if item.isalpha():
            dict_to_append = {
                "char": item,
                "num": dictionary_to_sort[item]
            }
            list_of_dict.append(dict_to_append)
            list_of_dict.sort(reverse=True, key=sort_on)
        else:
            continue
    return list_of_dict

def sort_on(items):
    return items["num"]

