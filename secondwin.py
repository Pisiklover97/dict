from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Тест по словарям")
        self.initUI()
        self.connects()
        self.show()

    def update_timer(self):
        self.time_elapsed = self.time_elapsed.addSecs(1)  # Увеличиваем время на 1 секунду
        self.timer_label.setText(self.time_elapsed.toString("mm:ss"))

    def initUI(self):
        self.questions = [
            {
                "question": "1. Как создать пустой словарь в Python?",
                "options": ["dict()", "{}", "[]", "set()"],
                "answer": ["dict()", "{}"]
            },
            {
                "question": "2. Как добавить элемент в словарь?",
                "options": ["dict[key] = value", "dict.add(key, value)", "dict.insert(key, value)", "dict.append(key, value)"],
                "answer": ["dict[key] = value"]
            },
            {
                "question": "3. Как удалить элемент из словаря по ключу?",
                "options": ["del dict[key]", "dict.pop(key)", "dict.remove(key)", "dict.delete(key)"],
                "answer": ["del dict[key]", "dict.pop(key)"]
            },
            {
                "question": "4. Как проверить, существует ли ключ в словаре?",
                "options": ["key in dict", "dict.has_key(key)", "dict.contains(key)", "dict.exists(key)"],
                "answer": ["key in dict"]
            },
            {
                "question": "5. Как получить список всех ключей словаря?",
                "options": ["dict.keys()", "dict.get_keys()", "dict.all_keys()", "dict.keys"],
                "answer": ["dict.keys()"]
            },
            {
                "question": "6. Как получить список всех значений словаря?",
                "options": ["dict.values()", "dict.get_values()", "dict.all_values()", "dict.values"],
                "answer": ["dict.values()"]
            },
            {
                "question": "7. Как получить список пар ключ-значение из словаря?",
                "options": ["dict.items()", "dict.get_items()", "dict.all_items()", "dict.items"],
                "answer": ["dict.items()"]
            },
            {
                "question": "8. Как объединить два словаря в один?",
                "options": ["dict1.update(dict2)", "{**dict1, **dict2}", "dict1 + dict2", "dict1.merge(dict2)"],
                "answer": ["dict1.update(dict2)", "{**dict1, **dict2}"]
            },
            {
                "question": "9. Как создать словарь с помощью генератора словаря?",
                "options": ["{key: value for key, value in iterable}", "dict((key, value) for key, value in iterable)", "dict.fromkeys(iterable)", "dict.generate(key, value)"],
                "answer": ["{key: value for key, value in iterable}"]
            },
            {
                "question": "10. Как отсортировать словарь по ключам?",
                "options": ["sorted(dict.keys())", "dict(sorted(dict.items()))", "dict.sort()", "dict.order_by_key()"],
                "answer": ["sorted(dict.keys())", "dict(sorted(dict.items()))"]
            },
        ]

        self.current_question_index = 0
        self.answers = []  # Список для хранения выбранных ответов

        self.layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.current_question_index]["question"])
        self.layout.addWidget(self.question_label)

        # Добавляем радиокнопки для текущего вопроса
        self.radio_buttons = []
        for option in self.questions[self.current_question_index]["options"]:
            radio_button = QRadioButton(option)
            self.layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)

        self.btn_back = QPushButton("Назад", self)
        self.layout.addWidget(self.btn_back)

        self.btn_next = QPushButton("Далее", self)
        self.layout.addWidget(self.btn_next)

        self.setLayout(self.layout)

        # Таймер
        self.time_elapsed = QTime(0, 0, 0)
        self.timer_label = QLabel("00:00", self)
        self.layout.addWidget(self.timer_label, alignment=Qt.AlignCenter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def next_question(self):
        selected_button = None
        for button in self.radio_buttons:
            if button.isChecked():
                selected_button = button.text()
                break

        if selected_button:
            self.answers.append(selected_button)
        else:
            self.answers.append(None)

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.update_question()
        else:
            self.check_answers()

    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.update_question()

    def update_question(self):
        self.question_label.setText(self.questions[self.current_question_index]["question"])

        for i, button in enumerate(self.radio_buttons):
            if i < len(self.questions[self.current_question_index]["options"]):
                button.setText(self.questions[self.current_question_index]["options"][i])
                button.setChecked(False)
            else:
                button.setText("")
                button.setChecked(False)

    def check_answers(self):
        correct_answers = sum(
            1 for i, q in enumerate(self.questions)
            if self.answers[i] in q["answer"]
        )

        elapsed_time = self.time_elapsed.toString("mm:ss")  # Конвертация времени

        self.fw = FinalWin(correct_answers, elapsed_time)
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_question)
        self.btn_back.clicked.connect(self.previous_question)