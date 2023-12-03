import json

from app.controller.problem_solver_controller import ProblemSolverController
from app.model.domain_model import DomainModel
from app.model.problem_solver import ProblemSolverModel
from app.model.rule_model import RuleModel
from app.view.problem_solver_view import ProblemSolverView


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    print("hello world")
    domain = read_json("knowledge/domain.json")
    rules = read_json("knowledge/rules.json")
    domain_model = DomainModel(domain)
    rule_model = RuleModel(rules)
    model = ProblemSolverModel(domain_model, rule_model)
    view = ProblemSolverView()
    controller = ProblemSolverController(model, view)
    model.solve_problem()

if __name__ == "__main__":
    main()
