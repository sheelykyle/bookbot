import sys
from stats import word_count, character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(bookpath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")

    print("----------- Word Count ----------")
    word_count(bookpath)

    print("--------- Character Count -------")
    character_count(bookpath)

    print("============= END ===============")

main(sys.argv[1])