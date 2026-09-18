from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ReceptionDashboard(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard da Recepção")

        description = QLabel(
            "Aqui será possível gerir pacientes, "
            "consultas e fila de atendimento."
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
        self.parent().setCurrentIndex(0)