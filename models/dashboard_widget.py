class DashboardWidget:
    def __init__(self, title, widget_type, data_source):
        self.title = title
        self.widget_type = widget_type  # "chart", "list", "counter"
        self.data_source = data_source  # Função que retorna os dados
        self.position = None  # Posição no dashboard
        self.is_visible = True

    def update_data(self):
        return self.data_source()

    def __str__(self):
        return f"Widget: {self.title} ({self.widget_type})"