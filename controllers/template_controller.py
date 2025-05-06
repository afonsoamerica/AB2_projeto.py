from models.email_template import EmailTemplate

class TemplateController:
    """
    Controller for managing operations related to email templates.
    """
    
    def __init__(self, view, template_repository):
        """
        Initializes the controller with view and repository.
        
        Args:
            view: TemplateView object for user interaction.
            template_repository: Repository to store templates.
        """
        self.view = view
        self.repository = template_repository
    
    def create_template(self):
        """
        Creates a new email template.
        """
        try:
            # Get template data
            template_data = self.view.get_template_info()
            
            # Create template object
            template = EmailTemplate(
                template_data['name'],
                template_data['subject'],
                template_data['content']
            )
            
            # Validate the template
            template.validate()
            
            # Store the template
            self.repository.add(template)
            
            self.view.show_message(f'Template "{template.name}" created successfully!')
            self.view.show_message(f'Variables detected: {", ".join(template.variables)}')
        
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')
    
    def list_templates(self):
        """
        Lists all email templates.
        """
        templates = self.repository.get_all()
        self.view.show_templates(templates)
    
    def preview_template(self):
        """
        Previews an email template with sample data.
        """
        # Get the template name
        name = self.view.get_template_name()
        template = self.repository.get(name)
        
        if not template:
            self.view.show_message('Template not found.')
            return
        
        # Get sample data for variables
        sample_data = self.view.get_sample_data(template.variables)
        
        # Preview the template
        preview_content = template.preview(sample_data)
        self.view.show_preview(template.subject, preview_content)
    
    def remove_template(self):
        """
        Removes an email template.
        """
        # Get the template name
        name = self.view.get_template_name()
        
        # Remove the template
        if self.repository.remove(name):
            self.view.show_message(f'Template "{name}" removed successfully!')
        else:
            self.view.show_message('Template not found.')