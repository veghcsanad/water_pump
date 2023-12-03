class ProblemSolverModel:
    def __init__(self, domain_model, rule_model):
        self.domain_model = domain_model
        self.rule_model = rule_model

    def evaluate_rule(self, rule):
        for condition in rule["conditions"]:
            entity_type = condition["entity"]
            attribute = condition["attribute"]
            operator = condition["operator"]
            value = condition["value"]
            status = self.domain_model.get_entity(entity_type)[attribute]
            if status is not None:
                if operator == "equals" and status != value:
                    return False
            else:
                print("I need more info")

        self.rule_model.set_outcome(rule["action"])
        print(rule["action"])
        return True

    def solve_problem(self):
        for rule in self.rule_model.get_rules():
            self.evaluate_rule(self.rule_model.get_rules()[rule])

    def check_pump_status(self):
        pump = self.domain_model.get_water_pump()
        return 'noise' # for now checking the status of the water pump is not implemented

    def call_supplier(self):
        print("Calling the pump supplier.")
