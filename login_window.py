from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
import db
from register_window import RegisterWindow
from store_window import StoreWindow
from admin_panel import AdminPanelWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Yap")
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
                margin-top: 8px;
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

        layout.addWidget(QLabel("🎮 Giriş Yap"))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı Adı")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)

        # İki farklı giriş butonu
        role_layout = QHBoxLayout()
        user_btn = QPushButton("👤 Kullanıcı Girişi")
        admin_btn = QPushButton("🛠️ Yönetici Girişi")
        role_layout.addWidget(user_btn)
        role_layout.addWidget(admin_btn)

        user_btn.clicked.connect(self.user_login)
        admin_btn.clicked.connect(self.admin_login)

        layout.addLayout(role_layout)

        register_btn = QPushButton("Kayıt Ol")
        register_btn.clicked.connect(self.open_register)

        layout.addWidget(register_btn)

        self.setLayout(layout)

    def user_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user = db.get_user(username, password)
        if user:
            self.store = StoreWindow(user_id=user[0])
            self.store.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hatalı Giriş", "Kullanıcı adı veya şifre yanlış.")

    def admin_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user = db.get_user(username, password)
        if user and username == "admin":
            self.admin_panel = AdminPanelWindow()
            self.admin_panel.show()
            self.close()
        elif user:
            QMessageBox.warning(self, "Yetkisiz", "Bu kullanıcı admin değil.")
        else:
            QMessageBox.warning(self, "Hatalı Giriş", "Kullanıcı adı veya şifre yanlış.")

    def open_register(self):
        self.register = RegisterWindow()
        self.register.show()
