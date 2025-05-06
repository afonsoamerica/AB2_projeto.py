class SalesPipelineView:
    def show_menu(self):
        print('\n===== Sales Pipeline Management =====')
        print('1 - Add opportunity')
        print('2 - List opportunities')
        print('3 - Update opportunity stage')
        print('4 - Remove opportunity')
        print('0 - Return')
        return input('Enter option: ')
    
    def get_opportunity_info(self):
        value = input('Enter the value of the deal (R$): ')
        stage = input('Enter the stage of the deal (Prospection, Negotiation, Closed): ')
        return {'value': value, 'stage': stage}
    
    def get_opportunity_id(self):
        try:
            return int(input('Enter the opportunity ID: '))
        except ValueError:
            print('Please enter a valid ID.')
            return None
        
    def get_new_stage(self):
        return input('Enter the new stage of the opportunity (Prospection, Negotiation, Closed): ')
    
    def show_opportunity(self, opportunity):
        print(opportunity)

    def show_opportunities(self, opportunities):
        if not opportunities:
            print('No opportunities found.')
            return
        
        for opportunity in opportunities:
            print(opportunity)

    def show_message(self, message):
        print(message)