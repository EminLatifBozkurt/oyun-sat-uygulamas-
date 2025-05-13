import sys
from PyQt5.QtWidgets import QApplication
import db
from splash_screen import SplashScreen
from login_window import LoginWindow

def show_login():
    splash.close() #splash penceresini kapatır.
    global login_window
    login_window = LoginWindow() #yeni giriş penceresi oluşturur. 
    login_window.show() # pencereyi gösterir.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db.init_db() #veri tabanı oluşturduk.

    splash = SplashScreen(on_continue=show_login) #splash penceresini oluşturduk.
    splash.show()

    sys.exit(app.exec_())  # uygulama kapatılmadığı sürece döngüde.