import tkinter as tk
from tkinter import messagebox

class ProblemSolverView:
    def __init__(self, question_manager, problem_solver):
        root = tk.Tk()
        root.geometry("500x300")

        self.master = root
        self.master.title("Waterpump troubleshooting")
        self.question_manager = question_manager
        self.problem_solver = problem_solver
        self.question = []

        self.selected_answer = tk.StringVar()

        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        self.next_button = None
        self.load_question()

        root.mainloop()

    def load_question(self):
        if len(self.question_manager.query_list) == 0:
            self.question = []
            messagebox.showinfo("What to do?", self.problem_solver.rule_model.outcome)
            self.master.destroy()
            return

        self.question = self.question_manager.query_list[0]
        self.question_label.config(text=self.question.question_text)
        self.update_buttons()

    def next_question(self):
        if self.selected_answer.get() == "":
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        selected_index = int(self.selected_answer.get())
        self.question_manager.unquery()
        self.problem_solver.change_status(self.question.entity, self.question.attribute, self.question.outcomes[selected_index])

        self.selected_answer.set("")
        self.question = []

        self.problem_solver.solve_problem()
        self.load_question()

    def update_buttons(self):
        if self.next_button is not None:
            self.next_button.destroy()
        for radio_button in self.radio_buttons:
            radio_button.destroy()

        for i, answer in enumerate(self.question.answers):
            radio_button = tk.Radiobutton(
                self.master,
                text=answer,
                variable=self.selected_answer,
                value=str(i)
            )
            radio_button.pack(anchor=tk.CENTER)
            self.radio_buttons.append(radio_button)
            radio_button.config(state="normal")
        
        self.next_button = tk.Button(self.master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)