def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = count_words(text)
    letters = letters_count(text)
    letters_sorted = dict(sorted(letters.items(), key = lambda item: item[1], reverse = True))
    report(path = book_path, words = words_count, letters = letters_sorted)

def get_text(file):
    # Returns content of text file
    with open(file) as book:
        return book.read()

def count_words(book_text):
    # Returns number of ALL words in file
    words = book_text.split()
    return len(words)

def letters_count(text):
    # Return dictionary with all letters and symbols with numbers letter/symbol was used
    letters = {}
    text_lower = text.lower()
    for l in text_lower:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def report(path, words, letters):
    # Prints full report to the console
    print(f"--- Book report of \033[47;30m{path}\033[0m ---")
    print()
    print(f"Words found: \033[97m{words}\033[0m")
    print()
    print("\033[1mLetters found:\033[0m")
    for letter in letters:
        if letter.isalpha():
            print(f"Letter \033[97m{letter}\033[0m was used \033[97m{letters[letter]}\033[0m times")
    print()
    print("--- End of report ---")

main()