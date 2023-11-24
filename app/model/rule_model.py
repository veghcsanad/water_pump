class RuleModel:
    def __init__(self, rules):
        self.rules = rules

    def get_rule(self, condition):
        return self.rules.get(condition)