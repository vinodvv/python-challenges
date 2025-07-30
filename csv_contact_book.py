"""
Build a contact book in Python that stores names, phone numbers, and email addresses in a CSV file.
This project will teach you how to gather user input, work with CSVs, and display stored data —
all useful skills for handling structured information.
"""
import os
import csv

# Check directory is available
os.makedirs("files", exist_ok=True)

# File path and headers
FILE_PATH = "files/contacts.csv"
HEADERS = ["Name", "Phone", "Email Address"]

# Ensure file has headers if it doesn't exist
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

# Prompt user for new contact
name = input("Enter name: ").strip()
phone = input("Enter phone: ").strip()
email = input("Enter email: ").strip()

# Save contact
with open(FILE_PATH, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, phone, email])

print("Contact saved.")

# Ask if user wants to view all contacts
view = input("View all contacts? (yes/no): ").strip().lower()

if view in ['yes', 'y']:
    print("\nSaved Contacts:\n")
    with open(FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['Name']}")
            print(f"Phone: {row['Phone']}")
            print(f"Email: {row['Email Address']}")
            print("-" * 20)
