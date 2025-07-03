"""
Day 25: All the Same
Create a function called all_the_same that takes one argument, a
string, a list, or a tuple and checks if all the elements are the same.
If the elements are the same, the function should return True. If not,
it should return False. For example, [‘Mary’, ‘Mary’, ‘Mary’] should
return True.
"""


# Clear and readable
# Checks if all elements are equal to the first one. Empty input returns True.
def all_the_same(elements):
    if not elements:
        return True
    first_element = elements[0]
    for element in elements:
        if element != first_element:
            return False
    return True


# Pythonic concise
# using the in-built all() function. The all() function will return
# True if all the elements of iterable are true.
def all_same(a):
    a = all(i == a[0] for i in a)
    return a


if __name__ == "__main__":
    elements = ["Mary", "Mary", "Mary"]

    print(all_the_same(elements))
    print(all_same(elements))
