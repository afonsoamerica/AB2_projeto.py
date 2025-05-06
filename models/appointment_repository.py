from datetime import datetime

class AppointmentRepository:
    def __init__(self):
        self.appointments = []

    def add(self, appointment):
        self.appointments.append(appointment)

    def get_all(self):
        return sorted(self.appointments, key=lambda x: x.date_time)

    def get_by_contact(self, contact):
        return sorted([appointment for appointment in self.appointments if appointment.contact.cpf == contact.cpf], key=lambda x: x.date_time)

    def get_upcoming(self):
        return sorted([appointment for appointment in self.appointments if appointment.date_time > datetime.now()], key=lambda x: x.date_time)

    def remove(self, index):
        if 0 <= index < len(self.appointments):
            self.appointments.pop(index)
            return True
        return False