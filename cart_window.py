from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox
from datetime import datetime
import db
from invoice_generator import generate_invoice

class CartWindow(QWidget):
    def __init__(self, user_id, cart):
        super().__init__()
        self.setWindowTitle("Sepetim")
        self.resize(600, 400)
        self.user_id = user_id
        self.cart = cart

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QListWidget {
                background-color: #2e2e2e;
                color: white;
                padding: 10px;
                border-radius: 6px;
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
        """)

        layout = QVBoxLayout()
        self.list = QListWidget()
        self.update_cart_view()

        self.remove_btn = QPushButton("🗑️ Seçiliyi Kaldır")
        self.buy_btn = QPushButton("💳 Hepsini Satın Al")

        layout.addWidget(self.list)
        layout.addWidget(self.remove_btn)
        layout.addWidget(self.buy_btn)

        self.setLayout(layout)

        self.remove_btn.clicked.connect(self.remove_item)
        self.buy_btn.clicked.connect(self.purchase_all)

    def update_cart_view(self):
        self.list.clear()
        for game in self.cart:
            self.list.addItem(f"{game[1]} - {game[2]:.2f} TL")

    def remove_item(self):
        index = self.list.currentRow()
        if index >= 0:
            removed = self.cart.pop(index)
            QMessageBox.information(self, "Kaldırıldı", f"{removed[1]} sepetten çıkarıldı.")
            self.update_cart_view()

    def purchase_all(self):
        if not self.cart:
            QMessageBox.warning(self, "Boş Sepet", "Sepetiniz boş.")
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for game in self.cart:
            db.add_purchase(self.user_id, game[0], now)

        generate_invoice(self.user_id, self.cart)
        QMessageBox.information(self, "Başarılı", "Tüm oyunlar satın alındı. Fatura oluşturuldu.")
        self.cart.clear()
        self.update_cart_view()