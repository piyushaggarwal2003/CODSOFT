import string
import random
import tkinter as tk
from tkinter import Label, Entry, Button

def generate_password():
    p1 = list(string.ascii_lowercase)
    p2 = list(string.ascii_uppercase)
    p3 = list(string.digits)
    p4 = list(string.punctuation)

    try:
        password_length = int(entry_password_length.get())
        if password_length < 6:
            result_label.config(text="Password should contain at least 6 characters.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    random.shuffle(p1)
    random.shuffle(p2)
    random.shuffle(p3)
    random.shuffle(p4)

    part1 = round(password_length * (30 / 100))
    part2 = round(password_length * (20 / 100))

    result = []
    for x in range(part1):
        result.append(p1[x])
        result.append(p2[x])
    for x in range(part2):
        result.append(p3[x])
        result.append(p4[x])

    random.shuffle(result)
    final_password = "".join(result)
    result_label.config(text="Strong Password: " + final_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry fields
label_password_length = Label(root, text="How many characters should your password have?")
entry_password_length = Entry(root)
result_label = Label(root, text="")

# Create the generate button
generate_password = Button(root, text="Generate Password", command=generate_password)

# Arrange widgets using grid layout
label_password_length.grid(row=0, column=0)
entry_password_length.grid(row=0, column=1)
generate_password.grid(row=1, columnspan=2)
result_label.grid(row=2, columnspan=2)

# Start the GUI event loop
root.mainloop()
