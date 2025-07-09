def get_num_words(text):
        words = text.split()
        words_count = len(words)
        print(f"{words_count} words found in the document")


def get_num_characters(text):
        words = text
        num_characters = {}
        for character in words:
                num_characters[character.lower()] = num_characters.get(character.lower(), 0) + 1
        print(f"{num_characters} this i the count")
