def word_count(text):
    with open(text) as f:
        contents = f.read()
        split_contents = contents.split()
        count = len(split_contents)
    return count
def main():
    num_words = word_count("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()