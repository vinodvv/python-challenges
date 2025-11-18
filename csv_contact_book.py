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

# Main loop
while True:
    print("\nContact Book Menu")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        # Prompt user for new contact
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()

        # Save contact
        with open(FILE_PATH, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

        print("Contact saved.")

    elif choice == "2":
        print("\nSaved Contacts:\n")
        with open(FILE_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Name: {row['Name']}")
                print(f"Phone: {row['Phone']}")
                print(f"Email: {row['Email Address']}")
                print("-" * 20)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
