from Models.agent import Agent
from DAL.agent_dal import AgentDAL

dal = AgentDAL(host="localhost", user="root", password="", database="eagleeyeDB")
agent = Agent(code_name="ShadowFox", real_name="James Clarke", location="Berlin", status="Active", missions_completed=7)
agent2 = Agent(id = 4,code_name="Shadow", real_name="Yakir Uzan", location="JLM", status="Active", missions_completed=54)


# dal.add_agent(agent)
# print("Agent added successfully!")
#
# dal.add_agent(agent1)
# print("Agent added successfully!")

# dal.delete_agent(1)
# print("Agent deleted successfully!")

# # print(dal.get_agent_by_id(3))

# agents = dal.get_all_agents()
# for agent in agents:
#     print(f"{agent}\n")
dal.update_agent(agent2)




