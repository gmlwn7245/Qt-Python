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
    addT = 0
    speed = 1

    def timerEvent(self, event):
        if self.pb.value() <= 0 or self.pb.value() >= 100:
            #timer 종료
            self.timer.stop()
            print("종료됨")
        self.time += self.addT
        self.pb.setValue(self.time)
        print(self.time)


    def upClicked(self):
        print("up clicked")
        self.timer.stop()


    def upPressed(self):
        print("up pressed")
        self.addT = -1
        self.time = self.pb.value()
        self.timer = QBasicTimer()
        self.timer.start(1000/self.speed, self)

    def downPressed(self):
        print("dw pressed")
        self.addT = 1
        self.time = self.pb.value()
        self.timer = QBasicTimer()
        self.timer.start(1000/self.speed, self)

    def downClicked(self):
        print("dw clicked")
        self.timer.stop()

    def stop(self):
        print("stop")
        self.timer.stop()


    def slide(self):
        print("reset")
        self.speed = self.slider.value()+1

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()