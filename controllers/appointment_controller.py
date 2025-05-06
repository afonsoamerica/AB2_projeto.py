from datetime import datetime
from models.appointment import Appointment

class AppointmentController:
    def __init__(self, view, appointment_repository, contact_controller):
        self.view = view
        self.repository = appointment_repository
        self.contact_controller = contact_controller

    def add_appointment(self):
        contact = self.contact_controller.search_contact()

        if not contact:
            self.view.show_message('Contact not found. Please add the contact first.')
            return
        
        appointment_data = self.view.get_appointment_info()
        
        if not appointment_data:
            return  
        
        appointment = Appointment(
            contact,
            appointment_data['title'],
            appointment_data['date_time'],
            appointment_data['description']
        )

        self.repository.add(appointment)
        self.view.show_message('Appointment added successfully.')

    def list_appointments(self):
        appointments = self.repository.get_all()
        self.view.show_appointments(appointments)

    def update_appointment_status(self):
        appointments = self.repository.get_all()
        self.view.show_appointments(appointments)
        
        if not appointments:
            return
        
        index = self.view.get_appointment_index()
        
        if index is None or not (0 <= index < len(appointments)):
            self.view.show_message('Invalid appointment number.')
            return
        
        new_status = self.view.get_new_status()

        if appointments[index].update_status(new_status):
            self.view.show_message('Appointment status updated successfully.')
        else:
            self.view.show_message('Invalid status.')
        
    def remove_appointment(self):
        appointments = self.repository.get_all()
        self.view.show_appointments(appointments)
        
        if not appointments:
            return
        
        index = self.view.get_appointment_index()
        
        if index is None:
            return
        
        if self.repository.remove(index):
            self.view.show_message('Appointment removed successfully!')
        else:
            self.view.show_message('Invalid appointment number.')

    def list_appointments_by_contact(self):
        contact = self.contact_controller.search_contact()
        
        if not contact:
            self.view.show_message('Contact not found. Please add the contact first.')
            return
        
        appointments = self.repository.get_by_contact(contact.cpf)
        self.view.show_appointments(appointments)