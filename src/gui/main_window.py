from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from gui.role_selection import RoleSelection
from gui.reception_dashboard import ReceptionDashboard
from gui.doctor_dashboard import DoctorDashboard


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.setWindowTitle("MediSync")
        self.resize(900, 600)

        self.app = app

        self.stack = QStackedWidget()

        self.role_selection = RoleSelection()
        self.reception_dashboard = ReceptionDashboard(app)
        self.doctor_dashboard = DoctorDashboard(app)

        self.stack.addWidget(
            self.role_selection
        )

        self.stack.addWidget(
            self.reception_dashboard
        )

        self.stack.addWidget(
            self.doctor_dashboard
        )

        self.role_selection.reception_selected.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        self.role_selection.doctor_selected.connect(
            lambda: self.stack.setCurrentIndex(2)
        )

        self.setCentralWidget(self.stack)