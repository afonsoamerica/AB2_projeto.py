from models.contact import Contact
from utils.validators import Validator

class ContactFactory:
    @staticmethod
    def create_contact(cpf: str, name: str, phone: str, email: str) -> Contact:
        """Cria e valida um Contact antes de instanciá-lo."""
        validator = Validator()
        
        validated_cpf = validator.validate_cpf(cpf)
        validated_phone = validator.validate_phone(phone)
        validated_email = validator.validate_email(email)
        
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        return Contact(validated_cpf, name, validated_phone, validated_email)