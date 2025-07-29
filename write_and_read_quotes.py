"""
Write a Python program that saves a quote entered by the user and then reads it back from a file.
This simple project introduces you to basic file input/output — a key Python skill used in everything
from logging to data processing.
"""
import os

# Ensure directory exists
os.makedirs("files", exist_ok=True)

try:
    # Get user input and clean it up
    quote = input("What is your favourite quote? ").strip()

    # Save the quote
    with open("files/quotes.txt", "w") as file:
        file.write(quote)

    # Read teh quote back
    with open("files/quotes.txt", "r") as file:
        saved_quote = file.read().strip()

    print(f"Saved and loaded quote: {saved_quote}")

except Exception as e:
    print(f"An error occurred: {e}")
