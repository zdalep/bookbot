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
def main():
    with open("./books/frankenstein.txt")as f:
        text = f.read()
        num_words = word_count(text)
        char_count = character_count(text)
    print(f"{num_words} words found in the document")
    print(char_count)
main()
