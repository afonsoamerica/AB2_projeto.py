class CampaignRepository:
    """
    Repository for storing and accessing email campaigns.
    """
    
    def __init__(self):
        """
        Initializes the campaign repository.
        """
        self.campaigns = {}
    
    def add(self, campaign):
        """
        Adds a campaign to the repository.
        
        Args:
            campaign: EmailCampaign object to be added.
            
        Returns:
            EmailCampaign: The added campaign.
        """
        self.campaigns[campaign.name] = campaign
        return campaign
    
    def get(self, name):
        """
        Gets a campaign by name.
        
        Args:
            name (str): Campaign name.
            
        Returns:
            EmailCampaign: Campaign object or None if not found.
        """
        return self.campaigns.get(name)
    
    def get_all(self):
        """
        Gets all campaigns.
        
        Returns:
            list: List of all campaign objects.
        """
        return list(self.campaigns.values())
    
    def remove(self, name):
        """
        Removes a campaign by name.
        
        Args:
            name (str): Name of the campaign to be removed.
            
        Returns:
            bool: True if successfully removed, False otherwise.
        """
        if name in self.campaigns:
            del self.campaigns[name]
            return True
        return False