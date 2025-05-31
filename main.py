from stats import word_count, character_count, sort_list
import sys
def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1])as f:
            text = f.read()
            num_words = word_count(text)
            char_count = character_count(text)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_letters = sort_list(char_count)
    for letter in sorted_letters:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")
if __name__ == "__main__": main()
