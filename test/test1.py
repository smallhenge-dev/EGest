from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QDateEdit, QComboBox, QTextEdit,
    QPushButton, QLabel, QFrame, QFileDialog, QSizePolicy, QScrollArea
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from qt_material import apply_stylesheet
import qtawesome as qta
import sys

app = QApplication(sys.argv)
apply_stylesheet(app, theme='light_blue.xml') # Base Material claire

# --- QSS Custom pour ressembler à l'image ---
app.setStyleSheet(app.styleSheet() + """
    QWidget {
        background-color: #F8F9FA;
        font-family: 'Segoe UI';
    }
    QFrame#card {
        background-color: white;
        border-radius: 16px;
        padding: 20px;
    }
    QLabel#title {
        font-size: 22px;
        font-weight: 600;
        color: #1F2937;
    }
    QLabel#section_title {
        font-size: 16px;
        font-weight: 600;
        color: #1F2937;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    QLabel#field_label {
        font-size: 13px;
        font-weight: 500;
        color: #4B5563;
        margin-bottom: 4px;
    }
    QLineEdit, QDateEdit, QComboBox, QTextEdit {
        border: 1px solid #D1D5DB;
        border-radius: 6px;
        padding: 8px;
        font-size: 14px;
        background-color: white;
        min-height: 28px;
    }
    QLineEdit:focus, QDateEdit:focus, QComboBox:focus, QTextEdit:focus {
        border: 2px solid #3B82F6; /* Bleu au focus comme l'image */
    }
    QPushButton#btn_primary {
        background-color: #3B82F6;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: 600;
        font-size: 14px;
    }
    QPushButton#btn_primary:hover { background-color: #2563EB; }
    QPushButton#btn_secondary {
        background-color: #F3F4F6;
        color: #374151;
        border: 1px solid #D1D5DB;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: 600;
        font-size: 14px;
    }
    QPushButton#btn_secondary:hover { background-color: #E5E7EB; }
    QLabel#avatar {
        border: 2px solid #E5E7EB;
        border-radius: 60px;
    }
""")

# --- Fenêtre principale ---
window = QWidget()
window.setWindowTitle("Ajouter un étudiant")
window.resize(700, 650)
window.setMinimumSize(720, 420)

main_layout = QVBoxLayout(window)
main_layout.setContentsMargins(30, 30, 30, 30)

# --- Card Blanche ---
card = QFrame()
card.setObjectName("card")
card_layout = QVBoxLayout(card)

# --- Header ---
header = QHBoxLayout()
icon_title = QLabel()
icon_title.setPixmap(qta.icon('mdi6.account-circle', color='#3B82F6').pixmap(32, 32))
title = QLabel("Ajouter un étudiant")
title.setObjectName("title")
header.addWidget(icon_title)
header.addWidget(title)
header.addStretch()
card_layout.addLayout(header)

line = QFrame()
line.setFrameShape(QFrame.HLine)
line.setStyleSheet("background-color: #E5E7EB;")
card_layout.addWidget(line)

# --- Corps : Formulaire + Avatar ---
body_layout = QHBoxLayout()
body_layout.setSpacing(24)

# Colonne Gauche : Formulaire
form_widget = QWidget()
form_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
form_layout = QVBoxLayout(form_widget)
form_layout.setSpacing(18)

def add_field(label_text, icon_name, widget):
    container = QVBoxLayout()
    container.setSpacing(8)
    label = QLabel(label_text)
    label.setObjectName("field_label")
    label.setPixmap(qta.icon(icon_name, color='#4B5563').pixmap(16, 16))
    h = QHBoxLayout()
    h.addWidget(label)
    h.addStretch()
    container.addLayout(h)
    container.addWidget(widget)
    form_layout.addLayout(container)

# Champs Etudiant
student_name = QLineEdit()
add_field("Nom complet", "mdi6.account", student_name)

student_dob = QDateEdit()
student_dob.setDisplayFormat("dd/MM/yyyy")
student_dob.setCalendarPopup(True)
add_field("Date de naissance", "mdi6.calendar", student_dob)

student_class = QComboBox()
student_class.addItems(["Sélectionner", "6ème", "5ème", "4ème", "3ème"])
add_field("Classe / Niveau", "mdi6.school", student_class)

student_email = QLineEdit()
student_email.setPlaceholderText("example@email.com")
add_field("Email", "mdi6.email", student_email)

student_phone = QLineEdit()
add_field("Téléphone", "mdi6.phone", student_phone)

form_separator = QFrame()
form_separator.setFrameShape(QFrame.HLine)
form_separator.setStyleSheet("background-color: #E5E7EB;")
form_layout.addWidget(form_separator)

