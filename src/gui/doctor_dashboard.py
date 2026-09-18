from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class DoctorDashboard(QWidget):
    def __init__(self, app, stack):
        super().__init__()

        self.app = app
        self.stack = stack

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard do Médico")

        description = QLabel(
            "Aqui será possível consultar a fila "
            "e atender pacientes."
        )

        back_button = QPushButton("Voltar")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(back_button)
        layout.addStretch()

        back_button.clicked.connect(
            self.go_back
        )

    def go_back(self):
        self.stack.setCurrentIndex(0)