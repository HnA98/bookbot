def count_words(text):
    story = text.split()
    words = len(story)
    return words

def count_characters(text):

    characters = {}

    for letter in text:
        letter = letter.lower()
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    
    return characters

def sorted_dictionaries(dictionary):
    dictionary_list = []
    

    for key in dictionary:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dictionary[key]
        dictionary_list.append(new_dict)

    sorted_list = dictionary_list.sort(reverse = True, key=sort_on)
    return dictionary_list

def sort_on(dictionary):
    return dictionary["num"]