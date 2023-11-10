from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainUI import Ui_MainWindow
from time import sleep

# QThread를 상속 받은 class 생성
class MyThread(QThread):
    mySignal = Signal(int)
    def __init__(self):
        super().__init__()

    flag = False

    # thread 가 start() 되면, 동작하는 함수
    def run(self):
        self.flag = True
        value = 0
        while self.flag and value < 100:
            self.mySignal.emit(value)
            value += 1
            sleep(0.1)
        self.stop()

    # thread 가 stop() 되면, 동작하는수함수
    def stop(self):
        self.flag = False
        print("Thread Stop")


# Ui_MainWindow class 도 상속한다.
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Ui를 Ui_MainWindow에서 갖고온다.
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def download(self):
        self.th = MyThread()
        self.th.start()
        self.th.mySignal.connect(self.settingUI)

    def settingUI(self, val):
        self.progressBar.setValue(val)
        self.progressBar_2.setValue(val)
        self.progressBar_3.setValue(val)
        self.progressBar_4.setValue(val)
        self.progressBar_5.setValue(val)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()