import sys
from PyQt5.QtWidgets import QApplication
from src.ui_elements import MyWindow  # ui_elements.py からインポート

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
