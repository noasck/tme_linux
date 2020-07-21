# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(280, 270, 511, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 561, 31))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 19))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 40, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(290, 80, 501, 25))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 78, 131, 21))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 110, 251, 451))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 501, 161))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Начальная строка"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.checkBox.setText(_translate("MainWindow", "Показывать промежуточные состояния? (Не рекомендуется)"))
        self.label_2.setText(_translate("MainWindow", "Список комманд: "))
        self.label_3.setText(_translate("MainWindow", "Справка по коммандам:\n"
"\n"
"1. <First state> <symbol1> <symbol2> <move:r,l,s> <Second state> \n"
"2. Вы можете использовать универсальный символ - * \n"
"    Он означает любой символ и\\или оставить\n"
"    символ \\состояние без изменения\n"
"3. Пробельный символ - \"_\"\n"
"4. Строка не ограничена.\n"
"\n"
"Конечный вывод:"))

