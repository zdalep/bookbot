def word_count(text):
    with open(text) as f:
        num_words = len(text.split())
    return num_words

def main():
    count = word_count("./books/frankenstein.txt")
    print(count)

main()