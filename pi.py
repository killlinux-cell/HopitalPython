from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class PatientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des patients")

        # Widgets pour ajouter un patient
        patient_form_layout = QVBoxLayout()
        patient_form_layout.addWidget(QLabel("Ajouter un patient"))
        self.patient_name = QLineEdit()
        patient_form_layout.addWidget(QLabel("Nom :"))
        patient_form_layout.addWidget(self.patient_name)
        self.patient_age = QLineEdit()
        patient_form_layout.addWidget(QLabel("Age :"))
        patient_form_layout.addWidget(self.patient_age)
        self.patient_gender = QLineEdit()
        patient_form_layout.addWidget(QLabel("Sexe :"))
        patient_form_layout.addWidget(self.patient_gender)
        add_patient_button = QPushButton("Ajouter le patient")
        add_patient_button.clicked.connect(self.add_patient)
        patient_form_layout.addWidget(add_patient_button)
        patient_form_widget = QWidget()
        patient_form_widget.setLayout(patient_form_layout)

        # Tableau pour afficher la liste des patients
        self.patient_table = QTableWidget()
        self.patient_table.setColumnCount(4)
        self.patient_table.setHorizontalHeaderLabels(["Nom", "Age", "Sexe", "ID patient"])
        self.patient_table.horizontalHeader().setStretchLastSection(True)
        self.load_patients()
        patient_table_widget = QWidget()
        patient_table_layout = QVBoxLayout()
        patient_table_layout.addWidget(self.patient_table)
        patient_table_widget.setLayout(patient_table_layout)

        # Ajouter les widgets au layout principal
        main_layout = QHBoxLayout()
        main_layout.addWidget(patient_form_widget)
        main_layout.addWidget(patient_table_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def add_patient(self):
        # Récupérer les informations saisies par l'utilisateur
        name = self.patient_name.text()
        age = self.patient_age.text()
        gender = self.patient_gender.text()

        # Ajouter le patient à la table
        row_position = self.patient_table.rowCount()
        self.patient_table.insertRow(row_position)
        self.patient_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.patient_table.setItem(row_position, 1, QTableWidgetItem(age))
        self.patient_table.setItem(row_position, 2, QTableWidgetItem(gender))
        self.patient_table.setItem(row_position, 3, QTableWidgetItem(str(row_position + 1)))

        # Effacer les champs de saisie
        self.patient_name.clear()
        self.patient_age.clear()
        self.patient_gender.clear()

    def load_patients(self):
        # Charger les patients à partir de la base de données
        # Dans cet exemple, nous allons ajouter 3 patients de test
        patients = [("Jean Dupont", "35", "Homme"),
                    ("Marie Martin", "28", "Femme"),
                    ("Lucie Dubois", "45", "Femme")]

        for i, patient in enumerate(patients):
            row_position = self.patient_table.rowCount()
            self.patient_table.insertRow(row_position)
            self.patient_table.setItem(row_position, 0, QTableWidgetItem(patient[0]))
            self.patient_table.setItem(row_position, 1, QTableWidgetItem(patient[1]))
            self.patient_table.setItem(row_position, 2, QTableWidgetItem(patient[2]))
            self.patient_table.setItem(row_position, 3, QTableWidgetItem(str(i + 1)))


if __name__ == "__main__":
    app = QApplication([])
    window = PatientWindow()
    window.show()
    app.exec_()
