class SalesPipelineController:
    def __init__(self, view, sales_pipeline_repository, contact_controller):
        self.view = view
        self.repository = sales_pipeline_repository
        self.contact_controller = contact_controller

    def add_opportunity(self):
        contact = self.contact_controller.search_contact()
        if not contact:
            self.view.show_message('Contact not found. Add the contact first.')
            return
        
        try:
            opportunity_data = self.view.get_opportunity_info()
            
            value = float(opportunity_data['value'])
            stage = opportunity_data['stage']

            opportunity = self.repository.add(contact, value, stage)
            
            self.view.show_message(f'Opportunity added successfully! ID: {opportunity.id}')

        except ValueError as e:
            self.view.show_message(f'ERROR: {str(e)}')

    def list_opportunities(self):
        opportunities = self.repository.get_all()
        self.view.show_opportunities(opportunities)

    def update_opportunity_stage(self):
        opportunity_id = self.view.get_opportunity_id()
        
        if opportunity_id is None:
            return
        
        if opportunity_id in self.repository.opportunities:
            new_stage = self.view.get_new_stage()
            
            if self.repository.update_stage(opportunity_id, new_stage):
                self.view.show_message('Opportunity updated successfully!')
            else:
                self.view.show_message('Failed to update opportunity.')
        else:
            self.view.show_message('Opportunity not found.')

    def remove_opportunity(self):
        opportunity_id = self.view.get_opportunity_id()
        
        if opportunity_id is None:
            return
        
        if self.repository.remove(opportunity_id):
            self.view.show_message('Opportunity removed successfully.')
        else:
            self.view.show_message('Opportunity not found.')