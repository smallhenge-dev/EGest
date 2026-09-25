from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QSize

class EGButton(QPushButton):
    def __init__(
            self, 
            text="",
            icon = None,
            width=None,
            height=45,
            style = "primary",
            parent=None
            ):
        super().__init__(parent)

        self.setText(text)
        self.setObjectName("egbutton")
        self.setFixedHeight(height)
        self.style = style
        if icon is not None:
            self.setIcon(icon)
            self.setIconSize(QSize(18, 18))
        if width is not None:
            self.setFixedWidth(width)
        self._contain()
        self._setup_style

    def _contain(self):
        self.setCursor(Qt.PointingHangCursor)

    def _setup_style(self):
        style = {
            "primary": """
                #egbutton {
                    background-color: ;
                    color: white;
                    border-radius: 8px;
                    padding: 10px, 18px;
                }

                #egbutton:hover {
                    backgroung-color: ;
                }

                #egbutton:pressed {
                    backgroung-color: ;
                }
            """,
            "secondary": """
                #egbutton {
                    background-color: ;
                    color: white;
                    border-radius: 8px;
                    padding: 10px, 18px;
                }

                #egbutton:hover {
                    backgroung-color: ;
                }

            """,
            "danger": """
                #egbutton {
                    background-color: ;
                    color: white;
                    border-radius: 8px;
                    padding: 10px, 18px;
                }

                #egbutton:hover {
                    backgroung-color: ;
                }
            """
        }