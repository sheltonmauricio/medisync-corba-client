from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDateTimeEdit
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QComboBox,
    QMessageBox,
    QFormLayout,
)


class ReceptionDashboard(QWidget):
    def __init__(self, app, stack):
        super().__init__()

        self.app = app
        self.stack = stack

        self.setObjectName("receptionDashboard")

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            40,
            30,
            40,
            30,
        )

        main_layout.setSpacing(20)

        # Cabeçalho
        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        title = QLabel("Área da Recepção")
        title.setObjectName("sectionTitle")

        subtitle = QLabel(
            "Gestão de pacientes e atendimento hospitalar"
        )
        subtitle.setObjectName("sectionSubtitle")

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        back_button = QPushButton("Voltar")
        back_button.setObjectName("secondaryButton")
        back_button.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        header_layout.addWidget(back_button)

        main_layout.addLayout(header_layout)

        # Cartão de agendamento
        appointment_card = QFrame()
        appointment_card.setObjectName("card")

        appointment_layout = QVBoxLayout(
            appointment_card
        )

        appointment_layout.setContentsMargins(
            20,
            18,
            20,
            18,
        )

        appointment_layout.setSpacing(10)

        appointment_title = QLabel(
            "Agendar consulta"
        )

        appointment_title.setObjectName(
            "sectionTitle"
        )

        appointment_layout.addWidget(
            appointment_title
        )

        appointment_form = QFormLayout()
        appointment_form.setSpacing(8)

        self.appointment_patient_id_input = QLineEdit()
        self.appointment_patient_id_input.setPlaceholderText(
            "ID do paciente"
        )

        self.appointment_doctor_input = QLineEdit()
        self.appointment_doctor_input.setPlaceholderText(
            "Nome do médico"
        )

        self.appointment_date_input = QDateTimeEdit()
        self.appointment_date_input.setCalendarPopup(
            True
        )

        self.appointment_date_input.setDateTime(
            QDateTime.currentDateTime()
        )

        self.appointment_date_input.setDisplayFormat(
            "yyyy-MM-dd HH:mm"
        )

        self.appointment_specialty_input = QLineEdit()
        self.appointment_specialty_input.setPlaceholderText(
            "Ex.: Clínica Geral"
        )

        appointment_form.addRow(
            "ID do paciente:",
            self.appointment_patient_id_input,
        )

        appointment_form.addRow(
            "Médico:",
            self.appointment_doctor_input,
        )

        appointment_form.addRow(
            "Data e hora:",
            self.appointment_date_input,
        )

        appointment_form.addRow(
            "Especialidade:",
            self.appointment_specialty_input,
        )

        appointment_layout.addLayout(
            appointment_form
        )

        appointment_actions = QHBoxLayout()

        schedule_button = QPushButton(
            "Agendar consulta"
        )

        schedule_button.setObjectName(
            "successButton"
        )

        schedule_button.clicked.connect(
            self.schedule_appointment
        )

        clear_appointment_button = QPushButton(
            "Limpar"
        )

        clear_appointment_button.setObjectName(
            "secondaryButton"
        )

        clear_appointment_button.clicked.connect(
            self.clear_appointment_form
        )

        appointment_actions.addWidget(
            schedule_button
        )

        appointment_actions.addWidget(
            clear_appointment_button
        )

        appointment_actions.addStretch()

        appointment_layout.addLayout(
            appointment_actions
        )

        # Cartão de registo
        register_card = QFrame()
        register_card.setObjectName("card")

        register_layout = QVBoxLayout(register_card)
        register_layout.setContentsMargins(20, 18, 20, 18)
        register_layout.setSpacing(10)

        register_title = QLabel("Registar paciente")
        register_title.setObjectName("sectionTitle")

        register_layout.addWidget(register_title)

        form_layout = QFormLayout()
        form_layout.setSpacing(8)

        self.full_name_input = QLineEdit()
        self.full_name_input.setPlaceholderText(
            "Nome completo do paciente"
        )

        self.birth_date_input = QLineEdit()
        self.birth_date_input.setPlaceholderText(
            "Ex.: 2000-05-20"
        )

        self.gender_input = QComboBox()
        self.gender_input.addItems(
            [
                "Seleccione o género",
                "Masculino",
                "Feminino",
                "Outro",
            ]
        )

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText(
            "Contacto telefónico"
        )

        form_layout.addRow(
            "Nome completo:",
            self.full_name_input,
        )

        form_layout.addRow(
            "Data de nascimento:",
            self.birth_date_input,
        )

        form_layout.addRow(
            "Género:",
            self.gender_input,
        )

        form_layout.addRow(
            "Telefone:",
            self.phone_input,
        )

        register_layout.addLayout(form_layout)

        actions_layout = QHBoxLayout()

        register_button = QPushButton(
            "Registar paciente"
        )
        register_button.setObjectName("successButton")
        register_button.clicked.connect(
            self.register_patient
        )

        clear_button = QPushButton("Limpar")
        clear_button.setObjectName("secondaryButton")
        clear_button.clicked.connect(
            self.clear_form
        )

        actions_layout.addWidget(register_button)
        actions_layout.addWidget(clear_button)
        actions_layout.addStretch()

        register_layout.addLayout(actions_layout)

        forms_layout = QHBoxLayout()
        forms_layout.setSpacing(20)

        appointment_card.setMinimumHeight(260)
        register_card.setMinimumHeight(260)

        forms_layout.addWidget(
            appointment_card,
            1,
        )

        forms_layout.addWidget(
            register_card,
            1,
        )

        main_layout.addLayout(
            forms_layout
        )

        # Cartão da lista
        patients_card = QFrame()
        patients_card.setObjectName("card")

        patients_layout = QVBoxLayout(patients_card)
        patients_layout.setContentsMargins(25, 25, 25, 25)
        patients_layout.setSpacing(15)

        patients_header = QHBoxLayout()

        patients_title = QLabel("Pacientes registados")
        patients_title.setObjectName("sectionTitle")

        refresh_button = QPushButton("Actualizar")
        refresh_button.setObjectName("secondaryButton")
        refresh_button.clicked.connect(
            self.load_patients
        )

        patients_header.addWidget(patients_title)
        patients_header.addStretch()
        patients_header.addWidget(refresh_button)

        patients_layout.addLayout(patients_header)

        self.patients_table = QTableWidget()
        self.patients_table.setColumnCount(5)
        self.patients_table.setHorizontalHeaderLabels(
            [
                "ID",
                "Nome completo",
                "Nascimento",
                "Género",
                "Telefone",
            ]
        )

        self.patients_table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.patients_table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.patients_table.horizontalHeader().setStretchLastSection(
            True
        )

        patients_layout.addWidget(
            self.patients_table
        )

        main_layout.addWidget(
            patients_card,
            1,
        )

        self.load_patients()

    def register_patient(self):
        full_name = self.full_name_input.text().strip()
        birth_date = self.birth_date_input.text().strip()
        gender_index = self.gender_input.currentIndex()
        phone = self.phone_input.text().strip()

        if not full_name:
            self.show_error(
                "Introduza o nome completo do paciente."
            )
            return

        if not birth_date:
            self.show_error(
                "Introduza a data de nascimento."
            )
            return

        if gender_index == 0:
            self.show_error(
                "Seleccione o género do paciente."
            )
            return

        if not phone:
            self.show_error(
                "Introduza o contacto telefónico."
            )
            return

        gender = self.gender_input.currentText()

        try:
            patient = self.app.register_patient(
                full_name,
                birth_date,
                gender,
                phone,
            )

            QMessageBox.information(
                self,
                "Sucesso",
                (
                    "Paciente registado com sucesso.\n\n"
                    f"ID atribuído: {patient.id}"
                ),
            )

            self.clear_form()
            self.load_patients()

        except Exception as error:
            self.show_error(
                f"Não foi possível registar o paciente:\n{error}"
            )

    def schedule_appointment(self):
        patient_id_text = (
            self.appointment_patient_id_input
            .text()
            .strip()
        )

        doctor = (
            self.appointment_doctor_input
            .text()
            .strip()
        )

        specialty = (
            self.appointment_specialty_input
            .text()
            .strip()
        )

        appointment_date = (
            self.appointment_date_input
            .dateTime()
            .toString("yyyy-MM-dd HH:mm")
        )

        if not patient_id_text:
            self.show_error(
                "Introduza o ID do paciente."
            )
            return

        if not patient_id_text.isdigit():
            self.show_error(
                "O ID do paciente deve ser numérico."
            )
            return

        if not doctor:
            self.show_error(
                "Introduza o nome do médico."
            )
            return

        if not specialty:
            self.show_error(
                "Introduza a especialidade."
            )
            return

        patient_id = int(patient_id_text)

        try:
            appointment = self.app.schedule_appointment(
                patient_id,
                doctor,
                appointment_date,
                specialty,
            )

            QMessageBox.information(
                self,
                "Sucesso",
                (
                    "Consulta agendada com sucesso.\n\n"
                    f"ID da consulta: {appointment.id}"
                ),
            )

            self.clear_appointment_form()

        except Exception as error:
            self.show_error(
                (
                    "Não foi possível agendar a consulta:\n"
                    f"{error}"
                )
            )


    def clear_appointment_form(self):
        self.appointment_patient_id_input.clear()
        self.appointment_doctor_input.clear()
        self.appointment_specialty_input.clear()

        self.appointment_date_input.setDateTime(
            QDateTime.currentDateTime()
        )

    def load_patients(self):
        try:
            patients = self.app.list_patients()

            self.patients_table.setRowCount(
                len(patients)
            )

            for row, patient in enumerate(patients):
                values = [
                    patient.id,
                    patient.fullName,
                    patient.birthDate,
                    patient.gender,
                    patient.phone,
                ]

                for column, value in enumerate(values):
                    item = QTableWidgetItem(
                        str(value)
                    )

                    self.patients_table.setItem(
                        row,
                        column,
                        item,
                    )

            self.patients_table.resizeColumnsToContents()

        except Exception as error:
            self.show_error(
                f"Não foi possível carregar os pacientes:\n{error}"
            )

    def clear_form(self):
        self.full_name_input.clear()
        self.birth_date_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.phone_input.clear()

    def show_error(self, message: str):
        QMessageBox.critical(
            self,
            "Erro",
            message,
        )