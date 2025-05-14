from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QLabel
import db

class AdminPanelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎮 Yönetici Paneli")
        self.resize(600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #2e2e2e;
                color: white;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #2196f3;
                color: white;
                padding: 10px;
                border-radius: 6px;
                margin-top: 5px;
            }
            QPushButton:hover {
                background-color: #1976d2;
            }
            QListWidget {
                background-color: #2e2e2e;
                color: white;
                border-radius: 6px;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
                padding-bottom: 5px;
            }
        """)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("🎯 Mevcut Oyunlar"))

        self.game_list = QListWidget()
        self.refresh_games()
        layout.addWidget(self.game_list)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Oyun Adı")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Fiyat")

        add_button = QPushButton("➕ Oyun Ekle")
        delete_button = QPushButton("🗑️ Seçili Oyunu Sil")
        logout_button = QPushButton("🚪 Çıkış Yap")

        add_button.clicked.connect(self.add_game)
        delete_button.clicked.connect(self.delete_game)
        logout_button.clicked.connect(self.logout)

        layout.addWidget(self.name_input)
        layout.addWidget(self.price_input)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(logout_button)
        self.setLayout(layout)

    def refresh_games(self):
        self.game_list.clear()
        games = db.get_all_games()
        for game in games:
            self.game_list.addItem(f"{game[0]}. {game[1]} - {game[2]:.2f} TL")

    def add_game(self):
        name = self.name_input.text()
        try:
            price = float(self.price_input.text())
        except ValueError:
            QMessageBox.warning(self, "Hata", "Geçerli bir fiyat girin.")
            return

        if name and price >= 0:
            db.add_game(name, price)
            QMessageBox.information(self, "Başarılı", f"{name} oyunu eklendi.")
            self.name_input.clear()
            self.price_input.clear()
            self.refresh_games()
        else:
            QMessageBox.warning(self, "Eksik Bilgi", "Tüm alanları doldurun.")

    def delete_game(self):
        selected_index = self.game_list.currentRow()
        games = db.get_all_games()

        if selected_index < 0 or selected_index >= len(games):
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek için bir oyun seçin.")
            return

        game_id = games[selected_index][0]
        try:
            db.delete_game(game_id)
            QMessageBox.information(self, "Silindi", "Oyun başarıyla silindi.")
            self.refresh_games()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Silme işlemi başarısız: {str(e)}")
    def logout(self):
     reply = QMessageBox.question(self, "Çıkış", "Çıkmak istiyor musunuz?", QMessageBox.Yes | QMessageBox.No)
     if reply == QMessageBox.Yes:
        from login_window import LoginWindow
        self.close()
        self.login = LoginWindow()
        self.login.show()