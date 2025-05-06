# Models package for CRM system

from .contact import Contact
from .contact_repository import ContactRepository
from .sales_opportunity import SalesOpportunity
from .sales_pipeline_repository import SalesPipelineRepository
from .activity import Activity
from .activity_repository import ActivityRepository
from .appointment import Appointment
from .appointment_repository import AppointmentRepository
from .lead import Lead
from .lead_repository import LeadRepository
from .email_template import EmailTemplate
from .template_repository import TemplateRepository
from .email_campaign import EmailCampaign
from .campaign_repository import CampaignRepository
from .dashboard_widget import DashboardWidget
from .dashboard import Dashboard
from .dashboard_repository import DashboardRepository
from .report import Report
from .analytics_repository import AnalyticsRepository
from .document import Document
from .document_repository import DocumentRepository

__all__ = [
    'Contact',
    'ContactRepository',
    'SalesOpportunity',
    'SalesPipelineRepository',
    'Activity',
    'ActivityRepository',
    'Appointment',
    'AppointmentRepository',
    'Lead',
    'LeadRepository',
    'EmailTemplate',
    'TemplateRepository',
    'EmailCampaign',
    'CampaignRepository',
    'DashboardWidget',
    'Dashboard',
    'DashboardRepository',
    'Report',
    'AnalyticsRepository',
    'Document',
    'DocumentRepository'
]