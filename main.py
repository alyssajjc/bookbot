from stats import get_word_count, count_characters, sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    char_count = count_characters(text)
    sorted_chars = sorted_characters(char_count)

    # generate report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_chars:
        char = entry['char']
        if char.isalpha():
            print(f"{char}: {entry['num']}")

main()