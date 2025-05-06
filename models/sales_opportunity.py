class SalesOpportunity:
    def __init__(self, id, contact, value, stage):
        self.id = id
        self.contact = contact
        self.value = value
        self.stage = stage
    
    def update_stage(self, new_stage):
        self.stage = new_stage
        return True

    def __str__(self):
        return f'ID: {self.id} | Contact: {self.contact.name} | Value: {self.value} | Stage: {self.stage}'