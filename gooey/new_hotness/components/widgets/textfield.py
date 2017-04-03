from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit

from gooey.new_hotness.components.widgets.bases import TextContainer


class TextField(TextContainer):
    widget_class = QLineEdit

    def getSublayout(self, *args, **kwargs):
        layout = QHBoxLayout()
        layout.addWidget(self.widget)
        return layout

    def setValue(self, value):
        self.widget.setText(value)

    def connectSignal(self):
        self.widget.textChanged.connect(self.dispatchChange)

    def dispatchChange(self, value, **kwargs):
        self.value.on_next({'value': value, 'id': self._id})