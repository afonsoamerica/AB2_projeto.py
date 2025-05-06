from models.document import Document

class DocumentController:
    """
    Controller for managing operations related to documents.
    """
    
    def __init__(self, view, document_repository):
        """
        Initializes the controller with view and repository.
        
        Args:
            view: DocumentView object for user interaction.
            document_repository: Repository to store documents.
        """
        self.view = view
        self.repository = document_repository
    
    def upload_document(self):
        """
        Uploads a new document.
        """
        # Get available categories
        categories = self.repository.get_categories()
        
        # Get document information
        doc_info = self.view.get_document_info(categories)
        
        if not doc_info:
            return  # User cancelled or invalid input
            
        # Create and store the document
        document = Document(
            doc_info['name'],
            doc_info['category'],
            doc_info['content'],
            doc_info['related_to']
        )
        
        self.repository.add(document)
        
        self.view.show_message(f"\nDocument uploaded successfully! ID: {document.id}")
    
    def list_documents(self):
        """
        Lists all documents.
        """
        documents = self.repository.get_all()
        self.view.show_documents(documents)
    
    def search_documents(self):
        """
        Searches for documents based on criteria.
        """
        search_info = self.view.get_search_option()
        
        if not search_info:
            return  # User cancelled or invalid input
            
        search_type, search_term = search_info
        
        if search_type == "name":
            results = self.repository.search_by_name(search_term)
        elif search_type == "category":
            results = self.repository.search_by_category(search_term)
        elif search_type == "related":
            results = self.repository.search_by_related(search_term)
        
        self.view.show_documents(results)
    
    def view_document(self):
        """
        Views a document in detail.
        """
        doc_id = self.view.get_document_id()
        
        if doc_id is None:
            return  # Invalid input
            
        document = self.repository.get(doc_id)
        
        if not document:
            self.view.show_message("Document not found.")
            return
            
        self.view.show_document(document)
    
    def update_document(self):
        """
        Updates an existing document.
        """
        doc_id = self.view.get_document_id()
        
        if doc_id is None:
            return  # Invalid input
            
        document = self.repository.get(doc_id)
        
        if not document:
            self.view.show_message("Document not found.")
            return
            
        # Get updated content
        updated_content = self.view.get_update_content(document.content)
        
        # Create new version
        new_doc = Document(
            document.name,
            document.category,
            updated_content,
            document.related_to
        )
        new_doc.version = document.version + 1
        
        # Add new version
        self.repository.add(new_doc)
        
        self.view.show_message(f"Document updated successfully! New version ID: {new_doc.id}")