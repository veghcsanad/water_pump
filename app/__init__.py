from view.problem_solver_view import ProblemSolverView
from model.question_manager import QuestionManager
from model.rule_model import RuleModel
from model.domain_model import DomainModel
from model.problem_solver import ProblemSolverModel
import json
import tkinter as tk

with open('knowledge/domain.json', 'r') as file:
    domain = DomainModel(json.load(file))
with open('knowledge/rules.json', 'r') as file:
    rules = RuleModel(json.load(file))

question_manager = QuestionManager()

problem_solver = ProblemSolverModel(domain, rules, question_manager)
problem_solver.solve_problem()

root = tk.Tk()
app = ProblemSolverView(root, question_manager, problem_solver)

frame_width = 500
frame_height = 150
root.geometry(f"{frame_width}x{frame_height}")
frame = tk.Frame(root, width=frame_width, height=frame_height, bg="white")
frame.pack()

# Run the application
root.mainloop()