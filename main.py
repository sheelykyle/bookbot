letter_dictionary = {}

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as book:
        text = book.read()
        number_of_words = countWords(text)
        number_of_letters = countLetters(text)
    sorted_dict = sortDict(letter_dictionary)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    for character in sorted_dict:
        print(f"The {character} was found {letter_dictionary[character]} times")
    print("--- End report ---")

def sortDict(letter_dictionary):
    sorted_dict = sorted(letter_dictionary, key=letter_dictionary.get, reverse=True)
    return sorted_dict

def countWords(text):
    words = text.split()
    return len(words)

def countLetters(text):
    for word in text:
        lowercase_letter = word.lower()
        if lowercase_letter.isalpha() == True:
            if lowercase_letter in letter_dictionary:
                letter_dictionary[lowercase_letter] += 1
            else:
                letter_dictionary[lowercase_letter] = 1
    return letter_dictionary

main()