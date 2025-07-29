"""
Write a Python program that saves a quote entered by the user and then reads it back from a file.
This simple project introduces you to basic file input/output — a key Python skill used in everything
from logging to data processing.
"""
import os
from datetime import datetime

# Ensure directory exists
os.makedirs("files", exist_ok=True)

file_path = "files/quotes.txt"

try:
    # Get user input and clean it up
    print("Type 'exit' to Quit.\n")

    while True:
        quote = input("What is you favourite quote? ").strip()
        if quote.lower() == "exit":
            break

        if not quote:
            continue  # skip empty input

        # Save the quote
        with open(file_path, "a") as file:
            file.write(quote + "\n")

    # Read and display all saved quotes
    with open(file_path, "r") as file:
        saved_quote = file.read()

    print(f"\nSaved and loaded quotes:\n{saved_quote}")

except Exception as e:
    print(f"An error occurred: {e}")
