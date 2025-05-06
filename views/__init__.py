# Views package for CRM system

from .main_view import MainView
from .contact_view import ContactView
from .sales_pipeline_view import SalesPipelineView
from .activity_view import ActivityView
from .appointment_view import AppointmentView
from .lead_view import LeadView
from .template_view import TemplateView
from .campaign_view import CampaignView
from .dashboard_view import DashboardView
from .analytics_view import AnalyticsView
from .document_view import DocumentView

__all__ = [
    'MainView',
    'ContactView',
    'SalesPipelineView',
    'ActivityView',
    'AppointmentView',
    'LeadView',
    'TemplateView',
    'CampaignView',
    'DashboardView',
    'AnalyticsView',
    'DocumentView'
]