import tkinter as tk
from tkinter import messagebox, scrolledtext


def search_names(event=None):  # Allow event arg for key binding
    filename = "files/names.txt"
    name_to_find = entry_name.get().strip().lower()
    text_result.delete('1.0', tk.END)  # Clear the text box

    if not name_to_find:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return

    try:
        with open(filename, "r", encoding='utf-8') as file:
            names = file.readlines()

        matches = [name.strip() for name in names if name.lower().startswith(name_to_find)]

        if matches:
            text_result.insert(tk.END, f"These are all the names starting with '{name_to_find.capitalize()}':\n\n")
            for name in matches:
                text_result.insert(tk.END, name + '\n')
        else:
            text_result.insert(tk.END, f"No names found starting with '{name_to_find.capitalize()}'.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "Name list file not found.")


def exit_app(event=None):  # Allow event arg for key binding
    root.destroy()


# GUI setup
root = tk.Tk()
root.title("Name Finder")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Enter the name to look for: ", font=('Arial', 12)).pack(pady=10)
entry_name = tk.Entry(root, width=40, font=('Arial', 14))
entry_name.pack(pady=5)
entry_name.focus()

tk.Button(root, text="Search", font=('Arial', 12), command=search_names).pack(pady=10)

text_result = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=('Courier', 12))
text_result.pack(pady=10)

# Keyboard binding
root.bind('<Return>', search_names)
root.bind('<Escape>', exit_app)

root.mainloop()
