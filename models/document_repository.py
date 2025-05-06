class DocumentRepository:
    """
    Repository for storing and accessing documents.
    """
    
    def __init__(self):
        """
        Initializes the document repository.
        """
        self.documents = {}
        self.current_id = 1
        self.categories = ["proposal", "contract", "marketing", "other"]
    
    def add(self, document):
        """
        Adds a document to the repository.
        
        Args:
            document: Document object to be added.
            
        Returns:
            Document: The added document with ID assigned.
        """
        document.id = self.current_id
        self.documents[self.current_id] = document
        self.current_id += 1
        return document
    
    def get(self, doc_id):
        """
        Gets a document by ID.
        
        Args:
            doc_id (int): Document ID.
            
        Returns:
            Document: Document object or None if not found.
        """
        return self.documents.get(doc_id)
    
    def get_all(self):
        """
        Gets all documents.
        
        Returns:
            list: List of all document objects.
        """
        return list(self.documents.values())
    
    def search_by_name(self, name):
        """
        Searches documents by name.
        
        Args:
            name (str): Search term for document name.
            
        Returns:
            list: List of matching document objects.
        """
        name = name.lower()
        return [doc for doc in self.documents.values() if name in doc.name.lower()]
    
    def search_by_category(self, category):
        """
        Searches documents by category.
        
        Args:
            category (str): Category to search for.
            
        Returns:
            list: List of matching document objects.
        """
        category = category.lower()
        return [doc for doc in self.documents.values() if category == doc.category.lower()]
    
    def search_by_related(self, related_to):
        """
        Searches documents by related entity.
        
        Args:
            related_to (str): Related entity identifier.
            
        Returns:
            list: List of matching document objects.
        """
        return [doc for doc in self.documents.values() if related_to == doc.related_to]
    
    def get_categories(self):
        """
        Gets available document categories.
        
        Returns:
            list: List of category names.
        """
        return self.categories