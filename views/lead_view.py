class LeadView:
    def show_menu(self):
        print('\n===== Lead Management =====')
        print('1 - Add lead')
        print('2 - List leads')
        print('3 - Update lead status')
        print('4 - Add lead note')
        print('5 - View lead details')
        print('0 - Return')
        return input('Enter option: ')

    def get_lead_info(self):
        name = input("Enter lead name: ")
        email = input("Enter lead email: ")
        phone = input("Enter lead phone: ")

        print("\nSelect lead source:")
        print("1 - Website")
        print("2 - Social Media")
        print("3 - Referral")
        print("4 - Other")
        source_option = input("Enter option: ")
        
        sources = {
            "1": "Website",
            "2": "Social Media",
            "3": "Referral",
            "4": "Other"
        }

        source = sources.get(source_option, "Other")
        
        return {'name': name, 'email': email, 'phone': phone, 'source': source}

    def get_lead_id(self):
        try:
            return int(input("Enter lead ID: "))
        except ValueError:
            print('Please enter a valid ID')
            return None
        
    def get_new_status(self):
        print("\nSelect new status:")
        print("1 - New")
        print("2 - Qualified")
        print("3 - Negotiating")
        print("4 - Converted")
        print("5 - Lost")
        
        status_map = {
            "1": "New",
            "2": "Qualified",
            "3": "Negotiating",
            "4": "Converted",
            "5": "Lost"
        }

        option = input("Enter option: ")
        return status_map.get(option)
    
    def get_note(self):
        return input("Enter note: ")
    
    def show_lead(self, lead):
        print(lead)

    def show_leads(self, leads):
        if not leads:
            print("No leads found.")
            return
        
        for lead in leads:
            print("\n" + "-"*50)
            print(lead)
            if lead.last_interaction:
                print(f"Last interaction: {lead.last_interaction.strftime('%d/%m/%Y %H:%M')}")

    def show_lead_details(self, lead):
        print("\n=== Lead Details ===")
        print(f"ID: {lead.id}")
        print(f"Name: {lead.name}")
        print(f"Email: {lead.email}")
        print(f"Phone: {lead.phone}")
        print(f"Source: {lead.source}")
        print(f"Status: {lead.status}")
        print(f"Score: {lead.score}")
        print(f"Created: {lead.created_at.strftime('%d/%m/%Y %H:%M')}")
        
        if lead.notes:
            print("\nNotes:")
            for note in lead.notes:
                print(f"[{note['timestamp'].strftime('%d/%m/%Y %H:%M')}] {note['content']}")

    def show_message(self, message):
        print(message)