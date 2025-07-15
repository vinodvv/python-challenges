"""
Build a small, practical Python app that searches through a text file containing a list of names and surnames,
and prints out all the full names that have a specific given name (the first word in each line).

But this time, instead of making your own text file, you’ll use a real dataset provided for you.
"files/names.txt"

This is exactly the kind of lightweight program you might write to:

- Filter a raw text export from a database,

- Quickly look up all records for a given first name,

- Or do informal audits of membership or contact lists.
"""


def search_names(filename, name):
    name = name.lower()
    matches = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            full_name = line.strip()
            if full_name.lower().startswith(name):
                matches.append(full_name)

    if matches:
        print(f"\nThese are all the names starting with '{name.capitalize()}': ")
        for name in matches:
            print(name)
    else:
        print(f"\nNo names found starting with '{name.capitalize()}'.")


if __name__ == "__main__":
    filename = "files/names.txt"
    search_name = input("Enter the name to look for: ").strip()
    search_names(filename, search_name)
