import tkinter as tk
from tkinter import messagebox

class ProblemSolverView:
    def __init__(self, master, question_manager, problem_solver):
        self.master = master
        self.master.title("Waterpump troubleshooting")
        self.question_manager = question_manager
        self.problem_solver = problem_solver
        self.question = []

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

        self.load_question()

    def load_question(self):
        if len(self.question_manager.query_list) == 0:
            self.question = []
            messagebox.showinfo("What to do?", self.problem_solver.rule_model.outcome)
            return

        self.question = self.question_manager.query_list[0]
        self.question_label.config(text=self.question.question_text)

        for i in range(len(self.question.answers)):
            self.radio_buttons[i].config(text=self.question.answers[i], state="normal")

    def next_question(self):
        if self.selected_answer.get() == "":
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        selected_index = int(self.selected_answer.get())
        self.question_manager.unquery
        self.problem_solver.change_status(self.question.entity, self.question.attribute, self.question.answers[selected_index])
        
        messagebox.showinfo("Question answered.", "Question answered.")

        self.selected_answer.set("")
        self.question = []

        self.load_question()