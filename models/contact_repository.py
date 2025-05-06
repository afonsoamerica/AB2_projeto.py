class ContactRepository:

    def __init__(self):
        self.contacts = {}

    def add(self, contact):
        self.contacts[contact.cpf] = contact

    def get(self, cpf):
        return self.contacts.get(cpf)
    
    def get_all(self):
        return list(self.contacts.values())
    
    def remove(self, cpf):
        if cpf in self.contacts:
            del self.contacts[cpf]
            return True
        return False