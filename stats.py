def get_num_words(text):
        words = text.split()
        words_count = len(words)
        print(f"Found {words_count} total words")


def get_num_characters(text):
        words = text
        num_characters = {}
        for character in words:
                num_characters[character.lower()] = num_characters.get(character.lower(), 0) + 1
        return num_characters

def sort_on(items):
        return items["num"]

def get_report(dic):
        dic_list = []
        for d in dic:
            new_dic = {}
            count = dic[d]
            new_dic["char"] = d
            new_dic["num"] = count
            dic_list += [new_dic]
        dic_list.sort(reverse=True, key=sort_on)
        return dic_list
