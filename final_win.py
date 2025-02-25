from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self, correct_answers, elapsed_time):
        super().__init__()
        self.correct_answers = correct_answers
        self.elapsed_time = elapsed_time
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Результаты теста")
        self.initUI()
        self.show()

    def initUI(self):
        layout = QVBoxLayout()

        result_text = f"Вы правильно ответили на {self.correct_answers} вопросов из 15."
        time_text = f"Затраченное время: {self.elapsed_time}."

        layout.addWidget(QLabel(result_text))
        layout.addWidget(QLabel(time_text))

        self.btn_back = QPushButton("Назад", self)
        layout.addWidget(self.btn_back)

        self.setLayout(layout)

        self.btn_back.clicked.connect(self.go_back)

    def go_back(self):
        from my_app import MainWin
        self.main_win = MainWin()
        self.close()