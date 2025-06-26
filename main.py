from Models.agent import Agent
from DAL.agent_dal import AgentDAL

dal = AgentDAL("localhost", "root", "", "eagleeyeDB")

def print_menu():
    print("\n=== Eagle Eye Agent Management ===\n")
    print("1. Add new agent.")
    print("2. Update agent.")
    print("3. Delete agent.")
    print("4. Show agent by ID.")
    print("5. Show all agents.")
    print("6. Exit")

def add_agent():
    print("Add new agent:")
    code_name = input("Code Name: ")
    real_name = input("Real Name: ")
    location = input("Location: ")
    status = check_status()
    missions_completed = int(input("Missions Completed: "))
    agent = Agent(None, code_name, real_name, location, status, missions_completed)
    dal.add_agent(agent)
    print("✅ Agent added successfully!")
    print("-" * 40)

def update_agent():
    agent_id = int(input("Agent ID to update: "))
    print("Enter new details:")
    code_name = input("Code Name: ")
    real_name = input("Real Name: ")
    location = input("Location: ")
    status = check_status()
    missions_completed = int(input("Missions Completed: "))
    agent = Agent(agent_id, code_name, real_name, location, status, missions_completed)
    dal.update_agent(agent)
    print("✅ Agent updated successfully!")
    print("-" * 40)

def delete_agent():
    agent_id = int(input("Agent ID to delete: "))
    dal.delete_agent(agent_id)
    print("🗑️ Agent deleted.")
    print("-" * 40)

def get_agent():
    agent_id = int(input("Enter agent ID: "))
    agent = dal.get_agent_by_id(agent_id)
    if agent:
        print(agent)
        print("-" * 40)
    else:
        print("❌ Agent not found.")


def show_all_agents():
    agents = dal.get_all_agents()
    if not agents:
        print("No agents in the system.")
    else:
        for agent in agents:
            print(agent)
            print("-" * 40)

def check_status():
    statuses = ["Active", "Injured", "Missing", "Retired"]
    while True:
        status = input("Status (Active, Injured, Missing, Retired): ")
        if status in statuses:
            return status
        print("Invalid status, please try again.")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_agent()
        elif choice == "2":
            update_agent()
        elif choice == "3":
            delete_agent()
        elif choice == "4":
            get_agent()
        elif choice == "5":
            show_all_agents()
        elif choice == "6":
            print("Goodbye 👋")
            print("-" * 40)
            break
        else:
            print("❗Invalid choice, please try again.")
