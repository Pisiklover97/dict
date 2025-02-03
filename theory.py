from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from second_win import TestWin

class TheoryWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Теоретический материал")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.theory_text = QTextEdit(self)
        self.theory_text.setReadOnly(True)  # Запрещаем редактирование
        self.theory_text.setPlainText(
            "Теория по словарям в Python:\n\n"
            "1. Объявление словаря:\n"
            "   - Пустой словарь: `books = dict()`"
            "   - Словарь с элементами: `books = {'поэма': 'Руслан и Людмила', 'сказка': 'Волшебное кольцо'}`\n\n"
            "2. Получение элемента по ключу:\n"
            "   - genre = input('Введите жанр:')\n"
            "   print('Рекомендация:', books[genre])\n\n"
            "3. Добавление и изменение элементов:\n"
            "   - Добавить элемент: `dict[key] = value`\n"
            "   - Изменить элемент: `dict[key] = new_value`\n\n"
            "4. Удаление элементов:\n"
            "   - Удалить по ключу: `del dict[key]` или `dict.pop(key)`\n\n"
            "5. Проверка наличия ключа:\n"
            "   - `key in dict` возвращает `True`, если ключ существует\n\n"
            "6. Получение элементов словаря:\n"
            "   - Ключи: `dict.keys()`\n"
            "   - Значения: `dict.values()`\n"
            "   - Пары ключ-значение: `dict.items()`\n\n"
            "7. Объединение словарей:\n"
            "   - `dict1.update(dict2)` или `{**dict1, **dict2}`\n\n"
            "8. Генераторы словарей:\n"
            "   - `{key: value for key, value in iterable}`\n\n"
            "9. Сортировка словаря:\n"
            "   - По ключам: `sorted(dict.keys())` или `dict(sorted(dict.items()))`\n\n"
            "10. Печать словаря целиком:\n"
            "   - print(books)\n\n"
            "Изучите материал и нажмите 'Перейти к тесту', чтобы начать."
        )

        self.btn_next = QPushButton("Перейти к тесту", self)

        layout = QVBoxLayout()
        layout.addWidget(self.theory_text)
        layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(layout)
#Добавленный Тест win
    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)