class DocumentView:
    """
    View for user interaction related to documents.
    """
    
    def show_menu(self):
        """
        Displays the document management menu.
        
        Returns:
            str: Option selected by the user.
        """
        print('\n===== Document Management =====')
        print('1 - Upload document')
        print('2 - List documents')
        print('3 - Search documents')
        print('4 - View document')
        print('5 - Update document')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_document_info(self, categories):
        """
        Gets information to create a new document.
        
        Args:
            categories (list): List of available document categories.
            
        Returns:
            dict: Dictionary with document information or None if invalid.
        """
        print("\n=== Upload Document ===")
        name = input("Enter document name: ")
        
        print("\nSelect category:")
        for i, category in enumerate(categories, 1):
            print(f"{i} - {category.title()}")
        
        try:
            category_index = int(input("Enter category number: ")) - 1
            
            if not (0 <= category_index < len(categories)):
                self.show_message("Invalid category.")
                return None
                
            category = categories[category_index]
            
            print("\nDocument content (type 'END' on a new line when finished):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            content = '\n'.join(content_lines)
            
            related_to = input("\nRelated to (CPF/ID or leave empty): ").strip() or None
            
            return {
                'name': name,
                'category': category,
                'content': content,
                'related_to': related_to
            }
        except ValueError:
            self.show_message("Please enter a valid number.")
            return None
    
    def get_document_id(self):
        """
        Gets a document ID.
        
        Returns:
            int: Document ID entered by the user or None if invalid.
        """
        try:
            return int(input("Enter document ID: "))
        except ValueError:
            self.show_message("Please enter a valid document ID.")
            return None
    
    def get_search_option(self):
        """
        Gets the search criteria for documents.
        
        Returns:
            tuple: Search type and search term, or None if invalid.
        """
        print("\n=== Search Documents ===")
        print("1 - Search by name")
        print("2 - Search by category")
        print("3 - Search by related to")
        option = input("Enter option: ")
        
        if option == "1":
            name = input("Enter document name: ").lower()
            return ("name", name)
        elif option == "2":
            category = input("Enter category: ").lower()
            return ("category", category)
        elif option == "3":
            related_to = input("Enter CPF/ID: ")
            return ("related", related_to)
        else:
            self.show_message("Invalid option.")
            return None
    
    def get_update_content(self, current_content):
        """
        Gets updated content for a document.
        
        Args:
            current_content (str): Current document content.
            
        Returns:
            str: Updated content.
        """
        print("\nCurrent content:")
        print(current_content)
        
        print("\nNew content (type 'END' on a new line when finished):")
        content_lines = []
        while True:
            line = input()
            if line == 'END':
                break
            content_lines.append(line)
        
        return '\n'.join(content_lines)
    
    def show_document(self, document):
        """
        Displays document information.
        
        Args:
            document: Document object to be displayed.
        """
        print("\n=== Document Details ===")
        print(f"ID: {document.id}")
        print(f"Name: {document.name}")
        print(f"Category: {document.category}")
        print(f"Version: {document.version}")
        print(f"Upload Date: {document.upload_date.strftime('%d/%m/%Y %H:%M')}")
        if document.related_to:
            print(f"Related to: {document.related_to}")
        print("\nContent:")
        print("-"*50)
        print(document.content)
    
    def show_documents(self, documents):
        """
        Displays list of documents.
        
        Args:
            documents (list): List of Document objects.
        """
        if not documents:
            print("No documents found.")
            return
        
        for doc in documents:
            print("\n" + "-"*50)
            print(doc)
    
    def show_message(self, message):
        """
        Displays a message to the user.
        
        Args:
            message (str): Message to be displayed.
        """
        print(message)