def main():
    with open("books/frankenstein.txt") as book:
        text = book.read()
        number_of_words = countWords(text)
        print(number_of_words)

def countWords(text):
    words = text.split()
    return len(words)

main()