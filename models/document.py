from datetime import datetime
import os

class Document:
    def __init__(self, name, category, content, related_to=None):
        self.id = None  # Será definido pelo DocumentManager
        self.name = name
        self.category = category  # proposal, contract, marketing, other
        self.content = content
        self.related_to = related_to  # CPF do contato ou ID da oportunidade
        self.upload_date = datetime.now()
        self.version = 1
        self.file_type = self._get_file_type(name)

    def _get_file_type(self, name):
        return os.path.splitext(name)[1].lower()

    def __str__(self):
        related = f"| Related to: {self.related_to}" if self.related_to else ""
        return f"Document: {self.name} | Category: {self.category} | Version: {self.version} {related}"