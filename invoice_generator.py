from reportlab.pdfgen import canvas # pdf için kullanılır
from reportlab.lib.pagesizes import A4 # pdf A4 olsun
import os
import db
from datetime import datetime # fatura isim ve tarihi için

def generate_invoice(user_id, games):
    if not games:
        return

    user = db.get_user_by_id(user_id)
    if not user:
        return

    username = user[1]
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{username}_fatura_{now}.pdf"
    output_dir = "invoices" #klasör yoksa klasör oluşturur
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename) # pdf yolu

    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)# faturada yazacak şeyler ve stilleri.
    c.drawString(50, height - 50, "Satın Alma Faturası")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Müşteri: {username}")
    c.drawString(50, height - 100, f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.line(50, height - 110, width - 50, height - 110)

    y = height - 140
    total = 0
    for i, game in enumerate(games, 1):# ödeme tutar hesabı
        name, price = game[1], game[2]
        c.drawString(50, y, f"{i}. {name} - {price} TL")
        total += price
        y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Toplam: {total:.2f} TL")

    c.save()
    print(f"Fatura kaydedildi: {filepath}")
