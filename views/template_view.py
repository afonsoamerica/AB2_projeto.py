class TemplateView:
    def show_menu(self):
        print('\n===== Template Management =====')
        print('1 - Create template')
        print('2 - List templates')
        print('3 - Preview template')
        print('4 - Remove template')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_template_info(self):
        name = input('Enter template name: ')
        subject = input('Enter email subject: ')
        print('Enter email content (use {variable_name} for personalization):')
        print('Example: Hello {name}, welcome to {company}!')
        content = input('Content: ')
        
        return {'name': name, 'subject': subject, 'content': content}
    
    def get_template_name(self):
        return input('Enter template name: ')
    
    def get_sample_data(self, variables):
        print('\nTemplate variables:', ', '.join(variables))
        sample_data = {}
        
        for var in variables:
            value = input(f'Enter sample value for {var}: ')
            sample_data[var] = value
            
        return sample_data
    
    def show_template(self, template):
        print('\n' + '-'*50)
        print(template)
    
    def show_templates(self, templates):
        if not templates:
            print('No templates found.')
            return
        
        for template in templates:
            print('\n' + '-'*50)
            print(template)
    
    def show_preview(self, subject, content):
        print('\nPreview:')
        print('-'*50)
        print('Subject:', subject)
        print('Content:')
        print(content)
        print('-'*50)
    
    def show_message(self, message):
        print(message)