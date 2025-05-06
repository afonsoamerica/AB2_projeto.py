class LeadRepository:
    def __init__(self):
        self.leads = {}
        self.current_id = 1

    def add(self, lead):
        lead.id = self.current_id
        self.leads[self.current_id] = lead
        self.current_id += 1
        return lead
    
    def get(self, lead_id):
        return self.leads.get(lead_id)
    
    def get_all(self):
        return list(self.leads.values())
    
    def remove(self, lead_id):
        if lead_id in self.leads:
            del self.leads[lead_id]
            return True
        return False