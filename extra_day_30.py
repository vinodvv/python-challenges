"""
The school has a list of
names of students saved in a list. The school has asked you to write
a program that takes a list of names and sorts them alphabetically.
The names should be sorted by last names. Here is a list of names:
[‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris Brown’,’
Tom Cruise’]
Your code should not just sort them alphabetically, but it should also
switch the names (the last name must be the first). Here is how your
code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie',
'Knowles Beyonce']
Write a function called sorted_names.
"""

# names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
# sorted_names = sorted(names, key=lambda x: x.split()[-1])
#
# list1 = []
#
# for name in sorted_names:
#     name_parts = name.split()
#     if len(name_parts) == 2:
#         # print(f"{name_parts[1]} {name_parts[0]}")
#         list1.append(f"{name_parts[1]} {name_parts[0]}")
#     else:
#         list1.append(name)
#
# print(names)
# print(list1)
#
#
# # Swap first and last name
# swapped_names = [f"{last} {first}" for first, last in (name.split() for name in sorted_names)]
#
# print(swapped_names)


def sort_and_swap_names(names):
    # Sort by last name
    sorted_names = sorted(names, key=lambda x: x.split()[-1])

    # Swap the first and last names
    swapped_names = []
    for name in sorted_names:
        name_parts = name.split()
        if len(name_parts) == 2:
            swapped_names.append(f"{name_parts[1]} {name_parts[0]}")
        else:
            swapped_names.append(name)  # fallback for unexpected formats

    return swapped_names


if __name__ == "__main__":
    names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
    result = sort_and_swap_names(names)
    print(f"Original list of names: {names}")
    print(f"\nSorted list of names: {result}")
