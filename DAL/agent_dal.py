import mysql.connector
from Models.agent import Agent

class AgentDAL:
    def __init__(self, host= "localhost", user= "root", password= "", database= "eagleEyeDB"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def add_agent(self, agent):
        self.connect()
        query = """
            INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed))
        self.conn.commit()
        self.close()

    def get_all_agents(self):
        self.connect()
        query = "SELECT * FROM agents"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.close()

        agents = []
        for row in rows:
            agent = Agent(
                id=row["id"],
                code_name=row["codeName"],
                real_name=row["realName"],
                location=row["location"],
                status=row["status"],
                missions_completed=row["missionsCompleted"]
            )
            agents.append(agent)

        return agents

    def get_agent_by_id(self, agent_id):
        self.connect()
        query = "SELECT * FROM agents WHERE id = %s"
        self.cursor.execute(query, (agent_id,))
        row = self.cursor.fetchone()
        self.close()

        if row:
            agent = Agent(
                id=row["id"],
                code_name=row["codeName"],
                real_name=row["realName"],
                location=row["location"],
                status=row["status"],
                missions_completed=row["missionsCompleted"]
            )
            return agent
        else:
            return None

    def update_agent(self, agent):
        self.connect()
        query = """
        UPDATE agents
        SET codeName = %s, realName = %s, location = %s, status = %s, missionsCompleted = %s
        WHERE id = %s
        """
        self.cursor.execute(query, (
            agent.code_name,
            agent.real_name,
            agent.location,
            agent.status,
            agent.missions_completed,
            agent.id
        ))
        self.conn.commit()
        self.close()

    def delete_agent(self, agent_id):
        self.connect()
        query = "DELETE FROM agents WHERE id = %s"
        self.cursor.execute(query, (agent_id,))
        self.conn.commit()
        self.close()
