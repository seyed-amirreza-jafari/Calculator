from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.resize(350, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_box = QtWidgets.QLabel(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(5, 10, 340, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.output_box.setFont(font)
        self.output_box.setFrameShape(QtWidgets.QFrame.Box)
        self.output_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_box.setLineWidth(1)
        self.output_box.setMidLineWidth(0)
        self.output_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_box.setIndent(10)
        self.output_box.setObjectName("output_box")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('%'))
        self.percent_button.setGeometry(QtCore.QRect(10, 120, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")
        self.devide_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('/'))
        self.devide_button.setGeometry(QtCore.QRect(265, 120, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.devide_button.setFont(font)
        self.devide_button.setObjectName("devide_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.backspace())
        self.arrow_button.setGeometry(QtCore.QRect(180, 120, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('C'))
        self.clear_button.setGeometry(QtCore.QRect(95, 120, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('7'))
        self.seven_button.setGeometry(QtCore.QRect(10, 196, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('*'))
        self.multiply_button.setGeometry(QtCore.QRect(265, 196, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('9'))
        self.nine_button.setGeometry(QtCore.QRect(180, 196, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('8'))
        self.eight_button.setGeometry(QtCore.QRect(95, 196, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('4'))
        self.four_button.setGeometry(QtCore.QRect(10, 272, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('-'))
        self.minus_button.setGeometry(QtCore.QRect(265, 272, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('6'))
        self.six_button.setGeometry(QtCore.QRect(180, 272, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('5'))
        self.five_button.setGeometry(QtCore.QRect(95, 272, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.minus_add_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.minus_plus_clicked())
        self.minus_add_button.setGeometry(QtCore.QRect(10, 424, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus_add_button.setFont(font)
        self.minus_add_button.setObjectName("minus_add_button")
        self.point_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.point_clicked())
        self.point_button.setGeometry(QtCore.QRect(180, 424, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.point_button.setFont(font)
        self.point_button.setObjectName("point_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('0'))
        self.zero_button.setGeometry(QtCore.QRect(95, 424, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.answer())
        self.equal_button.setGeometry(QtCore.QRect(265, 424, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('1'))
        self.one_button.setGeometry(QtCore.QRect(10, 348, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('3'))
        self.three_button.setGeometry(QtCore.QRect(180, 348, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('2'))
        self.two_button.setGeometry(QtCore.QRect(95, 348, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.add_button = QtWidgets.QPushButton(self.centralwidget,
        clicked = lambda: self.button_clicked('+'))
        self.add_button.setGeometry(QtCore.QRect(265, 348, 75, 66))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def answer(self):
        screen = self.output_box.text()

        try:
            answer = eval(screen)
            self.output_box.setText(str(answer))
        except:
            self.output_box.setText('Error!')

    def minus_plus_clicked(self):
        screen = self.output_box.text()

        flag = 0
        final_list = list()
        
        if screen[0] == '-':
            flag = 0
        else:
            flag = 1

        words_screen = screen.split('+')
        for word in words_screen:
            if '-' in word:
                word_screen = word.split('-')
                final_list.append('+'.join(word_screen))
            else:
                final_list.append(word)
            
        screen = '-'.join(final_list)

        if flag == 1:
            screen = '-' + screen

        self.output_box.setText(screen)

    def backspace(self):
        screen = self.output_box.text()
        screen = screen[:-1]

        self.output_box.setText(screen)
    def point_clicked(self):
        screen = self.output_box.text()

        flag = 0

        screen = screen[::-1]

        for string in screen:
            if string == '.':
                flag = 1
            elif string == '+' or string == '-' or string == '/' or string == '%' or string == '*':
                break
        screen = screen[::-1]

        if flag == 1:
            pass
        else:
            self.output_box.setText(f'{screen}.')

    def button_clicked(self, pressed):
        screen = self.output_box.text()
        if screen == 'Error!':
            self.output_box.setText(pressed)
        else:
            if pressed == 'C':
                self.output_box.setText('0')
            else:
                if self.output_box.text() == '0':
                    self.output_box.setText('')
                self.output_box.setText(f'{self.output_box.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_box.setText(_translate("MainWindow", "0"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.devide_button.setText(_translate("MainWindow", "/"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.multiply_button.setText(_translate("MainWindow", "X"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.minus_add_button.setText(_translate("MainWindow", "+/-"))
        self.point_button.setText(_translate("MainWindow", "."))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.add_button.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
