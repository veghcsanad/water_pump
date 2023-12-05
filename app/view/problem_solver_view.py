import tkinter as tk
from tkinter import messagebox
import json

class ProblemSolverView:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Waterpump troubleshooting")

        # Define questions and answers
        self.questions = questions

        self.current_question = 0
        self.selected_answer = tk.StringVar()

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(2):
            radio_button = tk.Radiobutton(master, text="", variable=self.selected_answer, value=str(i))
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)
            radio_button.config(state="disabled")

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        # Display the first question
        self.load_question()

    def load_question(self):
        question_data = self.questions[str(self.current_question)]
        self.question_label.config(text=question_data['question'])

        for i in range(len(question_data['answers'])):
            self.radio_buttons[i].config(text=question_data['answers'][str(i)], state="normal")

    def next_question(self):
        # Check if an answer is selected
        if self.selected_answer.get() == "":
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        # Check if the selected answer is correct
        question_data = self.questions[str(self.current_question)]
        selected_index = int(self.selected_answer.get())
        # todo: modify stuff accordingly
        messagebox.showinfo("Question answered.", "Question answered.")

        # Move to the next question or finish the quiz
        self.selected_answer.set("")
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Completed", "All questions answered.")
            self.master.destroy()


json_file_path = 'knowledge/questions.json'

with open(json_file_path, 'r') as file:
    questions = json.load(file)

root = tk.Tk()
app = ProblemSolverView(root, questions)

# Run the application
root.mainloop()