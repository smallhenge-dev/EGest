from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QAbstractButton


class Kpi(QFrame):

    def __init__(self, title="", icon=None, text="", evolution=None):
        super.__init__()
        self.content()
        self.title = title
        self.icon = icon
        self.label = text
        self.evolutionv = evolution

    def content(self):
        content = QVBoxLayout(self)
        IconBox = QHBoxLayout(content)
        LabelBox = QVBoxLayout(IconBox)
        LabelBox.addWidget(QLabel(self.title))
        LabelBox.addWidget(QLabel(self.label))
        IconBox.addWidget()