import sys
import asyncio

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHeaderView,
    QLabel,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from frontend.app.utils.api_client import Client


class StudentListFrame(QFrame):
    """Frame affichant la liste des étudiants."""

    def __init__(self, students=None) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setStyleSheet(
            "QFrame { background-color: #f5f7fb; border: 1px solid #dfe6ef; border-radius: 10px; }"
        )

        self.students = students or [
            {"id": 1, "nom": "Dupont", "prenom": "Alice", "matricule": "ETU-001"},
            {"id": 2, "nom": "Martin", "prenom": "Paul", "matricule": "ETU-002"},
            {"id": 3, "nom": "Diallo", "prenom": "Sali", "matricule": "ETU-003"},
        ]

        layout = QVBoxLayout(self)
        title = QLabel("Liste des étudiants")
        title.setStyleSheet("font-size: 18px; font-weight: 600; margin-bottom: 8px;")
        layout.addWidget(title)

        table = QTableWidget(len(self.students), 4)
        table.setHorizontalHeaderLabels(["ID", "Nom", "Prénom", "Matricule"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setAlternatingRowColors(True)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        for row, student in enumerate(self.students):
            table.setItem(row, 0, QTableWidgetItem(str(student["id"])))
            table.setItem(row, 1, QTableWidgetItem(student["nom"]))
            table.setItem(row, 2, QTableWidgetItem(student["prenom"]))
            table.setItem(row, 3, QTableWidgetItem(student["matricule"]))

        layout.addWidget(table)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.api = Client()
        self.setWindowTitle("EGest")
        self.resize(1100, 720)

        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        self.status_label = QLabel("Chargement...")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 24px; font-weight: 600; margin-bottom: 10px;")
        layout.addWidget(self.status_label)

        self.student_list = StudentListFrame()
        layout.addWidget(self.student_list)

        self.setCentralWidget(main_widget)

    def set_status(self, status: str) -> None:
        self.status_label.setText(status)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    try:
        response = asyncio.run(window.api.get("/health"))
        status = response.json().get("status", "API indisponible")
    except Exception:
        status = "API indisponible"

    window.set_status(status)
    exit_code = app.exec()

    try:
        asyncio.run(window.api.close())
    except RuntimeError:
        pass

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
