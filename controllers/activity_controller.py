from models.activity import Activity

class ActivityController:
    def __init__(self, view, activity_repository, contact_repository):
        self.view = view
        self.repository = activity_repository
        self.contact_repository = contact_repository

    def add_activity(self):
        try:
            activity_data = self.view.get_activity_info()
            
            cpf = activity_data['cpf']

            contact = self.contact_repository.get(cpf)
            if not contact:
                self.view.show_message('Contact not found. Please add the contact first.')
                return
            
            activity_type = activity_data['activity_type']
            description = activity_data['description']

            activity = Activity(cpf, activity_type, description)
            self.repository.add(activity)

            self.view.show_message('Activity added successfully.')
        
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')

    def list_activities(self):
        activities = self.repository.get_all()
        self.view.show_activities(activities)

    def find_activities_by_contact(self):
        cpf = self.view.get_cpf()
        
        contact = self.contact_repository.get(cpf)
        if not contact:
            self.view.show_message('Contact not found.')
            return
        
        activities = self.repository.get_by_contact(cpf)
        self.view.show_activities(activities)