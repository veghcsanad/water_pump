class ProblemSolverController:
    def __init__(self, problem_solver_model, problem_solver_view):
        self.model = problem_solver_model
        self.view = problem_solver_view

    def get_user_input(self):
        user_input = input("Enter your command: ")
        return user_input

    def run(self):
        while True:
            user_input = self.get_user_input()
            if user_input.lower() == "exit":
                break
            self.handle_user_input(user_input)
            self.update_view()
    '''def solve_problem(self):
        pass
        pump_status = self.model.check_pump_status()

        if pump_status == 'noise':
            self.model.call_supplier()
            self.view.display_message("Supplier called. Pump is making noise.")
        else:
            self.view.display_message("No issues detected.")
            '''