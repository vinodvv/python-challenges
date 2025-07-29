"""
In this challenge, copy the text below and save it as a CSV file.
Save it in the same folder as your Python file. Save it as python.csv.
Write a function called just_digits that reads the text from the CSV
file and returns only digit elements from the file. Your function should
return 1991, 2, 200, 3, 2008 as a list of strings.
"""


with open("files/python.csv", "r", encoding='utf-8') as file:
    words = file.read().split()
    list1 = []
    for word in words:
        if word.isdigit():
            list1.append(word)
print(list1)


