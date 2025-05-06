from models.lead import Lead
from factories.lead_factory import LeadFactory  # Importe a Factory

class LeadController:
    def __init__(self, view, lead_repository):
        self.view = view
        self.repository = lead_repository

    def add_lead(self):
        try:
            lead_data = self.view.get_lead_info()
            
            # Usa a Factory para criar o Lead
            lead = LeadFactory.create_lead(
                name=lead_data['name'],
                email=lead_data['email'],
                phone=lead_data['phone'],
                source=lead_data['source']
            )
            
            self.repository.add(lead)
            self.view.show_message(f"\nLead added successfully! ID: {lead.id}")
        
        except ValueError as e:
            self.view.show_message(f"Error: {str(e)}")

    # --- Métodos abaixo permanecem inalterados (não criam Leads) ---
    def list_leads(self):
        leads = self.repository.get_all()
        self.view.show_leads(leads)

    def update_lead_status(self):
        lead_id = self.view.get_lead_id()
        if lead_id is None:
            return
        
        lead = self.repository.get(lead_id)
        if not lead:
            self.view.show_message("Lead not found.")
            return
        
        print("\nCurrent status:", lead.status)
        new_status = self.view.get_new_status()

        if new_status and lead.update_status(new_status):
            self.view.show_message("Status updated successfully!")
        else:
            self.view.show_message("Invalid status.")

    def add_lead_note(self):
        lead_id = self.view.get_lead_id()
        if lead_id is None:
            return
        
        lead = self.repository.get(lead_id)
        if not lead:
            self.view.show_message("Lead not found.")
            return
        
        note = self.view.get_note()
        lead.add_note(note)
        self.view.show_message("Note added successfully!")

    def view_lead_details(self):
        lead_id = self.view.get_lead_id()
        if lead_id is None:
            return
        
        lead = self.repository.get(lead_id)
        if not lead:
            self.view.show_message("Lead not found.")
            return
        
        self.view.show_lead_details(lead)