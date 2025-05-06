from datetime import datetime

class Appointment:
    def __init__(self, contact, title, date_time, description):
        self.contact = contact
        self.title = title
        self.date_time = date_time
        self.description = description
        self.status = 'Scheduled' # (Scheduled, Completed, Cancelled)

    def __str__(self):
        return f'Title: {self.title} | Date: {self.date_time.strftime("%d/%m/%Y %H:%M")} | Status: {self.status} | Contact: {self.contact.name}'
    
    def update_status(self, new_status):
        allowed_status = ['Scheduled', 'Completed', 'Cancelled']
        if new_status in allowed_status:
            self.status = new_status
            return True
        return False