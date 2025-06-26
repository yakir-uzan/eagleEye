import mysql.connector
from Models.agent import Agent

class AgentDAL:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor()

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.connection.cursor(dictionary = True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_agent_by_id(self, agent_id):
        self.connect()
        query = "SELECT * FROM agents WHERE id = %s"
        self.cursor.execute(query, (agent_id,))
        result = self.cursor.fetchone()
        self.close()
        return result

    def add_agent(self, agent):
       self.connect()
       query = """
           INSERT INTO agents (name, rank, specialty)
           VALUES (%s, %s, %s)
           """
       self.cursor.execute(query, (agent.name, agent.rank, agent.specialty))
       self.connection.commit()
       self.close()