def word_count(text):
    split_contents = text.split()
    count = len(split_contents)
    return count

def character_count(text):
    characters = {}
    lowcase = text.lower()
    for character in lowcase:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters
def sort_list(dict):
    results = []
    for key, value in dict.items():
        letter = {"char": key, "num": value}
        if letter["char"].isalpha():
            results.append(letter)
    def sort_on(item):
        return item["num"]
    results.sort(reverse = True, key=sort_on)
    return results
