class DomainModel:
    def __init__(self, domain):
        self.water_pump = domain["water_pump"]
        self.pump_head = domain["pump_head"]
        self.pump_flow = domain["pump_flow"]
        self.strainer = domain["strainer"]
        self.valves = domain["valves"]
        self.water = domain["water"]
        self.hose = domain["hose"]

    def get_entity(self, type):
        if type == "water_pump":
            return self.water_pump
        if type == "pump_head":
            return self.pump_head
        if type == "pump_flow":
            return self.pump_flow
        if type == "strainer":
            return self.strainer
        if type == "valves":
            return self.valves
        if type == "water":
            return self.water
        if type == "hose":
            return self.hose

    def get_water_pump(self):
        return self.water_pump
