from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
class SplashScreen(QWidget):
    def __init__(self, on_continue):
        super().__init__()
        
        layout = QVBoxLayout()
        logo = QLabel()
        pixmap = QPixmap("logo.png").scaled(120, 120)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)
        self.setWindowTitle("Hoş Geldiniz")
        self.resize(600,400)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
                font-size: 16px;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)


        title = QLabel("🎮 Oyun Mağazasına Hoş Geldiniz")
        title.setAlignment(Qt.AlignCenter)

        continue_btn = QPushButton("Devam Et")
        continue_btn.clicked.connect(on_continue)

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(continue_btn, alignment=Qt.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)