class AnalyticsView:
    """
    View for user interaction related to reports and analytics.
    """
    
    def show_menu(self):
        """
        Displays the reports and analytics menu.
        
        Returns:
            str: Option selected by the user.
        """
        print('\n===== Reports and Analytics =====')
        print('1 - Generate sales report')
        print('2 - Generate lead report')
        print('3 - Generate pipeline report')
        print('4 - List reports')
        print('5 - View report details')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_report_index(self, total_reports):
        """
        Gets the index of a report to view.
        
        Args:
            total_reports (int): Total number of reports available.
            
        Returns:
            int: Report index or None if invalid.
        """
        try:
            index = int(input('Enter the report index: '))
            if 0 <= index < total_reports:
                return index
            else:
                print('Invalid report index.')
                return None
        except ValueError:
            print('Please enter a valid number.')
            return None
    
    def show_reports(self, reports):
        """
        Displays list of reports.
        
        Args:
            reports (list): List of Report objects.
        """
        if not reports:
            print("No reports generated yet.")
            return

        for i, report in enumerate(reports):
            print(f"\n{i}. {report}")
    
    def show_sales_report(self, data):
        """
        Displays a sales report.
        
        Args:
            data (dict): Sales report data.
        """
        print(f"\nTotal Opportunities: {data.get('total_opportunities', 0)}")
        print(f"Total Value: R$ {data.get('total_value', 0):.2f}")
        print(f"Conversion Rate: {data.get('conversion_rate', 0):.1f}%")
        print("\nOpportunities by Stage:")
        for stage, count in data.get('by_stage', {}).items():
            print(f"- {stage}: {count}")
    
    def show_lead_report(self, data):
        """
        Displays a lead report.
        
        Args:
            data (dict): Lead report data.
        """
        print(f"\nTotal Leads: {data.get('total_leads', 0)}")
        print("\nLeads by Status:")
        for status, count in data.get('by_status', {}).items():
            print(f"- {status}: {count}")
        print("\nLeads by Source:")
        for source, count in data.get('by_source', {}).items():
            print(f"- {source}: {count}")
        print("\nConversion Funnel:")
        funnel = data.get('conversion_funnel', {})
        print(f"- Total Leads: {funnel.get('total_leads', 0)}")
        print(f"- Qualified Leads: {funnel.get('qualified_leads', 0)}")
        print(f"- Opportunities: {funnel.get('opportunities', 0)}")
        print(f"- Closed Deals: {funnel.get('closed_deals', 0)}")
    
    def show_pipeline_report(self, data):
        """
        Displays a pipeline report.
        
        Args:
            data (dict): Pipeline report data.
        """
        print("\nStage Distribution:")
        for stage, count in data.get('stage_distribution', {}).items():
            print(f"- {stage}: {count}")
        print("\nValue by Stage:")
        for stage, value in data.get('value_by_stage', {}).items():
            print(f"- {stage}: R$ {value:.2f}")
        print(f"\nAverage Deal Size: R$ {data.get('average_deal_size', 0):.2f}")
    
    def show_report(self, report):
        """
        Displays a report.
        
        Args:
            report: Report object to be displayed.
        """
        print(f"\n=== {report.title} ===")
        print(f"Generated at: {report.generated_at.strftime('%d/%m/%Y %H:%M')}")
        print("\nResults:")
        
        if report.report_type == "sales":
            self.show_sales_report(report.data)
        elif report.report_type == "leads":
            self.show_lead_report(report.data)
        elif report.report_type == "pipeline":
            self.show_pipeline_report(report.data)
    
    def show_message(self, message):
        """
        Displays a message to the user.
        
        Args:
            message (str): Message to be displayed.
        """
        print(message)