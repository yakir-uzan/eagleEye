class Agent:
    def __init__(self, id=None, code_name='', real_name='', location='', status='', missions_completed=0):
        self.id = id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return (f"Agent ID: {self.id}\n"
                f"Code Name: {self.code_name}\n"
                f"Real Name: {self.real_name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status}\n"
                f"Missions Completed: {self.missions_completed}")
