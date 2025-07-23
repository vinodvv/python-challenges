"""
Day 31: Longest Word
Write a function that has one parameter and takes a list of words as
an argument. The function returns the longest word from the list.
Name the function longest_word. The function should return the
longest word and the number of letters in that word. For example, if
you pass [‘Java, ‘JavaScript’, ‘Python’], your function should
return
[10, JavaScript] as the longest word.
"""

# list1 = ['Java', 'JavaScript', 'Python']
# longest_word = max(list1, key=len)
# print(longest_word)
# longest_word = max([[len(word), word] for word in list1])
#
# print(longest_word)


def long_word(a):
    b = []
    for word in a:
        b.append([len(word), word])
    return max(b)


def longest_word(a):
    longest_word = max([[len(word), word] for word in a])
    return longest_word


if __name__ == "__main__":
    list1 = ['Java', 'JavaScript', 'Python']
    print(longest_word(list1))
    print(long_word(list1))
