from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *
from menu_window import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Через воду він проводить а сам з місця вік не сходить.', 'міст', 'корабель', 'кінь', 'дошка')
q2 = Question('Хоч не літак, а крилатий без крил не може працювати.', 'вітряк', 'вертоліт', 'вентилятор', '')
q3 = Question('Коли хочеш ти читати то повинен мене знати а коли мене не знаєш то нічого не вчитаєш.', 'абетка', 'книги', 'закони Нютона', 'букви')
q4 = Question('Народився із землі зарум’янивсь на вогні і з’явився на столі.', 'хліб', 'піца', 'картопля', 'буряк')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')

btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()

btn_rest.clicked.connect(rest)

def menu_generation():
    menu_win.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

window.show()
app.exec_()