from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import rcParams
from .stock_predictor import predict_stock_data

# 日本語フォントの設定
rcParams['font.family'] = 'MS Gothic'

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('株価予測ツール')
        self.setGeometry(100, 100, 800, 600)

        # レイアウトの作成
        self.layout = QVBoxLayout()

        # ラベル: タイトル
        self.title_label = QLabel('株価予測ツール')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # ユーザー入力フォーム
        self.input_layout = QHBoxLayout()

        # シンボル入力
        self.symbol_label = QLabel('株式シンボル:')
        self.input_layout.addWidget(self.symbol_label)
        self.symbol_input = QLineEdit(self)
        self.input_layout.addWidget(self.symbol_input)

        # 日付範囲入力
        self.date_label = QLabel('日付範囲 (例: 2023-01-01 to 2023-12-31):')
        self.input_layout.addWidget(self.date_label)
        self.date_input = QLineEdit(self)
        self.input_layout.addWidget(self.date_input)

        self.layout.addLayout(self.input_layout)

        # グラフを表示するキャンバス
        self.canvas = FigureCanvas(plt.figure())
        self.layout.addWidget(self.canvas)

        # 予測ボタン
        self.predict_button = QPushButton('株価予測を表示')
        self.predict_button.clicked.connect(self.plot_graph)  # plot_graph メソッドを接続
        self.layout.addWidget(self.predict_button)

        # 予測結果の表示エリア
        self.result_label = QLabel('予測結果:')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def plot_graph(self):  # plot_graph メソッドがここに定義されていることを確認
        # ユーザーの入力から株式シンボルと日付範囲を取得
        symbol = self.symbol_input.text()
        date_range = self.date_input.text()

        # 日付範囲の解析
        try:
            start_date, end_date = date_range.split(" to ")
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
        except ValueError:
            self.result_label.setText('日付範囲の形式が不正です。正しい形式で入力してください。')
            return

        # 株価予測のデータを取得
        dates, actual_prices, predicted_prices = predict_stock_data(symbol, start_date, end_date)

        # グラフの描画
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)

        # 実際の株価と予測株価をプロット
        ax.plot(dates, actual_prices, label='実際の株価')
        ax.plot(dates, predicted_prices, label='予測株価', color='orange')

        # タイトルや軸ラベル
        ax.set_title(f'{symbol} 株価予測', fontsize=14)
        ax.set_xlabel('日付', fontsize=12)
        ax.set_ylabel('株価 (円)', fontsize=12)
        ax.legend(fontsize=12)

        # グラフを描画
        self.canvas.draw()

