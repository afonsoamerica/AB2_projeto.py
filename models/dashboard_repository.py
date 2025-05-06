class DashboardRepository:
    """
    Repository for storing and accessing dashboards.
    """
    
    def __init__(self):
        """
        Initializes the dashboard repository.
        """
        self.dashboards = {}
    
    def add(self, dashboard):
        """
        Adds a dashboard to the repository.
        
        Args:
            dashboard: Dashboard object to be added.
            
        Returns:
            Dashboard: The added dashboard.
        """
        self.dashboards[dashboard.name] = dashboard
        return dashboard
    
    def get(self, name):
        """
        Gets a dashboard by name.
        
        Args:
            name (str): Dashboard name.
            
        Returns:
            Dashboard: Dashboard object or None if not found.
        """
        return self.dashboards.get(name)
    
    def get_all(self):
        """
        Gets all dashboards.
        
        Returns:
            list: List of all dashboard objects.
        """
        return list(self.dashboards.values())
    
    def remove(self, name):
        """
        Removes a dashboard by name.
        
        Args:
            name (str): Name of the dashboard to be removed.
            
        Returns:
            bool: True if successfully removed, False otherwise.
        """
        if name in self.dashboards:
            del self.dashboards[name]
            return True
        return False