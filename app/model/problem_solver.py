class ProblemSolverModel:
    def __init__(self, domain_model, rule_model, question_manager):
        self.domain_model = domain_model
        self.rule_model = rule_model
        self.question_manager = question_manager

    def evaluate_rule(self, rule):
        for condition in rule["conditions"]:
            entity_type = condition["entity"]
            attribute = condition["attribute"]
            operator = condition["operator"]
            value = condition["value"]
            status = self.domain_model.get_entity(entity_type)[attribute]
            if status is not None and status != "":
                if operator == "equals" and status != value:
                    return "not_applies"
            else:
                self.question_manager.query(condition['entity'], condition['attribute'])
                return "incomplete"
        return "applies"

    def solve_problem(self):
        for rule in self.rule_model.get_rules():
            outcome = self.evaluate_rule(self.rule_model.get_rules()[rule])
            if outcome == "incomplete":
                return
            elif outcome == "not_applies":
                if self.rule_model.outcome is None or self.rule_model.outcome == "":
                    self.rule_model.outcome = "no action needed"
            else:
                self.rule_model.outcome = self.rule_model.get_rules()[rule]['action']

    def change_status(self, entity, attribute, status):
        self.domain_model.get_entity(entity)[attribute] = status