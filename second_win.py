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
                "options": [  "dict.remove(key)", "del dict[key]", "dict.delete(key)", "dict.pop(key)"],
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
                "question": "6. Что выведет следующий код?\n\n"
                            "d = {'a': 1, 'b': 2, 'c': 3}\n"
                            "print(d.get('d', 4))",
                "options": [
                    "Ошибка, так как ключ 'd' отсутствует",
                    "None",
                    "4",
                    "Выведет {'d': 4}"
                ],
                "answer": ["4"]
            },
            {
                "question": "7. Что произойдет при выполнении следующего кода?\n\n"
                            "d = {'x': 10, 'y': 20}\n"
                            "d.update({'z': 30})\n"
                            "print(d)",
                "options": [
                    "Ошибка, метод update() не существует",
                    "{'x': 10, 'y': 20, 'z': 30}",
                    "{'x': 10, 'y': 20}",
                    "Будет добавлена пара ('z', 30), но print() ничего не выведет"
                ],
                "answer": ["{'x': 10, 'y': 20, 'z': 30}"]
            },
            {
                "question": "8. Что произойдет при выполнении следующего кода?\n\n"
                            "d = {'a': 5, 'b': 10}\n"
                            "del d['b']\n"
                            "print(d)",
                "options": [
                    "Ошибка, так как нельзя удалять элементы из словаря",
                    "{'a': 5}",
                    "{'a': 5, 'b': 10}",
                    "Ключ 'b' будет удалён, но print() ничего не выведет"
                ],
                "answer": ["{'a': 5}"]
            },
            {
                "question": "9. Что выведет следующий код?\n\n"
                            "d = {'apple': 2, 'banana': 3}\n"
                            "print('apple' in d)",
                "options": [
                    "True",
                    "False",
                    "None",
                    "Ошибка"
                ],
                "answer": ["True"]
            },
            {
                "question": "10. Какой результат выдаст следующий код?\n\n"
                            "d = {'x': 1, 'y': 2, 'z': 3}\n"
                            "print(list(d.keys()))",
                "options": [
                    "['x', 'y', 'z']",
                    "{'x', 'y', 'z'}",
                    "dict_keys(['x', 'y', 'z'])",
                    "Ошибка"
                ],
                "answer": ["['x', 'y', 'z']"]
            },
            {
                "question": "11. Какой результат будет у следующего кода?\n\n"
                            "d = {'x': 1, 'y': 2}\n"
                            "print(d.pop('x'))",
                "options": [
                    "1",
                    "{'y': 2}",
                    "Ошибка, метод pop() не поддерживается",
                    "None"
                ],
                "answer": ["1"]
            },
            {
                "question": "12. Что произойдет при выполнении следующего кода?\n\n"
                            "d = {'a': 1, 'b': 2}\n"
                            "print(d.items())",
                "options": [
                    "[('a', 1), ('b', 2)]",
                    "dict_items([('a', 1), ('b', 2)])",
                    "{('a', 1), ('b', 2)}",
                    "Ошибка"
                ],
                "answer": ["dict_items([('a', 1), ('b', 2)])"]
            },
            {
                "question": "13. Что делает следующий код?\n\n"
                            "d1 = {'a': 1, 'b': 2}\n"
                            "d2 = {'c': 3, 'd': 4}\n"
                            "d = {**d1, **d2}\n"
                            "print(d)",
                "options": [
                    "Объединяет d1 и d2, результат {'a': 1, 'b': 2, 'c': 3, 'd': 4}",
                    "Ошибка, так как нельзя объединять словари таким способом",
                    "Создаёт новый пустой словарь",
                    "Выдаст None"
                ],
                "answer": ["Объединяет d1 и d2, результат {'a': 1, 'b': 2, 'c': 3, 'd': 4}"]
            },
            {
                "question": "14. Что выведет следующий код?\n\n"
                            "d = {x: x**2 for x in range(3)}\n"
                            "print(d)",
                "options": [
                    "{0: 0, 1: 1, 2: 4}",
                    "{0: 1, 1: 2, 2: 3}",
                    "{0: 0, 1: 2, 2: 6}",
                    "Ошибка"
                ],
                "answer": ["{0: 0, 1: 1, 2: 4}"]
            },
            {
                "question": "15. Какой результат выдаст следующий код?\n\n"
                            "d = {'a': 3, 'b': 1, 'c': 2}\n"
                            "print(dict(sorted(d.items())))",
                "options": [
                    "{'a': 3, 'b': 1, 'c': 2}",
                    "{'b': 1, 'c': 2, 'a': 3}",
                    "{'c': 2, 'b': 1, 'a': 3}",
                    "Ошибка"
                ],
                "answer": ["{'a': 3, 'b': 1, 'c': 2}"]
            }
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



        self.btn_next = QPushButton("Далее", self)
        self.layout.addWidget(self.btn_next)

        self.btn_back = QPushButton("Назад", self)
        self.layout.addWidget(self.btn_back)

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
        self.fw.show()
        self.close()  # Закрываем текущее окно

    def connects(self):
        self.btn_next.clicked.connect(self.next_question)
        self.btn_back.clicked.connect(self.previous_question)