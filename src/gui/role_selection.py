from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class RoleSelection(QWidget):
    reception_selected = Signal()
    doctor_selected = Signal()

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            80,
            60,
            80,
            60,
        )

        main_layout.setSpacing(12)

        title = QLabel("MediSync")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(
            "Sistema de Gestão de Atendimento Hospitalar"
        )
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        main_layout.addStretch()
        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addSpacing(40)

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(24)

        reception_card = self.create_role_card(
            "Recepção",
            "Gestão de pacientes, consultas e fila.",
            self.reception_selected,
        )

        doctor_card = self.create_role_card(
            "Médico",
            "Gestão da fila e atendimento de pacientes.",
            self.doctor_selected,
        )

        cards_layout.addWidget(reception_card)
        cards_layout.addWidget(doctor_card)

        main_layout.addLayout(cards_layout)
        main_layout.addStretch()

    def create_role_card(
        self,
        title: str,
        description: str,
        signal,
    ) -> QFrame:

        card = QFrame()
        card.setObjectName("card")

        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            30,
            30,
            30,
            30,
        )

        layout.setSpacing(16)

        role_title = QLabel(title)
        role_title.setAlignment(Qt.AlignCenter)

        role_description = QLabel(description)
        role_description.setAlignment(Qt.AlignCenter)
        role_description.setWordWrap(True)

        button = QPushButton(
            f"Entrar como {title}"
        )

        button.clicked.connect(
            signal.emit
        )

        layout.addWidget(role_title)
        layout.addWidget(role_description)
        layout.addSpacing(10)
        layout.addWidget(button)

        return card