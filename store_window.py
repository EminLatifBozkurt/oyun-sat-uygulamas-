from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox, QLabel
from datetime import datetime
import db
from invoice_generator import generate_invoice
from cart_window import CartWindow

class StoreWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.setWindowTitle("Oyun Mağazası")
        self.resize(600, 400)
        self.user_id = user_id
        self.cart = []
        self.games = db.get_all_games()

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QListWidget {
                background-color: #2e2e2e;
                padding: 10px;
                border-radius: 6px;
                color: white;
            }
            QPushButton {
                background-color: #4caf50;
                padding: 10px;
                border-radius: 6px;
                margin-top: 8px;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 18px;
                padding: 10px 0;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("🎮 Mevcut Oyunlar"))

        self.list = QListWidget()
        for game in self.games:
            self.list.addItem(f"{game[1]}   ---->      {game[2]:.2f} TL")
        layout.addWidget(self.list)

        self.add_btn = QPushButton("➕ Sepete Ekle")
        self.cart_btn = QPushButton("🛒 Sepeti Gör")
        self.back_btn = QPushButton("🔙 Geri Dön")


        self.add_btn.clicked.connect(self.add_to_cart)
        self.cart_btn.clicked.connect(self.open_cart)
        self.back_btn.clicked.connect(self.go_back) 

        layout.addWidget(self.add_btn)
        layout.addWidget(self.cart_btn)
        layout.addWidget(self.back_btn)

        self.setLayout(layout)

    def add_to_cart(self):
        selected = self.list.currentRow()
        if selected >= 0:
            self.cart.append(self.games[selected])
            QMessageBox.information(self, "Sepet", f"{self.games[selected][1]} sepete eklendi.")

    def open_cart(self):
        self.cart_window = CartWindow(self.user_id, self.cart)
        self.cart_window.show()

    def purchase(self):
        if not self.cart:
            QMessageBox.warning(self, "Boş", "Sepetiniz boş.")
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for game in self.cart:
            db.add_purchase(self.user_id, game[0], now)

        generate_invoice(self.user_id, self.cart)
        QMessageBox.information(self, "Başarılı", "Satın alma tamamlandı. Fatura oluşturuldu.")
        self.cart.clear()

    def go_back(self):
     from login_window import LoginWindow
     self.close()
     self.login = LoginWindow()
     self.login.show()