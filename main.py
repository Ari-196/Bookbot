from stats import word_count
from stats import get_book_text
from stats import char_count
from stats import sort_count
import sys
def main():
    try:
        book_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print(f"{word_count(get_book_text("./books/frankenstein.txt"))} words found in the document")

    character_count = char_count(get_book_text(book_path)[0])
    #print(character_count)
    sorted_counts = (sort_count(character_count))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {get_book_text(book_path)[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(book_path)[0])} total words")
    print("--------- Character Count -------")
    for i in sorted_counts:
        if i["char"][0].isalpha():
            print(f"{i["char"][0]}: {i["num"]}")
main()
