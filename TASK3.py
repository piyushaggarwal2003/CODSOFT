import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Please select operation -\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        self.label.pack()

        self.select_var = StringVar()
        self.select_entry = Entry(self.root, textvariable=self.select_var)
        self.select_entry.pack()

        self.number1_var = StringVar()
        self.number1_entry = Entry(self.root, textvariable=self.number1_var)
        self.number1_entry.pack()

        self.number2_var = StringVar()
        self.number2_entry = Entry(self.root, textvariable=self.number2_var)
        self.number2_entry.pack()

        self.result_label = Label(self.root, text="")
        self.result_label.pack()

        self.calculate_button = Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        select = int(self.select_var.get())
        number_1 = int(self.number1_var.get())
        number_2 = int(self.number2_var.get())

        if select == 1:
            result = number_1 + number_2
        elif select == 2:
            result = number_1 - number_2
        elif select == 3:
            result = number_1 * number_2
        elif select == 4:
            result = number_1 / number_2
        else:
            result = "Invalid input"

        self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
