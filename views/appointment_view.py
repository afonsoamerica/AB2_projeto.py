from datetime import datetime

class AppointmentView:
    def show_menu(self):
        print('\n===== Appointment Management =====')
        print('1 - Add appointment')
        print('2 - List appointments')
        print('3 - Update appointment status')
        print('4 - Remove appointment')
        print('5 - List appointments by contact')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_appointment_info(self):
        title = input('Enter title of the appointment: ')

        try:
            date_str = input('Enter the date of the appointment (YYYY-MM-DD): ')
            time_str = input('Enter the time of the appointment (HH:MM): ')
            date_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')

            if date_time < datetime.now():
                print('The appointment must be scheduled for a future date.')
                return None
                
            description = input('Enter a description for the appointment: ')
            
            return {
                'title': title,
                'date_time': date_time,
                'description': description
            }
            
        except ValueError:
            print('Invalid date and time format. Please try again.')
            return None
        
    def get_appointment_index(self):
        try:
            index = int(input('Enter the appointment index (1, 2, 3...): ')) - 1
            return index
        except ValueError:
            print('Invalid index. Please enter a valid number.')
            return None
        
    def get_new_status(self):
        print('Available status: Scheduled, Completed, Cancelled')
        return input('Enter new status: ')
    
    def get_cpf(self):
        return input('Enter the contact CPF: ')
    
    def show_appointments(self, appointments):
        if not appointments:
            print('No appointments found.')
            return
        
        for i, appointment in enumerate(appointments, 1):
            print(f"{i}. {appointment}")

    def show_message(self, message):
        print(message)