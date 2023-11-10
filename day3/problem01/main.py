from PySide6.QtWidgets import *
from PySide6.QtCore import *
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

    time = 0
    def timerEvent(self, event):
        if self.time > 100:
            #timer 종료
            self.timer.stop()
        self.time += 1
        self.progressBar.setValue(self.time)

    def download(self):
        print("download")
        self.time = 0
        self.timer = QBasicTimer()
        self.timer.start(100, self)

    def stop(self):
        print("stop")
        self.timer.stop()

    def reset(self):
        print("reset")
        self.time = 0
        self.timer.start(100,self)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()