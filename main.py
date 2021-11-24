import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        inpt = ['b_' + str(i) for i in range(10)]
        for i in range(10):
            setattr(self, inpt[i], QPushButton(str(i), self))
            self.hbox_first.addWidget(getattr(self, inpt[i]))

        frst = ['b_' + str(i) for i in 'plus minus mult dev dot'.split()]
        c = '+-*/.'
        for i in range(len(frst)):
            setattr(self, frst[i], QPushButton(c[i], self))
            self.hbox_first.addWidget(getattr(self, frst[i]))

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_c = QPushButton("C", self)
        self.hbox_first.addWidget(self.b_c)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_dev.clicked.connect(lambda: self._operation("/"))

        self.b_result.clicked.connect(self._result)

        self.b_c.clicked.connect(self._clear)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_dot.clicked.connect(lambda: self._button("."))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
        except:
            self.input.setText("Сперва введите число, а только потом операцию. Воспользуйтесь кнопкой очистки C")

    def _clear(self):
        self.input.setText('')
        self.op = ''
        self.num_1 = .0
        self.num_2 = .0

    def _result(self):
        try:
            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))

            if self.op == "/":
                if self.num_2 == "0":
                    self.input.setText(str('cant devide by 0'))
                else:
                    self.input.setText(str(self.num_1 / self.num_2))
        except:
            self.input.setText('Вы не ввели второе число. Воспользуйтесь кнопкой очистки C')


app = QApplication(sys.argv)

win = Calculator()
win.show()
sys.exit(app.exec_())