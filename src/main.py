import sys
from pathlib import Path


from PySide6.QtWidgets import QApplication

from application.medisync_app import MediSyncApp
from gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    style_path = (
        Path(__file__).resolve().parent
        / "gui"
        / "style.qss"
    )

    with open(style_path, "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    medisync_app = MediSyncApp()

    try:
        window = MainWindow(medisync_app)
        window.showMaximized()

        sys.exit(app.exec())

    finally:
        medisync_app.close()


if __name__ == "__main__":
    main()