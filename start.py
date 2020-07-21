import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import mte
from core import *


class ExampleApp(QtWidgets.QMainWindow, mte.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushed)

    def pushed(self):
        machine = TM(self.plainTextEdit_2.toPlainText(), initial_str=self.plainTextEdit.toPlainText(), max_len=20,
                     verbose=bool(self.checkBox.isChecked()))
        result = machine.run()

        self.textBrowser.setText(result.res_str )
        self.textBrowser.append("Steps: " + str(result.steps) + " Time: (s) " + str(result.time_elapsed))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()