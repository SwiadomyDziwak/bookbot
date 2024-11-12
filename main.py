def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = count_words(text)
    print(f"Words in file: {words_count}")

def get_text(file):
    with open(file) as book:
        return book.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

main()