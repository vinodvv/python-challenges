"""
Day 29: Middle Figure
Write a function called middle_figure that takes two parameters a,
and b. The two parameters are strings. The function joins the two
strings and finds the middle element. If the combined string has a
middle element, the function should return the element, otherwise,
return ‘no middle figure’. Use ‘ make love’ as an argument for a and
‘not wars’ as an argument for b. Your function should return ‘e’ as
the middle element. Whitespaces should be removed.
"""


def middle_figure(a, b):
    # Remove white spaces
    a = a.replace(" ", "")
    b = b.replace(" ", "")

    # Join the strings
    joined_string = a + b

    # Check if the length is odd
    if len(joined_string) % 2 == 1:

        middle_index = len(joined_string) // 2
        return f"The middle figure is: '{joined_string[middle_index]}'"
    else:
        return "No middle figure"


if __name__ == "__main__":
    string1 = "make love"
    string2 = "not wars"
    print(middle_figure(string1, string2))

