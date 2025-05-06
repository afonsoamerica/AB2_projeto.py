class Validator:
    @staticmethod
    def validate_cpf(cpf):
        # remove not numeric characters
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise ValueError('CPF must have 11 digits.')
        return cpf
    
    @staticmethod
    def validate_email(email):
        if '@' not in email or not '.' in email:
            raise ValueError('Email must have "@" and "."')
        return email
    
    @staticmethod
    def validate_phone(phone):
        # remove not numeric characters
        phone = ''.join(filter(str.isdigit, phone))

        if len(phone) < 10 or len(phone) > 11:
            raise ValueError('Phone number must have 10 or 11 digits.')
        return phone