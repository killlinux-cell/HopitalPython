# pour la base de donnée SQLlite

import sqlite3

class PatientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des patients")

        # ...
        # Code pour ajouter les widgets à la fenêtre
        # ...

        # Connexion à la base de données SQLite
        self.db_connection = sqlite3.connect("patients.db")
        self.cursor = self.db_connection.cursor()

        # Création de la table patients si elle n'existe pas
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS patients 
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                age INTEGER,
                                gender TEXT)""")
        self.db_connection.commit()

    def add_patient(self):
        # Récupérer les informations saisies par l'utilisateur
        name = self.patient_name.text()
        age = self.patient_age.text()
        gender = self.patient_gender.text()

        # Ajouter le patient à la table
        self.cursor.execute("INSERT INTO patients (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
        self.db_connection.commit()

        # Actualiser la table des patients
        self.load_patients()

        # Effacer les champs de saisie
        self.patient_name.clear()
        self.patient_age.clear()
        self.patient_gender.clear()

    def load_patients(self):
        # Charger les patients à partir de la base de données
        self.patient_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM patients")
        patients = self.cursor.fetchall()

        for i, patient in enumerate(patients):
            row_position = self.patient_table.rowCount()
            self.patient_table.insertRow(row_position)
            self.patient_table.setItem(row_position, 0, QTableWidgetItem(patient[1]))
            self.patient_table.setItem(row_position, 1, QTableWidgetItem(str(patient[2])))
            self.patient_table.setItem(row_position, 2, QTableWidgetItem(patient[3]))
            self.patient_table.setItem(row_position, 3, QTableWidgetItem(str(patient[0])))


# Ajouter

class PatientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des patients")

        # ...
        # Code pour ajouter les widgets à la fenêtre
        # ...

        # Connexion à la base de données SQLite
        self.db_connection = sqlite3.connect("patients.db")
        self.cursor = self.db_connection.cursor()

        # Création de la table patients si elle n'existe pas
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS patients 
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                age INTEGER,
                                gender TEXT)""")
        self.db_connection.commit()

        # Connecter le champ de recherche à la fonction de recherche
        self.search_bar.textChanged.connect(self.search_patients)

    def search_patients(self):
        search_text = self.search_bar.text()

        # Charger les patients qui correspondent à la recherche
        self.patient_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM patients WHERE name LIKE ? OR id LIKE ?", ('%' + search_text + '%', '%' + search_text + '%'))
        patients = self.cursor.fetchall()

        for i, patient in enumerate(patients):
            row_position = self.patient_table.rowCount()
            self.patient_table.insertRow(row_position)
            self.patient_table.setItem(row_position, 0, QTableWidgetItem(patient[1]))
            self.patient_table.setItem(row_position, 1, QTableWidgetItem(str(patient[2])))
            self.patient_table.setItem(row_position, 2, QTableWidgetItem(patient[3]))
            self.patient_table.setItem(row_position, 3, QTableWidgetItem(str(patient[0])))