# Section Tuteur
section_tuteur = QLabel("Informations du tuteur")
section_tuteur.setObjectName("section_title")
section_tuteur.setPixmap(qta.icon('mdi6.account-tie', color='#1F2937').pixmap(20, 20))
form_layout.addWidget(section_tuteur)

tuteur_name = QLineEdit()
add_field("Nom du tuteur", "mdi6.account", tuteur_name)

row1 = QHBoxLayout()
row1.setSpacing(16)
tuteur_lien = QLineEdit()
tuteur_lien.setPlaceholderText("Ex: Père, Mère...")
v1 = QVBoxLayout()
v1.setSpacing(8)
tuteur_lien_label = QLabel("Lien avec l'étudiant")
tuteur_lien_label.setObjectName("field_label")
v1.addWidget(tuteur_lien_label)
v1.addWidget(tuteur_lien)
tuteur_phone = QLineEdit()
v2 = QVBoxLayout()
v2.setSpacing(8)
tuteur_phone_label = QLabel("Téléphone du tuteur")
tuteur_phone_label.setObjectName("field_label")
v2.addWidget(tuteur_phone_label)
v2.addWidget(tuteur_phone)
row1.addLayout(v1)
row1.addLayout(v2)
form_layout.addLayout(row1)

row2 = QHBoxLayout()
row2.setSpacing(16)
tuteur_adresse = QTextEdit()
tuteur_adresse.setPlaceholderText("Saisir l'adresse du tuteur...")
tuteur_adresse.setFixedHeight(60)
v3 = QVBoxLayout()
v3.setSpacing(8)
adresse_label = QLabel("Adresse")
adresse_label.setObjectName("field_label")
v3.addWidget(adresse_label)
v3.addWidget(tuteur_adresse)
tuteur_adresse2 = QTextEdit()
tuteur_adresse2.setFixedHeight(60)
v4 = QVBoxLayout()
v4.setSpacing(8)
adresse_tuteur_label = QLabel("Adresse du tuteur")
adresse_tuteur_label.setObjectName("field_label")
v4.addWidget(adresse_tuteur_label)
v4.addWidget(tuteur_adresse2)
row2.addLayout(v3)
row2.addLayout(v4)
form_layout.addLayout(row2)

body_layout.addWidget(form_widget, 3)

# Colonne Droite : Avatar
avatar_layout = QVBoxLayout()
avatar_layout.setAlignment(Qt.AlignTop)
avatar = QLabel()
avatar.setObjectName("avatar")
avatar.setFixedSize(120, 120)
avatar.setPixmap(qta.icon('mdi6.account-circle', color='#9CA3AF').pixmap(120, 120))
avatar.setAlignment(Qt.AlignCenter)

def import_avatar():
    image_path, _ = QFileDialog.getOpenFileName(
        window,
        "Choisir une image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp *.webp)"
    )
    if not image_path:
        return

    image = QPixmap(image_path)
    if not image.isNull():
        avatar.setPixmap(image.scaled(
            avatar.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        ))

btn_import = QPushButton("Importer une image")
btn_import.setObjectName("btn_secondary")
btn_import.setFixedWidth(145)
btn_import.clicked.connect(import_avatar)

avatar_layout.addWidget(avatar, alignment=Qt.AlignCenter)
avatar_layout.addWidget(btn_import, alignment=Qt.AlignCenter)
avatar_widget = QWidget()
avatar_widget.setFixedWidth(180)
avatar_widget.setLayout(avatar_layout)
body_layout.addWidget(avatar_widget)
body_layout.setStretch(0, 1)
body_layout.setStretch(1, 0)

card_layout.addLayout(body_layout)

# --- Boutons du bas ---
btn_layout = QHBoxLayout()
btn_layout.addStretch()
btn_save = QPushButton("Enregistrer")
btn_save.setObjectName("btn_primary")
btn_save.setIcon(qta.icon('mdi6.content-save', color='white'))
btn_save.setIconSize(QSize(20, 20))
btn_cancel = QPushButton("Annuler")
btn_cancel.setObjectName("btn_secondary")
btn_cancel.setIcon(qta.icon('mdi6.close', color='#374151'))
btn_cancel.setIconSize(QSize(20, 20))
btn_layout.addWidget(btn_save)
btn_layout.addWidget(btn_cancel)
card_layout.addLayout(btn_layout)

card.setMinimumHeight(card.sizeHint().height())
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)
scroll_area.setFrameShape(QFrame.NoFrame)
scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
scroll_area.setWidget(card)
main_layout.addWidget(scroll_area)
window.show()
sys.exit(app.exec())