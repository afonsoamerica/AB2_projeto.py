class ContactView:
    def show_menu(self):
        print('\n===== Contact Management =====')
        print('1 - Add contact')
        print('2 - List contacts')
        print('3 - Remove contact')
        print('4 - Update contact')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_contact_info(self):
        cpf = input('Enter the CPF: ')
        name = input('Enter the name: ')
        phone = input('Enter the phone: ')
        email = input('Enter the email: ')
        return {'cpf': cpf, 'name': name, 'phone': phone, 'email': email}
    
    def get_cpf(self):
        return input('Enter the CPF: ')

    def get_update_info(self, contact):
        print('Leave the field blank if you do not want to update it.')
        name = input(f'Current name ({contact.name}): ')
        phone = input(f'Current phone ({contact.phone}): ')
        email = input(f'Current email ({contact.email}): ')
        return {'name': name, 'phone': phone, 'email': email}
    
    def show_contact(self, contact):
        print(contact)

    def show_contacts(self, contacts):
        if not contacts:
            print('No contacts found.')
            return

        for contact in contacts:
            print(contact)

    def show_message(self, message):
        print(message)