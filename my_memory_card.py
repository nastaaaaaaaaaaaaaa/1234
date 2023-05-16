from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QRadioButton, QMessageBox, QGroupBox, QButtonGroup
)

class Question():
    def __init__(self, text, right, wrong1, wrong2, wrong3):
        self.text = text
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 

q1 = Question("Какой национальности не существует?","Смурфы", "Энцы", "Чулымцы", "Алеуты") 
q2 = Question('Государственный язык Бразилии?', 'Португальский', 'Немецкий', 'Францусий', 'Англиский')
q3 = Question('Какого цвета нету на Российском флаге?', 'зелёный' ,'красный' , 'синий' ,'белый')
q4 = Question('Сколько будет 2 в корне?', '4' , '3' , '9' , '1')
q5 = Question('Кто из этих великих художников долго жил на Таити?', 'Гоген' , 'Дега' , 'Сезанн' , 'Матисс')
q6 = Question('Кем приходился Петр2 Петру1?', 'Внуком' , 'Племянником' , 'Сыном' , 'Братом')
questions = list()
questions.append(q1)
questions.append(q2)
questions.append(q3)
questions.append(q4)
questions.append(q5)
questions.append(q6)
app = QApplication([])

# главное окно:
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.move(100, 100)
main_win.resize(400, 200)

question = QLabel()

# область с вопросами
radiobox = QGroupBox("Варианты ответов")
answer1 = QRadioButton()
answer2 = QRadioButton()
answer3 = QRadioButton()
answer4 = QRadioButton()

answergroup = QButtonGroup()
answergroup.addButton(answer1)
answergroup.addButton(answer2)
answergroup.addButton(answer3)
answergroup.addButton(answer4)

# направляющие для области с вопросами
radioboxVline1 = QVBoxLayout()
radioboxVline2 = QVBoxLayout()
radioboxHline  = QHBoxLayout()

# "собираем конструктор" для radiobox
# (прикрепляем виджеты к направляющим)
radioboxVline1.addWidget(answer1, alignment=Qt.AlignCenter)
radioboxVline1.addWidget(answer2, alignment=Qt.AlignCenter)
radioboxVline2.addWidget(answer3, alignment=Qt.AlignCenter)
radioboxVline2.addWidget(answer4, alignment=Qt.AlignCenter)
radioboxHline.addLayout(radioboxVline1)
radioboxHline.addLayout(radioboxVline2)
radiobox.setLayout(radioboxHline)

# область с ответом
resultbox = QGroupBox("Результат теста")
correct = QLabel("Правильный ответ")
result = QLabel("Прав ты или нет")

# направляющие для области с ответом
resultHline = QHBoxLayout()
resultVline = QVBoxLayout()

resultHline.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
resultHline.addWidget(correct, alignment=Qt.AlignHCenter)
resultVline.addLayout(resultHline)
resultbox.setLayout(resultVline)

submit = QPushButton(text="Ответить")

# обработчики нажатий на кнопку
def show_result():
    radiobox.hide()
    resultbox.show()
    submit.setText("К следующему вопросу")

def show_question():
    radiobox.show()
    resultbox.hide()
    submit.setText("Ответить")
    answergroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    answergroup.setExclusive(True)

#DEPRECATED
def start_test():
    if submit.text() == "Ответить":
        show_result()
    else:
        show_question()

from random import shuffle
answers = [answer1, answer2, answer3, answer4]
def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.text)
    correct.setText(q.right)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

main_win.score = 0
def check_answer():
    if answers[0].isChecked(): 
        show_correct("Верно!")
        main_win.score += 1
    else:
        show_correct("Неверно!")
def print_stat():
    print('Статистика')
    print('Всего вопосов',main_win.total)
    print('Правельных ответов',main_win.score)
    print('рейтинг:', (main_win.score / main_win.total) * 100)

from random import randint
main_win.total = 1
def next_question():
    print_stat()
    main_win.total += 1
    cur_question = randint(0, len(questions) -1)

    ask(questions[cur_question])

def click_ok():
    if submit.text() == "Ответить":
        check_answer()
    else:
        next_question()



submit.clicked.connect(click_ok)

# "собираем конструктор" для main_win
mainVline = QVBoxLayout()
mainVline.addWidget(question)
mainVline.addWidget(radiobox)
mainVline.addWidget(resultbox)
resultbox.hide()
mainVline.addWidget(submit, alignment=Qt.AlignHCenter)

# прикрепляем "конструктор" к основному окну
main_win.setLayout(mainVline)
ask(q1)

main_win.show()
app.exec_()

