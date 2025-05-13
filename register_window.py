from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import db

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kayıt Ol")
        self.resize(600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #1f1f1f;
                color: white;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
                padding: 10px;
                border-radius: 6px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 16px;
                margin-bottom: 5px;
            }
        """)

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Yeni Kullanıcı Adı")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Yeni Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)

        register_btn = QPushButton("Kaydol")
        register_btn.clicked.connect(self.register)

        layout.addWidget(QLabel("📝 Kayıt Ol"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(register_btn)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            db.add_user(username, password)
            QMessageBox.information(self, "Başarılı", "Kayıt tamamlandı. Giriş yapabilirsiniz.")
            self.close()
        else:
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen kullanıcı adı ve şifre girin.")
