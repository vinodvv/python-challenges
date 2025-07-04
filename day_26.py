"""
Day 26: Sort Words
Write a function called sort_words that takes a string of words as an
argument, removes the whitespaces, and returns a list of letters
sorted in alphabetical order. Letters will be separated by commas. All
letters should appear once in the list. This means that you sort and
remove duplicates. For example ‘love life’ should return as
['e,f,i,l,o,v'].
"""


def sort_words(sentence):
    list1 = []
    sentence = sentence.replace(" ", "")
    for i in sentence:
        if i not in list1:
            list1.append(i)
    list1.sort()
    sorted_words = [','.join(list1)]
    return sorted_words


def sort_word(string):
    no_spaces = string.replace(' ', '')
    unique_letters = sorted(list(set(no_spaces)))
    unique_letters = [",".join(unique_letters)]
    return unique_letters


if __name__ == "__main__":
    print(sort_words('love life'))
    print(sort_word('love life'))
