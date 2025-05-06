import re

class EmailTemplate:
    def __init__(self, name, subject, content):
        self.name = name
        self.subject = subject
        self.content = content
        self.variables = self.extract_variables()

    def extract_variables(self):
        """Extract variables from template content that are between curly braces {}"""
        pattern = r'\{([^}]+)\}'
        return list(set(re.findall(pattern, self.content)))

    def preview(self, sample_data=None):
        """Preview the email template with sample data"""
        if not sample_data:
            return
        
        preview_content = self.content
        for var in self.variables:
            if var in sample_data:
                preview_content = preview_content.replace(f'{{{var}}}', sample_data[var])
        return preview_content
    
    def validate(self):
        """Validate if the template has required fields"""
        if not self.name or not self.name.strip():
            raise ValueError("Template name is required")
        if not self.subject or not self.subject.strip():
            raise ValueError("Email subject is required")
        if not self.content or not self.content.strip():
            raise ValueError("Email content is required")
        return True

    def __str__(self):
        var_list = ', '.join(self.variables) if self.variables else 'None'
        return f"Template: {self.name}\nSubject: {self.subject}\nVariables: {var_list}"