from datetime import datetime

class CampaignView:
    """
    View for user interaction related to email campaigns.
    """
    
    def show_menu(self):
        """
        Displays the campaign management menu.
        
        Returns:
            str: Option selected by the user.
        """
        print('\n===== Campaign Management =====')
        print('1 - Create campaign')
        print('2 - List campaigns')
        print('3 - Schedule campaign')
        print('4 - Cancel campaign')
        print('5 - View campaign statistics')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_campaign_info(self, templates, contacts):
        """
        Gets information to create a new email campaign.
        
        Args:
            templates (list): List of available templates.
            contacts (list): List of available contacts.
            
        Returns:
            dict: Dictionary with campaign information.
        """
        # Get campaign name
        name = input('Enter campaign name: ')
        
        # Show available templates
        print('\nAvailable templates:')
        for i, template in enumerate(templates, 1):
            print(f"{i} - {template.name}")
            
        # Select template
        try:
            template_index = int(input('\nSelect template number: ')) - 1
            if not (0 <= template_index < len(templates)):
                self.show_message('Invalid template selection.')
                return None
        except ValueError:
            self.show_message('Please enter a valid number.')
            return None
            
        # Show available contacts
        print('\nAvailable contacts:')
        for i, contact in enumerate(contacts, 1):
            print(f"{i} - {contact.name} ({contact.email})")
            
        # Select target contacts
        target_contacts = []
        while True:
            try:
                contact_index = input('\nSelect contact number (or leave empty to finish): ')
                if not contact_index:
                    break
                    
                contact_index = int(contact_index) - 1
                if 0 <= contact_index < len(contacts):
                    target_contacts.append(contacts[contact_index])
                else:
                    self.show_message('Invalid contact selection.')
            except ValueError:
                self.show_message('Please enter a valid number.')
        
        if not target_contacts:
            self.show_message('You must select at least one contact.')
            return None
            
        return {
            'name': name, 
            'template': templates[template_index], 
            'target_contacts': target_contacts
        }
    
    def get_campaign_name(self):
        """
        Gets the name of a campaign.
        
        Returns:
            str: Campaign name entered by the user.
        """
        return input('Enter campaign name: ')
    
    def get_schedule_date(self):
        """
        Gets the date to schedule a campaign.
        
        Returns:
            datetime: Scheduled date and time or None if invalid.
        """
        try:
            date_str = input('Enter schedule date (YYYY-MM-DD): ')
            time_str = input('Enter schedule time (HH:MM): ')
            schedule_date = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
            
            if schedule_date <= datetime.now():
                self.show_message('Schedule date must be in the future.')
                return None
                
            return schedule_date
        except ValueError:
            self.show_message('Invalid date/time format. Please try again.')
            return None
    
    def show_campaign(self, campaign):
        """
        Displays campaign information.
        
        Args:
            campaign: EmailCampaign object to be displayed.
        """
        print('\n' + '-'*50)
        print(campaign)
    
    def show_campaigns(self, campaigns):
        """
        Displays list of campaigns.
        
        Args:
            campaigns (list): List of EmailCampaign objects.
        """
        if not campaigns:
            print('No campaigns found.')
            return
        
        for campaign in campaigns:
            print('\n' + '-'*50)
            print(campaign)
    
    def show_campaign_stats(self, campaign):
        """
        Displays statistics for a campaign.
        
        Args:
            campaign: EmailCampaign object with statistics.
        """
        print('\nCampaign Statistics:')
        print('-'*50)
        print(f'Name: {campaign.name}')
        print(f'Status: {campaign.status}')
        print(f'Total recipients: {campaign.stats["total"]}')
        print(f'Sent: {campaign.stats["sent"]}')
        print(f'Opened: {campaign.stats["opened"]}')
        print(f'Clicked: {campaign.stats["clicked"]}')
    
    def show_message(self, message):
        """
        Displays a message to the user.
        
        Args:
            message (str): Message to be displayed.
        """
        print(message)