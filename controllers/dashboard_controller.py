from models.dashboard import Dashboard
from models.dashboard_widget import DashboardWidget
from datetime import datetime

class DashboardController:
    """
    Controller for managing operations related to dashboards.
    """
    
    def __init__(self, view, dashboard_repository, contact_repository, sales_pipeline_repository, lead_repository, appointment_repository):
        """
        Initializes the controller with view and repositories.
        
        Args:
            view: DashboardView object for user interaction.
            dashboard_repository: Repository to store dashboards.
            contact_repository: Repository for contact data.
            sales_pipeline_repository: Repository for sales data.
            lead_repository: Repository for lead data.
            appointment_repository: Repository for appointment data.
        """
        self.view = view
        self.repository = dashboard_repository
        self.contact_repository = contact_repository
        self.sales_pipeline_repository = sales_pipeline_repository
        self.lead_repository = lead_repository
        self.appointment_repository = appointment_repository
        self._create_available_widgets()
    
    def _create_available_widgets(self):
        """
        Creates the default available widgets.
        """
        self.available_widgets = [
            DashboardWidget(
                "Total Contacts",
                "counter",
                lambda: len(self.contact_repository.get_all())
            ),
            DashboardWidget(
                "Active Opportunities",
                "chart",
                self._get_opportunities_by_stage
            ),
            DashboardWidget(
                "Recent Leads",
                "list",
                self._get_recent_leads
            ),
            DashboardWidget(
                "Upcoming Appointments",
                "list",
                self._get_upcoming_appointments
            )
        ]
    
    def _get_opportunities_by_stage(self):
        """
        Data source for opportunities by stage widget.
        
        Returns:
            dict: Counts of opportunities by stage.
        """
        stages = {}
        for opp in self.sales_pipeline_repository.get_all():
            stages[opp.stage] = stages.get(opp.stage, 0) + 1
        return stages
    
    def _get_recent_leads(self):
        """
        Data source for recent leads widget.
        
        Returns:
            list: Strings representing the most recent leads.
        """
        leads = self.lead_repository.get_all()
        sorted_leads = sorted(leads, key=lambda x: x.created_at, reverse=True)
        return [str(lead) for lead in sorted_leads[:5]]
    
    def _get_upcoming_appointments(self):
        """
        Data source for upcoming appointments widget.
        
        Returns:
            list: Strings representing upcoming appointments.
        """
        appointments = self.appointment_repository.get_upcoming()
        return [str(apt) for apt in appointments[:5]]
    
    def create_dashboard(self):
        """
        Creates a new dashboard.
        """
        name = self.view.get_dashboard_name()
        
        if name in self.repository.dashboards:
            self.view.show_message("A dashboard with this name already exists.")
            return
            
        dashboard = Dashboard(name)
        self.repository.add(dashboard)
        self.view.show_message(f"Dashboard '{name}' created successfully!")
    
    def list_dashboards(self):
        """
        Lists all dashboards.
        """
        dashboards = self.repository.get_all()
        
        if not dashboards:
            self.view.show_message("No dashboards found.")
            return
            
        for dashboard in dashboards:
            print("\n" + "-"*50)
            print(dashboard)
            if dashboard.widgets:
                print("Widgets:")
                for widget in dashboard.widgets:
                    print(f"  {widget.position}. {widget}")
    
    def customize_dashboard(self):
        """
        Customizes a dashboard.
        """
        dashboards = self.repository.get_all()
        dashboard = self.view.get_dashboard_to_customize(dashboards)
        
        if not dashboard:
            return
            
        while True:
            option = self.view.show_customize_menu()
            
            if option == "1":  # Add widget
                self._add_widget_to_dashboard(dashboard)
            elif option == "2":  # Remove widget
                self._remove_widget_from_dashboard(dashboard)
            elif option == "3":  # View dashboard
                self.view.show_dashboard(dashboard)
            elif option == "0":  # Return
                break
    
    def _add_widget_to_dashboard(self, dashboard):
        """
        Adds a widget to a dashboard.
        
        Args:
            dashboard: Dashboard to add the widget to.
        """
        widget_index = self.view.get_widget_selection(self.available_widgets)
        
        if widget_index is not None:
            widget = self.available_widgets[widget_index]
            dashboard.add_widget(widget)
            self.view.show_message("Widget added successfully!")
    
    def _remove_widget_from_dashboard(self, dashboard):
        """
        Removes a widget from a dashboard.
        
        Args:
            dashboard: Dashboard to remove the widget from.
        """
        position = self.view.get_widget_position_to_remove(dashboard.widgets)
        
        if position is not None and dashboard.remove_widget(position):
            self.view.show_message("Widget removed successfully!")