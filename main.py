from stats import get_num_words 
from stats import get_num_characters

def get_book_text(filepath):
        with open(filepath) as f:
             return f.read()

def main():
        book_text = get_book_text("./books/frankenstein.txt")
        get_num_words(book_text) 
        get_num_characters(book_text)

main()


