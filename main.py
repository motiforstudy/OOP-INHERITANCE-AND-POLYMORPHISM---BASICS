from classes.agent import Agent
from classes.mission import Mission
from classes.filedAgent import FieldAgent
from classes.cyberAgent import CyberAgent


# exercise_1 = Agent("shem", 5)
# exercise_1.report()
# exercise_2 = Mission("wow", "china")
# exercise_2_assign = exercise_2.assign(exercise_1.code_name)
# exercise_2.brief()
# exercise_3 = Agent("shem", 11)
# exercise_3.report()
# print(exercise_3.get_clearance_level())
# print(exercise_3.setter_clearance_level(6))
exercise_4 = FieldAgent("shem", 7, "japan")
# exercise_4.report()
exercise_5 = CyberAgent("shi", 8, "hacking")
list_of_agents = []
list_of_agents.append(exercise_4)
list_of_agents.append(exercise_5)
exercise_5.make_a_list(list_of_agents)
Agent.get_total_agents()