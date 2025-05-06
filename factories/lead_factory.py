from models.lead import Lead

class LeadFactory:
    @staticmethod
    def create_lead(name: str, email: str, phone: str, source: str) -> Lead:
        """
        Cria um objeto Lead após validar os dados (se necessário).
        Adicione validações específicas aqui no futuro.
        """
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        # Exemplo de validação opcional para e-mail/telefone:
        if email and "@" not in email:
            raise ValueError("Invalid email format.")
        
        return Lead(name, email, phone, source)