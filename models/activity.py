from datetime import datetime

class Activity:
    def __init__(self, cpf, activity_type, description):
        self.cpf = cpf
        self.activity_type = activity_type
        self.description = description
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.activity_type} - {self.description} (CPF: {self.cpf})"