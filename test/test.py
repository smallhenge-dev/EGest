from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QDateEdit, QComboBox, QPushButton, QLabel, QTextEdit
)
from PySide6.QtCore import QSize
from qt_material import apply_stylesheet
import qtawesome as qta

app = QApplication([])

# --- Appliquer un thème Material Design ---
apply_stylesheet(app, theme='light_blue.xml', parent='.qt_material_theme')


def icon_label(name):
    label = QLabel()
    label.setPixmap(qta.icon(name, color="#1976d2").pixmap(QSize(22, 22)))
    return label

# --- Fenêtre principale ---
window = QWidget()
window.setWindowTitle("Ajouter un étudiant")

main_layout = QVBoxLayout(window)

# --- Titre ---
title = QLabel("Ajouter un nouvel étudiant")
title.setStyleSheet("font-size: 20px; font-weight: bold;")
main_layout.addWidget(title)

# --- Formulaire ---
form_layout = QFormLayout()

# Nom complet
name_edit = QLineEdit()
name_edit.setPlaceholderText("Nom complet")
form_layout.addRow(icon_label("mdi.account"), name_edit)

# Date de naissance
dob_edit = QDateEdit()
dob_edit.setCalendarPopup(True)
form_layout.addRow(icon_label("mdi.calendar"), dob_edit)

# Classe / Niveau
class_combo = QComboBox()
class_combo.addItems(["6ème", "5ème", "4ème", "3ème", "2nde", "1ère", "Terminale"])
form_layout.addRow(icon_label("mdi.school"), class_combo)

# Email
email_edit = QLineEdit()
email_edit.setPlaceholderText("Emailr")
form_layout.addRow(icon_label("mdi.email"), email_edit)

# Téléphone
phone_edit = QLineEdit()
phone_edit.setPlaceholderText("Téléphone")
form_layout.addRow(icon_label("mdi.phone"), phone_edit)

# Adresse
address_edit = QTextEdit()
address_edit.setPlaceholderText("Adresse")
form_layout.addRow(icon_label("mdi.home"), address_edit)

main_layout.addLayout(form_layout)

# --- Boutons ---
save_button = QPushButton("Enregistrer")
save_button.setIcon(qta.icon("mdi.content-save", color="white"))

cancel_button = QPushButton("Annuler")
cancel_button.setIcon(qta.icon("mdi.close", color="white"))

main_layout.addWidget(save_button)
main_layout.addWidget(cancel_button)

window.setLayout(main_layout)
window.show()
app.exec()
