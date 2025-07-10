from stats import get_num_words 
from stats import get_num_characters
from stats import get_report 

def get_book_text(filepath):
        with open(filepath) as f:
             return f.read()

def main():
        book_text = get_book_text("./books/frankenstein.txt")
        print("----------- Word Count ----------")
        get_num_words(book_text) 
        dic = get_num_characters(book_text)
        print("--------- Character Count -------")
        for r in get_report(dic):
            c = r["char"].isalpha()
            count = r["num"]
            if c:
                print(f"{r['char']}: {count}")
        print("========= END ==========")


main()


