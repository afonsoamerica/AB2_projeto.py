class ActivityView:
    def show_menu(self):
        print('\n===== Activity Management =====')
        print('1 - Add activity')
        print('2 - List all activities')
        print('3 - Find activities by contact')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_activity_info(self):
        cpf = input('Enter the CPF of the contact: ')
        activity_type = input('Enter the type of activity (call, meeting, email): ')
        description = input('Enter the description of the activity: ')
        return {'cpf': cpf, 'activity_type': activity_type, 'description': description}

    def get_cpf(self):
        return input('Enter the CPF of the contact: ')
    
    def show_activities(self, activities):
        if not activities:
            print('No activities registered.')
            return
        
        for activity in activities:
            print(activity)

    def show_message(self, message):
        print(message)