# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SatSolver.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# Author : Iman Kianian
# Logic

from PyQt5 import QtCore, QtGui, QtWidgets
import string
import itertools
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SatSolver")
        MainWindow.resize(673, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.TextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.TextBox.setGeometry(QtCore.QRect(250, 220, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextBox.setFont(font)
        self.TextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox.setObjectName("TextBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.TextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(30, 426, 611, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TextEdit.setFont(font)
        self.TextEdit.setUndoRedoEnabled(False)
        self.TextEdit.setReadOnly(True)
        self.TextEdit.setObjectName("TextEdit")
        self.OuputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OuputLabel.setGeometry(QtCore.QRect(40, 370, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(16)
        self.OuputLabel.setFont(font)
        self.OuputLabel.setObjectName("OuputLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.satsolve)
        self.OuputLabel.setHidden(True)
        self.TextEdit.setHidden(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def satsolve(self):

        expression = self.TextBox.text()
        expression = expression.replace(' ', '')
        expression = expression.replace('v', '∨')
        expression = expression.replace('^', '∧')
        expression = expression.replace('~', '¬')
        correctvariablelist = list(string.ascii_lowercase)
        correctvariablelist.remove('v')
        variablelist = []
        Interpretations = []
        for i in range(len(expression)):
            if (expression[i] in correctvariablelist and expression[i] not in variablelist):
                variablelist.append(expression[i])
        Interpretations = []
        for roll in itertools.product([0, 1], repeat=len(variablelist)):
            Interpretations.append(roll)

        flag = False
        stri = 'Your Expression is Satisfiable with : \n'
        for i in range(len(Interpretations)):
            exp = expression

            for j in range(len(variablelist)):
                var = variablelist[j]
                exp = exp.replace(var, str(Interpretations[i][j]))

            while exp != '0' and exp != '1':
                # for T or F
                exp = exp.replace('F', '0')
                exp = exp.replace('T', '1')
                # for ¬
                exp = exp.replace('¬(1)', '(0)')
                exp = exp.replace('¬(0)', '(1)')

                while '¬1' in exp or '¬0' in exp:
                    exp = exp.replace('¬1', '0')
                    exp = exp.replace('¬0', '1')
                # for ∨
                exp = exp.replace('(1∨0)', '(1)')
                exp = exp.replace('(0∨1)', '(1)')
                exp = exp.replace('(1∨1)', '(1)')
                exp = exp.replace('(0∨0)', '(0)')

                # for ∧
                exp = exp.replace('(1∧1)', '(1)')
                exp = exp.replace('(1∧0)', '(0)')
                exp = exp.replace('(0∧1)', '(0)')
                exp = exp.replace('(0∧0)', '(0)')

                # for >
                exp = exp.replace('(1>1)', '(1)')
                exp = exp.replace('(0>1)', '(1)')
                exp = exp.replace('(0>0)', '(1)')
                exp = exp.replace('(1>0)', '(0)')

                # for <>
                exp = exp.replace('(1<>1)', '(1)')
                exp = exp.replace('(0<>0)', '(1)')
                exp = exp.replace('(1<>0)', '(0)')
                exp = exp.replace('(0<>1)', '(0)')

                # Others
                exp = exp.replace('1∨0', '1')
                exp = exp.replace('0∨1', '1')
                exp = exp.replace('1∨1', '1')
                exp = exp.replace('0∨0', '0')
                exp = exp.replace('1∧1', '1')
                exp = exp.replace('1∧0', '0')
                exp = exp.replace('0∧1', '0')
                exp = exp.replace('0∧0', '0')
                exp = exp.replace('1>1', '1')
                exp = exp.replace('0>1', '1')
                exp = exp.replace('0>0', '1')
                exp = exp.replace('1>0', '0')
                exp = exp.replace('1<>1', '1')
                exp = exp.replace('0<>0', '1')
                exp = exp.replace('1<>0', '0')
                exp = exp.replace('0<>1', '0')

                exp = exp.replace('(1)', '1')
                exp = exp.replace('(0)', '0')

            if exp == '1':
                self.OuputLabel.setStyleSheet('color:green;')
                self.OuputLabel.setHidden(False)
                for k in range(len(variablelist)):
                    print(variablelist[k], " : ", Interpretations[i][k])
                    stri+=(str(variablelist[k])+" : "+ str(Interpretations[i][k])+'\t')

                stri+=',\n'
                flag = True
                MainWindow.resize(673, 732)
                self.TextEdit.setText(stri)
                self.TextEdit.setHidden(False)

        if flag == False:
            self.OuputLabel.setStyleSheet('color:red;')
            self.OuputLabel.setText('This Expression is Not Satisfiable')
            MainWindow.resize(673, 450)
            self.TextEdit.setHidden(True)
            self.OuputLabel.setHidden(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SatSolver", "SatSolver"))
        self.label.setText(_translate("MainWindow", "Enter Your Expression : "))
        self.label_2.setText(_translate("MainWindow", "AND : ^ or ∧"))
        self.label_3.setText(_translate("MainWindow", "OR   :  v or ∨"))
        self.label_4.setText(_translate("MainWindow", "NOT :  ~ or  ¬"))
        self.label_5.setText(_translate("MainWindow", "Then :  >"))
        self.label_6.setText(_translate("MainWindow", "IFF  :  <>"))
        self.OuputLabel.setText(_translate("MainWindow", "Your Expression is Satisfiable  "))
        self.pushButton.setText(_translate("MainWindow", "Check Expression"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

