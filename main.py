def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def word_count():
        words = get_book_text("./books/frankenstein.txt").split()
        num_words = 0
        for w in words:
            if w in words:
                num_words += 1
        print(f"{num_words} words found in the document")

def main():
        word_count()

main()


