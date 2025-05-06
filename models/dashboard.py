class Dashboard:
    def __init__(self, name):
        self.name = name
        self.widgets = []

    def add_widget(self, widget):
        widget.position = len(self.widgets) + 1
        self.widgets.append(widget)

    def remove_widget(self, position):
        if 1 <= position <= len(self.widgets):
            self.widgets.pop(position - 1)
            self._update_positions()
            return True
        return False

    def _update_positions(self):
        for i, widget in enumerate(self.widgets, 1):
            widget.position = i

    def __str__(self):
        return f"Dashboard: {self.name} ({len(self.widgets)} widgets)"