from views import (
    MainView, ContactView, SalesPipelineView, ActivityView, 
    AppointmentView, LeadView, TemplateView, CampaignView, 
    DashboardView, AnalyticsView, DocumentView
)

from controllers import (
    ContactController, SalesPipelineController, ActivityController,
    AppointmentController, LeadController, TemplateController, 
    CampaignController, DashboardController, AnalyticsController,
    DocumentController
)

from models import (
    ContactRepository, SalesPipelineRepository, ActivityRepository,
    AppointmentRepository, LeadRepository, TemplateRepository,
    CampaignRepository, DashboardRepository, AnalyticsRepository,
    DocumentRepository
)

def main():
    main_view = MainView()
    contact_view = ContactView()
    sales_pipeline_view = SalesPipelineView()
    activity_view = ActivityView()
    appointment_view = AppointmentView()
    lead_view = LeadView()
    template_view = TemplateView()
    campaign_view = CampaignView()
    dashboard_view = DashboardView()
    analytics_view = AnalyticsView()
    document_view = DocumentView()

    contact_repository = ContactRepository()
    sales_pipeline_repository = SalesPipelineRepository()
    activity_repository = ActivityRepository()
    appointment_repository = AppointmentRepository()
    lead_repository = LeadRepository()
    template_repository = TemplateRepository()
    campaign_repository = CampaignRepository()
    dashboard_repository = DashboardRepository()
    analytics_repository = AnalyticsRepository()
    document_repository = DocumentRepository()

    contact_controller = ContactController(contact_view, contact_repository)
    sales_pipeline_controller = SalesPipelineController(sales_pipeline_view, sales_pipeline_repository, contact_controller)
    activity_controller = ActivityController(activity_view, activity_repository, contact_repository)
    appointment_controller = AppointmentController(appointment_view, appointment_repository, contact_controller)
    lead_controller = LeadController(lead_view, lead_repository)
    template_controller = TemplateController(template_view, template_repository)
    campaign_controller = CampaignController(campaign_view, campaign_repository, template_controller, contact_controller)
    dashboard_controller = DashboardController(dashboard_view, dashboard_repository, contact_repository, sales_pipeline_repository, lead_repository, appointment_repository)
    analytics_controller = AnalyticsController(analytics_view, analytics_repository, contact_repository, sales_pipeline_repository, lead_repository)
    document_controller = DocumentController(document_view, document_repository)

    while True:
        option = main_view.show_main_menu()
        if option == '1':
            handle_contact_menu(contact_controller, contact_view)
        elif option == '2':
            handle_sales_pipeline_menu(sales_pipeline_controller, sales_pipeline_view)
        elif option == '3':
            handle_activity_menu(activity_controller, activity_view)
        elif option == '4':
            handle_appointment_menu(appointment_controller, appointment_view)
        elif option == '5':
            handle_email_menu(template_controller, campaign_controller, template_view, campaign_view)
        elif option == '6':
            handle_lead_menu(lead_controller, lead_view)
        elif option == '7':
            handle_dashboard_menu(dashboard_controller, dashboard_view)
        elif option == '8':
            handle_analytics_menu(analytics_controller, analytics_view)
        elif option == '9':
            handle_document_menu(document_controller, document_view)
        elif option == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Try again.')

def handle_contact_menu(controller, view):
    while True:
        option = view.show_menu()

        if option == '1':
            controller.add_contact()
        elif option == '2':
            controller.list_contacts()
        elif option == '3':
            controller.remove_contact()
        elif option == '4':
            controller.update_contact()
        elif option == '0':
            break
        else:
            print('Invalid option.')

def handle_sales_pipeline_menu(controller, view):
    while True:
        option = view.show_menu()

        if option == '1':
            controller.add_opportunity()
        elif option == '2':
            controller.list_opportunities()
        elif option == '3':
            controller.update_opportunity_stage()
        elif option == '4':
            controller.remove_opportunity()
        elif option == '0':
            break
        else:
            print('Invalid option.')

def handle_activity_menu(controller, view):
    while True:
        option = view.show_menu()

        if option == '1':
            controller.add_activity()
        elif option == '2':
            controller.list_activities()
        elif option == '3':
            controller.find_activities_by_contact()
        elif option == '0':
            break
        else:
            print('Invalid option.')

def handle_appointment_menu(controller, view):
    while True:
        option = view.show_menu()

        if option == '1':
            controller.add_appointment()
        elif option == '2':
            controller.list_appointments()
        elif option == '3':
            controller.update_appointment_status()
        elif option == '4':
            controller.remove_appointment()
        elif option == '5':
            controller.list_appointments_by_contact()
        elif option == '0':
            break
        else:
            print('Invalid option.')

def handle_lead_menu(controller, view):
    while True:
        option = view.show_menu()

        if option == '1':
            controller.add_lead()
        elif option == '2':
            controller.list_leads()
        elif option == '3':
            controller.update_lead_status()
        elif option == '4':
            controller.add_lead_note()
        elif option == '5':
            controller.view_lead_details()
        elif option == '0':
            break
        else:
            print('Invalid option.')

def handle_email_menu(template_controller, campaign_controller, template_view, campaign_view):
    while True:
        print('\n===== Email Campaign Management =====')
        print('1 - Manage templates')
        print('2 - Manage campaigns')
        print('0 - Return')
        option = input('Enter option: ')
        
        if option == '1':  # Manage templates
            handle_template_menu(template_controller, template_view)
        elif option == '2':  # Manage campaigns
            handle_campaign_menu(campaign_controller, campaign_view)
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')

def handle_template_menu(controller, view):
    while True:
        option = view.show_menu()
        
        if option == '1':  # Create
            controller.create_template()
        elif option == '2':  # List
            controller.list_templates()
        elif option == '3':  # Preview
            controller.preview_template()
        elif option == '4':  # Remove
            controller.remove_template()
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')

def handle_campaign_menu(controller, view):
    while True:
        option = view.show_menu()
        
        if option == '1':  # Create
            controller.create_campaign()
        elif option == '2':  # List
            controller.list_campaigns()
        elif option == '3':  # Schedule
            controller.schedule_campaign()
        elif option == '4':  # Cancel
            controller.cancel_campaign()
        elif option == '5':  # View stats
            controller.view_campaign_stats()
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')

def handle_dashboard_menu(controller, view):
    while True:
        option = view.show_menu()
        
        if option == '1':  # Create
            controller.create_dashboard()
        elif option == '2':  # List
            controller.list_dashboards()
        elif option == '3':  # Customize
            controller.customize_dashboard()
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')

def handle_analytics_menu(controller, view):
    while True:
        option = view.show_menu()
        
        if option == '1':  # Generate report
            controller.generate_sales_report()
            view.show_message('Sales report generated sucessfully.')
        elif option == '2':
            controller.generate_lead_report()
            view.show.message('Lead report generated successfully.')
        elif option == '3':
            controller.generate_pipeline_report()
            view.show_message('Pipeline report generated successfully.')
        elif option == '4':
            controller.list_reports()
        elif option == '5':
            controller.view_report()  
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')

def handle_document_menu(controller, view):
    while True:
        option = view.show_menu()
        
        if option == '1':  # Upload
            controller.upload_document()
        elif option == '2':  # List
            controller.list_documents()
        elif option == '3':  # Search
            controller.search_documents()
        elif option == '4':  # View
            controller.view_document()
        elif option == '5':  # Update
            controller.update_document()
        elif option == '0':  # Return
            break
        else:
            print('Invalid option.')


if __name__ == '__main__':
    main()