# Shows total words found in the document
def get_num_words(text):
    words = text.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words

# Creates a Dict of how many of each characters are found in the book
def get_chars_dict(text):
    characters = {}
    for words in text:
        word = words.lower()
        for character in word:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return characters

# Sorts the list made in chars_dict_to_sorted_list
def sort_on(chars_dict):
    return chars_dict["num"]

# Creates a blank list to sort the dictionary and append the items to the list.
def chars_dict_to_sorted_list(chars_dict):
    sorted = []
    for char, num in chars_dict.items():
        sorted.append({"char": char, "num": num})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
