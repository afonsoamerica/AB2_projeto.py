from models.email_campaign import EmailCampaign
from datetime import datetime

class CampaignController:
    """
    Controller for managing operations related to email campaigns.
    """
    
    def __init__(self, view, campaign_repository, template_controller, contact_controller):
        """
        Initializes the controller with view and repositories.
        
        Args:
            view: CampaignView object for user interaction.
            campaign_repository: Repository to store campaigns.
            template_controller: Controller for accessing templates.
            contact_controller: Controller for accessing contacts.
        """
        self.view = view
        self.repository = campaign_repository
        self.template_controller = template_controller
        self.contact_controller = contact_controller
    
    def create_campaign(self):
        """
        Creates a new email campaign.
        """
        try:
            # Get available templates
            templates = self.template_controller.repository.get_all()
            if not templates:
                self.view.show_message('No templates available. Please create a template first.')
                return
                
            # Get available contacts
            contacts = self.contact_controller.repository.get_all()
            if not contacts:
                self.view.show_message('No contacts available. Please add contacts first.')
                return
                
            # Get campaign data
            campaign_data = self.view.get_campaign_info(templates, contacts)
            
            if not campaign_data:
                return  # User cancelled or there was an error
                
            name = campaign_data['name']
            
            # Check if campaign name already exists
            if self.repository.get(name):
                self.view.show_message('A campaign with this name already exists.')
                return
                
            # Create and store the campaign
            campaign = EmailCampaign(
                name,
                campaign_data['template'],
                campaign_data['target_contacts']
            )
            
            self.repository.add(campaign)
            
            self.view.show_message(f'\nCampaign "{name}" created successfully!')
            
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')
    
    def list_campaigns(self):
        """
        Lists all email campaigns.
        """
        campaigns = self.repository.get_all()
        self.view.show_campaigns(campaigns)
    
    def schedule_campaign(self):
        """
        Schedules an email campaign for future delivery.
        """
        try:
            # Get the campaign name
            name = self.view.get_campaign_name()
            campaign = self.repository.get(name)
            
            if not campaign:
                self.view.show_message('Campaign not found.')
                return
                
            if campaign.status != "Draft":
                self.view.show_message('Only draft campaigns can be scheduled.')
                return
                
            # Get the schedule date
            schedule_date = self.view.get_schedule_date()
            
            if not schedule_date:
                return  # User cancelled or there was an error
                
            # Schedule the campaign
            campaign.schedule(schedule_date)
            
            self.view.show_message(
                f'Campaign "{name}" scheduled successfully for ' +
                f'{schedule_date.strftime("%d/%m/%Y %H:%M")}'
            )
            
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')
    
    def cancel_campaign(self):
        """
        Cancels an email campaign.
        """
        # Get the campaign name
        name = self.view.get_campaign_name()
        campaign = self.repository.get(name)
        
        if not campaign:
            self.view.show_message('Campaign not found.')
            return
            
        try:
            # Cancel the campaign
            campaign.cancel()
            self.view.show_message(f'Campaign "{name}" cancelled successfully.')
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')
    
    def view_campaign_stats(self):
        """
        Views statistics for an email campaign.
        """
        # Get the campaign name
        name = self.view.get_campaign_name()
        campaign = self.repository.get(name)
        
        if not campaign:
            self.view.show_message('Campaign not found.')
            return
            
        # Show campaign statistics
        self.view.show_campaign_stats(campaign)