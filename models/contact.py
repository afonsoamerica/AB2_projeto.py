class Contact:
    def __init__(self, cpf, name, phone, email):
        self.cpf = cpf
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"CPF: {self.cpf} | Name: {self.name} | Phone: {self.phone} | Email: {self.email}"

    def update(self, name = None, phone = None, email = None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        return True