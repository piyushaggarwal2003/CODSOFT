import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.question_no = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to the Quiz Game!")
        self.label.pack()

        self.start_button = Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.question_no = 0
        self.score = 0
        self.label.config(text="NOTE: If you spell something poorly, it counts as a wrong response.")
        self.start_button.config(state="disabled")
        self.ask_question()

    def ask_question(self):
        self.question_no += 1
        if self.question_no <= 5:
            self.ques_label = Label(self.root, text=f"Question {self.question_no}: {self.get_question()}")
            self.ques_label.pack()

            self.ans_entry = Entry(self.root)
            self.ans_entry.pack()

            self.submit_button = Button(self.root, text="Submit", command=self.check_answer)
            self.submit_button.pack()
        else:
            self.show_result()

    def get_question(self):
        questions = [
            "What does KB stand for?",
            "What does GPU stand for?",
            "What does LCD stand for?",
            "What does PSU stand for?",
            "What does BIOS stand for?"
        ]
        return questions[self.question_no - 1]

    def check_answer(self):
        answers = [
            "kilobyte",
            "graphics processing unit",
            "liquid crystal display",
            "power supply unit",
            "basic input output system"
        ]
        user_answer = self.ans_entry.get().strip().lower()
        correct_answer = answers[self.question_no - 1]

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Accurate! Your score was 1.")
        else:
            messagebox.showinfo("Result", f"Incorrect!\nCorrect answer: {correct_answer}")

        self.ques_label.destroy()
        self.ans_entry.destroy()
        self.submit_button.destroy()
        self.ask_question()

    def show_result(self):
        try:
            percentage = (self.score * 100) / self.question_no
        except ZeroDivisionError:
            percentage = 0

        result_text = f"Number of questions: {self.question_no}\nYour score: {self.score}\n{percentage:.2f}% questions are correct."
        messagebox.showinfo("Game Over", result_text)
        self.label.config(text="Welcome to the Quiz Game!")
        self.start_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
