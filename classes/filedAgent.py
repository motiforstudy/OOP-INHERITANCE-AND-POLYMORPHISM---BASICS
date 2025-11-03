from classes.agent import Agent



class FieldAgent(Agent):

    def __init__(self,code_name, clearance_level, region : str):
        super().__init__(code_name, clearance_level)
        self.region = region


    def report(self):
        print(f"Agent {self.code_name} reporting. clearance level {self._clearance_level}, Region: {self.region}")

