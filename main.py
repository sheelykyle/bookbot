letter_dictionary = {}

def main():
    with open("books/frankenstein.txt") as book:
        text = book.read()
        number_of_words = countWords(text)
        print(number_of_words)

        number_of_letters = countLetters(text)
        print(letter_dictionary)

def countWords(text):
    words = text.split()
    return len(words)

def countLetters(text):
    for word in text:
        lowercase_letter = word.lower()
        if lowercase_letter in letter_dictionary:
            letter_dictionary[lowercase_letter] += 1
        else:
            letter_dictionary[lowercase_letter] = 1
    return letter_dictionary
main()