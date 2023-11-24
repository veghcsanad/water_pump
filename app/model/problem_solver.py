class ProblemSolverModel:
    def __init__(self, domain_model, rule_model):
        self.domain_model = domain_model
        self.rule_model = rule_model

    def check_pump_status(self):
        pump = self.domain_model.get_water_pump()
        return 'noise' # for now checking the status of the water pump is not implemented

    def call_supplier(self):
        print("Calling the pump supplier.")
