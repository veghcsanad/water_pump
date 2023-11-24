class ProblemSolverController:
    def __init__(self, problem_solver_model, problem_solver_view):
        self.model = problem_solver_model
        self.view = problem_solver_view

    def solve_problem(self):
        pump_status = self.model.check_pump_status()

        if pump_status == 'noise':
            self.model.call_supplier()
            self.view.display_message("Supplier called. Pump is making noise.")
        else:
            self.view.display_message("No issues detected.")