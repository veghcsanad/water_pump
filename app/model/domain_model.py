class DomainModel:
    def __init__(self, domain):
        self.domain = domain

    def get_value(self, entity, attribute):
        if entity in self.domain and attribute in self.domain[entity]:
            return self.domain[entity][attribute]
        else:
            return None

    def set_value(self, entity, attribute, value):
        if entity in self.domain and attribute in self.domain[entity]:
            self.domain[entity][attribute] = value