from datetime import datetime

class EmailCampaign:
    def __init__(self, name, template, target_contacts):
        self.name = name
        self.template = template
        self.target_contacts = target_contacts
        self.status = "Draft"  # Draft, Scheduled, In Progress, Completed, Cancelled
        self.schedule_date = None
        self.sent_date = None
        self.stats = {
            "total": len(target_contacts),
            "sent": 0,
            "opened": 0,
            "clicked": 0
        }

    def schedule(self, date):
        if self.status != "Draft":
            raise ValueError("Only draft campaigns can be scheduled")
        self.schedule_date = date
        self.status = "Scheduled"

    def cancel(self):
        if self.status not in ["Draft", "Scheduled"]:
            raise ValueError("Only draft or scheduled campaigns can be cancelled")
        self.status = "Cancelled"

    def __str__(self):
        status_line = f"Status: {self.status}"
        if self.schedule_date:
            status_line += f" (Scheduled for: {self.schedule_date.strftime('%d/%m/%Y %H:%M')})"
        
        return f"""
Campaign: {self.name}
{status_line}
Template: {self.template.name}
Recipients: {self.stats['total']}
Sent: {self.stats['sent']}
"""