import tkinter as tk

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

    # Use re.fullmatch to ensure the entire string matches the regex
    # re,match only checks from the beginning
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


def validate_email_gui():
    """
        Function to be called when the 'Validate' button is clicked.
        It retrieves the email from the input field, validates it,
        and updates the result label.
    """
    email = email_entry.get()  # Get the text from the entry widget

    if validate_email(email):
        # Update the result label with a success message and green color
        result_label.config(text="✅ That's a valid email address!", fg="green")
    else:
        # update the result label with an error message and red color
        result_label.config(text="❌ That's not a valid email address.", fg="red")


# Create the main application window
app = tk.Tk()
app.title("Email Validator")
app.geometry("400x200")  # Set initial window size

# Widgets

# Label for instructions
instruction_label = tk.Label(app, text="Enter an email address to validate:")
instruction_label.pack(pady=10)  # Add some padding

# Entry widget
email_entry = tk.Entry(app, width=40, borderwidth=2, relief="groove")
email_entry.pack(pady=5)
# Set focus to the entry widget when the app starts
email_entry.focus_set()

# Button to trigger validation
validate_button = tk.Button(app, text="Validate Email", command=validate_email_gui)
validate_button.pack(pady=10)

# Label to display validation result
result_label = tk.Label(app, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Start the Tkinter event loop
# This keeps the window open and responsive to user interactions
app.mainloop()
