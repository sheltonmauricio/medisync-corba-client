from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class ReceptionDashboard(QWidget):
    def __init__(self, app, stack):
        super().__init__()

        self.app = app
        self.stack = stack

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard da Recepção")

        description = QLabel(
            "Gestão de pacientes, consultas e fila de atendimento."
        )

        refresh_button = QPushButton(
            "Actualizar pacientes"
        )

        back_button = QPushButton("Voltar")

        self.patient_table = QTableWidget()
        self.patient_table.setColumnCount(5)
        self.patient_table.setHorizontalHeaderLabels(
            [
                "ID",
                "Nome",
                "Data de nascimento",
                "Género",
                "Telefone",
            ]
        )

        self.patient_table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(refresh_button)
        layout.addWidget(self.patient_table)
        layout.addWidget(back_button)

        refresh_button.clicked.connect(
            self.load_patients
        )

        back_button.clicked.connect(
            self.go_back
        )

        self.load_patients()

    def load_patients(self):
        patients = self.app.list_patients()

        self.patient_table.setRowCount(
            len(patients)
        )

        for row, patient in enumerate(patients):
            self.patient_table.setItem(
                row,
                0,
                QTableWidgetItem(str(patient.id)),
            )

            self.patient_table.setItem(
                row,
                1,
                QTableWidgetItem(patient.fullName),
            )

            self.patient_table.setItem(
                row,
                2,
                QTableWidgetItem(patient.birthDate),
            )

            self.patient_table.setItem(
                row,
                3,
                QTableWidgetItem(patient.gender),
            )

            self.patient_table.setItem(
                row,
                4,
                QTableWidgetItem(patient.phone),
            )

        self.patient_table.resizeColumnsToContents()

    def go_back(self):
        self.stack.setCurrentIndex(0)