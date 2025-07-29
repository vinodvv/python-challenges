"""
Build a simple Python program that repeatedly asks the user for input and stores each response in a text file.

Project Task
    * Repeatedly prompt the user to type something.
    * Save each input to a file (one input per line).
    * Stop asking when the user types "exit" (case-insensitive).
"""

import os


def input_save():
    # Ensure 'files' directory exits
    os.makedirs('files/', exist_ok=True)
    print("Type something to save it to a file. Type 'exit' to quit.")

    saved = False  # Flag to track if anything was saved

    while True:
        message = input("What do you want me to write? ")

        if message.lower() == 'exit':
            break
        else:
            with open('files/messages.txt', 'a') as file:
                file.write(message + '\n')
            saved = True  # Set flag to True if a message was saved

    if saved:
        print("\nAll text(s) saved to file 'files/messages.txt'\n")
        print("Here are the saved contents:\n")

        # Read and display file contents
        with open('files/messages.txt', 'r') as file:
            for line in file:
                print(line.strip())
    else:
        print("No text was saved.")


input_save()
