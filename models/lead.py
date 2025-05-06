from datetime import datetime

class Lead:
    def __init__(self, name, email, phone, source):
        self.id = None
        self.name = name
        self.email = email
        self.phone = phone
        self.source = source # Website, Social Media, Referral, etc.
        self.status  = 'New' # New, Qualified, Negotiating, Converted, Lost
        self.score = 0 # 0 - 100 score
        self.created_at = datetime.now()
        self.last_interaction = None
        self.notes = []

    def update_status(self, new_status):
        valid_status = ['New', 'Qualified', 'Negotiating', 'Converted', 'Lost']
        if new_status in valid_status:
            self.status = new_status
            return True
        return False
    
    def add_note(self, note):
        timestamp = datetime.now()
        self.notes.append({"timestamp": timestamp, "content": note})
        self.last_interaction = timestamp

    def update_score(self, score):
        if score <= score <= 100:
            self.score = score
            return True
        return False
    
    def __str__(self):
        return f'Lead: {self.name} | Status: {self.status} | Score: {self.score} | Source: {self.source}'