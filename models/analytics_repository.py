class AnalyticsRepository:
    """
    Repository for storing and accessing reports.
    """
    
    def __init__(self):
        """
        Initializes the analytics repository.
        """
        self.reports = []
    
    def add(self, report):
        """
        Adds a report to the repository.
        
        Args:
            report: Report object to be added.
            
        Returns:
            Report: The added report.
        """
        self.reports.append(report)
        return report
    
    def get_all(self):
        """
        Gets all reports.
        
        Returns:
            list: List of all report objects.
        """
        return self.reports
    
    def get(self, index):
        """
        Gets a report by index.
        
        Args:
            index (int): Index of the report.
            
        Returns:
            Report: Report object or None if not found.
        """
        if 0 <= index < len(self.reports):
            return self.reports[index]
        return None