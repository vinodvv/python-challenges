import tkinter as tk
from tkinter import messagebox


def sum_all_numbers(start, end):
    total = sum(range(start, end + 1))
    return f"The sum of all numbers from {start} to {end} is: {total}"


def calculate_sum():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())

        if start > end:
            messagebox.showinfo("Note", f"Start of Range ({start}) is greater than End of Range ({end})."
                                        f"Swapping values.")
            # print(f"Note: Start ({start}) is greater than end ({end}). Swapping values.")
            start, end = end, start  # Swap to ensure valid range

        result = sum_all_numbers(start, end)
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer for Start of Range and "
                                              "End of Range.")


def exit_app():
    root.destroy()


# Create root window
root = tk.Tk()
root.title("Range Sum Calculator")
root.geometry("400x250")
root.resizable(False, False)

# Labels and entry widgets
tk.Label(root, text="Enter Start of Range:").pack(pady=(20, 5))
start_entry = tk.Entry(root)
start_entry.pack()

tk.Label(root, text="Enter End of Range:").pack(pady=(10, 5))
end_entry = tk.Entry(root)
end_entry.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate_sum).pack(pady=15)

# Result display
result_label = tk.Label(root, text="", fg="blue", font=("Helvetica", 12, "bold"))
result_label.pack()

# Exit button
tk.Button(root, text="Exit", command=exit_app).pack(pady=10)

# Start the GUI event loop
root.mainloop()
