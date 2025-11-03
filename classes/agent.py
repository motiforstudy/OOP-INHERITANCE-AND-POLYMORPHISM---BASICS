class Agent:

    total_agents = 0

    def __init__(self, code_name : str, clearance_level : int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. clearance level {self._clearance_level}")

    def get_clearance_level(self):
        return self._clearance_level

    def setter_clearance_level(self, clearance_level):
        if 10 > clearance_level >= 1:
            print("good clearance level")
            self._clearance_level = clearance_level
            return self._clearance_level
        return None

    @staticmethod
    def get_total_agents():
        print(Agent.total_agents)