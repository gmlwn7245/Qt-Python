
from PySide6.QtWidgets import *
# mainUI.py 파일을 Ui_MainWindow Class import 한다.
# 파일명이 mainUI.py 가 아닌 경우 변경해야 한다.
from mainUI import Ui_MainWindow


# Ui_MainWindow class 도 상속한다.
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Ui를 Ui_MainWindow에서 갖고온다.
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def ledON(self):
        self.lcdNumber.display("ON")
        print("ON")

    def ledOFF(self):
        self.lcdNumber.display("OFF")
        print("ON")

    def setDial(self, num):
        self.lcdNumber.display(num)
        #print(num)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()