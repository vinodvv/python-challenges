"""
Build a Python program that checks if an email address is valid — using regular expressions (regex).

Here’s the challenge:
    - Ask the user to input an email address.

    - Use a regular expression to validate if it has the correct format (like someone@example.com).

    - Print whether it’s valid or not.

And for those ready for an extra challenge:
💡 Turn this into a small graphical app using tkinter, so users can paste an email and press a button to validate it.

This project gives you practice with:

    - re.match() from Python’s re module

    - Real-world string patterns and data validation

    - Optional: building a tiny GUI with tkinter
"""

import re


def validate_email(email):
    """
        Validates an email address using a regular expression.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
    # This regex broadly covers common email formats.
    # It checks for:
    # 1. Characters before the @ symbol (letters, numbers, dots, underscores, hyphens, plus signs)
    # 2. An @ symbol
    # 3. Characters between @ and the last dot (letters, numbers, dots, hyphens)
    # 4. A dot (.)
    # 5. Top-level domain (2 to 6 characters, letters only)
    # This regex is a common compromise for general email validation.
    # For stricter RFC-compliant validation, the regex would be much more complex.

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

    # Use re.match to check if the regex matches from the beginning of the string
    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == "__main__":
    # Ask the user for an email address
    user_email = input("Enter an email to check if it's valid: ")

    # Validate email
    if validate_email(user_email):
        print("✅ That's a valid email address!")
    else:
        print("❌ That's not a valid email address.")
