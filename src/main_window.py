from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from src.stock_data import get_stock_data, predict_stock

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # フォントの設定（日本語に対応したフォント）
        font = QFont('MS Gothic', 12)  # フォント名を指定（Windowsの日本語フォント）
        self.setFont(font)

        # ウィンドウの設定
        self.setWindowTitle('株価予測ツール')
        self.setGeometry(100, 100, 400, 200)

        # レイアウトの作成
        layout = QVBoxLayout()

        # ティッカーシンボルラベル
        ticker_label = QLabel('ティッカーシンボル:')
        layout.addWidget(ticker_label)

        # ティッカーシンボル入力フィールド
        self.ticker_input = QLineEdit()
        layout.addWidget(self.ticker_input)

        # 予測ボタン
        predict_button = QPushButton('予測開始')
        predict_button.clicked.connect(self.on_predict_button_click)
        layout.addWidget(predict_button)

        # レイアウトをウィンドウに設定
        self.setLayout(layout)

    def on_predict_button_click(self):
        ticker = self.ticker_input.text()
        predict_stock(ticker)
