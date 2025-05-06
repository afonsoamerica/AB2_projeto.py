class ActivityRepository:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        self.activities.append(activity)

    def get_all(self):
        return self.activities
    
    def get_by_contact(self, cpf):
        return [activity for activity in self.activities if activity.cpf == cpf]