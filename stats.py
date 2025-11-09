
from collections import Counter

def word_count(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()

    word_count = len(file_contents.split() )
    print(f"Found {word_count} total words")

def character_count(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    
    lowercase_file_contents = file_contents.lower()
    
    char_count = Counter(lowercase_file_contents)

    for char, count in char_count.most_common():
        if char.isalpha() == False:
            continue
        print(f"{char}: {count}")