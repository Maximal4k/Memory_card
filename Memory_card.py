from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton,
                             QLabel, QMessageBox, QButtonGroup)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText("Наступне питання")


def show_question():
    RadioGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText("Відповідь")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q):
    shuffle(answers)
    lb_Question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_right_answer.setText(q.right_answer)
    show_question()


def click_OK():
    if "Відповідь" == btn_OK.text():
        check_answers()
    else:
        next_question()


def next_question():
    current_question = randint(0, len(questions_list)-1)
    q = questions_list[current_question]
    ask(q)


def check_answers():
    if answers[0].isChecked():
        lb_Result.setText("Відповідь правильна")
        show_result()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            lb_Result.setText("Відповідь неправильна")
            show_result()

q1 = Question('Як буде "машина" англійською мовою', "car", "bus", "taxi", "ship")
q2 = Question('Як буде "ручка" англійською мовою', "pen", "pencil", "leaf", "egg")
q3 = Question('Як англійською буде "кіт"?', 'cat', 'dog', 'cow', 'horse')
q4 = Question('Як англійською буде "книга"?', 'book', 'pen', 'table', 'window')
q5 = Question('Як англійською буде "сонце"?', 'sun', 'moon', 'star', 'cloud')
q6 = Question('Як англійською буде "вода"?', 'water', 'fire', 'air', 'stone')
q7 = Question('Як англійською буде "друг"?', 'friend', 'enemy', 'teacher', 'student')
q8 = Question('Як англійською буде "їсти"?', 'eat', 'sleep', 'run', 'read')
q9 = Question('Як англійською буде "швидкий"?', 'fast', 'slow', 'big', 'heavy')
q10 = Question('Як англійською буде "місто"?', 'city', 'village', 'forest', 'field')
questions_list = []
questions_list.extend([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')

btn_OK = QPushButton('Відповідь')
lb_Question = QLabel("Питання")

RadioGroupBox = QGroupBox("Варіанти відповідей")
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)

layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ResultGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel()
lb_right_answer = QLabel()

layout_result = QVBoxLayout()
layout_result.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_right_answer, alignment=Qt.AlignHCenter, stretch=2)
ResultGroupBox.setLayout(layout_result)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ResultGroupBox)
ResultGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


window.current_question = -1
window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400,300)
window.show()
app.exec()