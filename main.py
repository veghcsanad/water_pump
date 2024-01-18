import json
from app.view.problem_solver_view_st import ProblemSolverViewSt
from app.model.question_manager import QuestionManager
from app.model.rule_model import RuleModel
from app.model.domain_model import DomainModel
from app.model.problem_solver import ProblemSolverModel
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    domain = DomainModel(read_json('knowledge/domain.json'))
    rules = RuleModel(read_json('knowledge/rules.json'))

    question_manager = QuestionManager()

    problem_solver = ProblemSolverModel(domain, rules, question_manager)
    problem_solver.solve_problem()

    app = ProblemSolverViewSt(question_manager, problem_solver)


if __name__ == "__main__":
    main()