
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import random
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

    def mousePressEvent(self, event):
        ex = event.x()
        ey = event.y()

        if abs(self.lbl.x()-ex) <= self.lbl.width() and abs(self.lbl.y()-ey) <= self.lbl.height():
            self.cnt+=1


    def nameChange(self):
        # https://gist.github.com/hoconoco/75066e0e22d01189b9718337f1e6d679
        print("Name Change")
        ret, ok = QInputDialog.getText(self, "text 입력", "글자를 입력하자")
        if ok:
            self.lbl.setText(ret)
            print(ret)

    def colorChange(self):
        print("Color Change")
        color = QColorDialog.getColor().name()
        if color:
            self.lbl.setStyleSheet("background-color:%s" % color)

    def timerEvent(self, event):
        if self.time > 10:
            self.timer.stop()
            msg = QMessageBox()
            # About messageBox, 현재 애플리케이션의 빌드 시기 or 버전을 표시하는 정보 창
            msg.about(self, "python", "1분동안 클릭 수 : " + str(self.cnt))
        self.time += 1
        # 이동
        left = random.randrange(1,self.frame.width())
        top = random.randrange(1, self.frame.height())
        self.lbl.setGeometry(QRect(left, top, 21, 16))

    def start(self):
        self.time = 0
        self.cnt = 0

        self.timer = QBasicTimer()
        self.timer.start(1000, self)



if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()