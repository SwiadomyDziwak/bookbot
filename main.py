def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = count_words(text)
    unique_words_list = unique_words(text)
    letters = letters_count(text)
    report(path = book_path, words = words_count, unique_words = unique_words_list, letters = letters)

def get_text(file):
    # Returns content of text file
    with open(file) as book:
        return book.read()

def count_words(book_text):
    # Returns number of ALL words in file
    words = book_text.split()
    return len(words)

def unique_words(book_text):
    # Return dictionary with all words with how many times that word was used
    # Sorted from most used to least
    symbols = '1234567890-=!@#$%^&*()_+[]\\;\',./{}|:"<>?'
    unique_words_dict = {}
    for word in book_text.split():
        if word.lower().strip('!?.,') in unique_words_dict:
            unique_words_dict[word.lower().strip(symbols)] += 1
        else:
            unique_words_dict[word.lower().strip(symbols)] =1
    unique_words_dict = dict(sorted(unique_words_dict.items(), key = lambda k: k[1], reverse = True))
    return unique_words_dict

def letters_count(text):
    # Return dictionary with all letters and symbols with how many times letter/symbol was used
    # Sorted from most used to least
    letters = {}
    text_lower = text.lower()
    for l in text_lower:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    letters = dict(sorted(letters.items(), key = lambda item: item[1], reverse = True))
    return letters

def report(path, words, unique_words, letters):
    # Prints full report to the console

    def white(text):
        return f'\033[97m{text}\033[m'
    
    print(f"--- Book report of {white(path)} ---")
    print()
    print(f"Words found: {white(words)}")
    print(f"Unique words: {white(len(unique_words))}")
    print()
    print(white('Letters found:'))
    for letter in letters:
        if letter.isalpha():
            print(f"Letter {white(letter)} was used {white(letters[letter])} times")
    print()
    print("--- End of report ---")

main()