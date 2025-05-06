from datetime import datetime

class Report:
    def __init__(self, title, report_type, data):
        self.title = title
        self.report_type = report_type  # sales, pipeline, leads, conversion
        self.data = data
        self.generated_at = datetime.now()

    def __str__(self):
        return f"Report: {self.title} (Type: {self.report_type}) - Generated at: {self.generated_at.strftime('%d/%m/%Y %H:%M')}"