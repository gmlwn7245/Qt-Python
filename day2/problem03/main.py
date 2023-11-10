
from PySide6.QtWidgets import *
# mainUI.py 파일을 Ui_MainWindow Class import 한다.
# 파일명이 mainUI.py 가 아닌 경우 변경해야 한다.
from mainUI import Ui_MainWindow
from pushDialog import Ui_PushDialog

# Ui_MainWindow class 도 상속한다.
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Ui를 Ui_MainWindow에서 갖고온다.
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def nameChange(self):
        #https://gist.github.com/hoconoco/75066e0e22d01189b9718337f1e6d679
        print("Name Change")
        ret, ok = QInputDialog.getText(self, "text 입력", "글자를 입력하자")
        if ok:
            self.lbl.setText(ret)
            print(ret)

    def colorChange(self):
        print("Color Change")
        color = QColorDialog.getColor().name()
        if color:
            self.frame.setStyleSheet("background-color:%s" % color)

    def start(self):
        msg = QMessageBox()
        # About messageBox, 현재 애플리케이션의 빌드 시기 or 버전을 표시하는 정보 창
        msg.about(self, "python", "1분동안 클릭 수 : 0")
        # 이건 내일
        



if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()