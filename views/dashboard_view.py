class DashboardView:
    """
    View for user interaction related to dashboards.
    """
    
    def show_menu(self):
        """
        Displays the dashboard management menu.
        
        Returns:
            str: Option selected by the user.
        """
        print('\n===== Dashboard Management =====')
        print('1 - Create dashboard')
        print('2 - List dashboards')
        print('3 - Customize dashboard')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_dashboard_name(self):
        """
        Gets the name for a new dashboard.
        
        Returns:
            str: Dashboard name entered by the user.
        """
        return input("Enter dashboard name: ")
    
    def get_dashboard_to_customize(self, dashboards):
        """
        Lets the user select a dashboard to customize.
        
        Args:
            dashboards (list): List of available dashboards.
            
        Returns:
            Dashboard: Selected dashboard or None if selection failed.
        """
        if not dashboards:
            print("No dashboards found.")
            return None
            
        print("\nAvailable dashboards:")
        for i, dashboard in enumerate(dashboards, 1):
            print(f"{i}. {dashboard}")
            
        try:
            index = int(input("\nSelect dashboard number: ")) - 1
            if 0 <= index < len(dashboards):
                return dashboards[index]
            else:
                print("Invalid dashboard number.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def show_customize_menu(self):
        """
        Displays the dashboard customization menu.
        
        Returns:
            str: Option selected by the user.
        """
        print("\n=== Customize Dashboard ===")
        print("1 - Add widget")
        print("2 - Remove widget")
        print("3 - View dashboard")
        print("0 - Return")
        return input("Enter option: ")
    
    def get_widget_selection(self, available_widgets):
        """
        Lets the user select a widget to add.
        
        Args:
            available_widgets (list): List of available widgets.
            
        Returns:
            int: Index of selected widget or None if selection failed.
        """
        print("\nAvailable widgets:")
        for i, widget in enumerate(available_widgets, 1):
            print(f"{i}. {widget}")

        try:
            widget_num = int(input("\nSelect widget number: ")) - 1
            if 0 <= widget_num < len(available_widgets):
                return widget_num
            else:
                print("Invalid widget number.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def get_widget_position_to_remove(self, widgets):
        """
        Lets the user select a widget position to remove.
        
        Args:
            widgets (list): List of widgets on the dashboard.
            
        Returns:
            int: Position to remove or None if selection failed.
        """
        if not widgets:
            print("No widgets to remove.")
            return None
            
        print("\nCurrent widgets:")
        for widget in widgets:
            print(f"{widget.position}. {widget}")

        try:
            position = int(input("\nEnter widget position to remove: "))
            return position
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def show_dashboard(self, dashboard):
        """
        Displays a dashboard.
        
        Args:
            dashboard: Dashboard object to be displayed.
        """
        print(f"\n=== {dashboard.name} ===")
        for widget in dashboard.widgets:
            print("\n" + "-"*30)
            print(f"{widget.title}:")
            data = widget.update_data()
            
            if widget.widget_type == "counter":
                print(data)
            elif widget.widget_type == "list":
                for item in data:
                    print(f"- {item}")
            elif widget.widget_type == "chart":
                for label, value in data.items():
                    print(f"{label}: {value}")
    
    def show_message(self, message):
        """
        Displays a message to the user.
        
        Args:
            message (str): Message to be displayed.
        """
        print(message)