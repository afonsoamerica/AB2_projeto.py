class SalesPipelineRepository:
    def __init__(self):
        self.opportunities = {}
        self.next_id = 1

    def add(self, contact, value, stage):
        from models.sales_opportunity import SalesOpportunity

        opportunity = SalesOpportunity(self.next_id, contact, value, stage)
        self.opportunities[self.next_id] = opportunity
        self.next_id += 1
        return opportunity
    
    def get(self, id):
        return self.opportunities.get(id)
    
    def get_all(self):
        return list(self.opportunities.values())
    
    def remove(self, id):
        if id in self.opportunities:
            del self.opportunities[id]
            return True
        return False
    
    def update_stage(self, id, new_stage):
        opportunity = self.get(id)
        if opportunity:
            return opportunity.update_stage(new_stage)
        return False