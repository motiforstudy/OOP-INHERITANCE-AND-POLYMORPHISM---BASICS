from classes.agent import Agent



class CyberAgent(Agent):

    def __init__(self,code_name, clearance_level, specialty : str):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty


    def report(self):
        print(f"Agent {self.code_name} reporting. clearance level {self._clearance_level}, specialty: {self.specialty}")


    def make_a_list(self, lst : list[Agent]):
        for agent in lst:
            agent.report()