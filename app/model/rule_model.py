class RuleModel:
    def __init__(self, rules):
        self.rules = rules
        self.outcome = None

    def set_outcome(self, outcome):
        self.outcome = outcome

    def get_rules(self):
        return self.rules
