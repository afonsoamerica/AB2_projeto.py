class TemplateRepository:
    def __init__(self):
        self.templates = {} 

    def add(self, template):
        self.templates[template.name] = template
        return template
    
    def get(self, name):
        return self.templates.get(name)
    
    def get_all(self):
        return list(self.templates.values())
    
    def remove(self, name):
        if name in self.templates:
            del self.templates[name]
            return True
        return False