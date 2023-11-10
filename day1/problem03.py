# QFormLayout 샘플코드
# Form 레이아웃은 text와 함께 widget을 추가 할 수 있다.
# Form 형식의 App 개발 시 개발속도를 단축시켜준다.
# .addRow() : text와 함께 widget을 추가하는 API

from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def openMessage(self):
        self.bar.showMessage("open 메뉴 클릭")

    def saveMessage(self):
        self.bar.showMessage("save 메뉴 클릭")

    def helpMessage(self):
        self.bar.showMessage("help 메뉴 클릭")

    def saveasMessage(self):
        self.bar.showMessage("save as 메뉴 클릭")


    def main(self):
        self.setWindowTitle("하하호호 메모장")
        self.setGeometry(0, 0, 300, 300)

        # mainWidget에 등록할 vlayout
        self.vlay = QVBoxLayout()

        # 화면 구성 요소들
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&File")
        self.menuExit = self.menu.addMenu("&Help")

        self.bar = self.statusBar()

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # 메뉴탭
        self.openAction1 = QAction("&Open", self)
        self.openAction1.setShortcut(QKeySequence("Ctrl+O"))

        self.openAction2 = QAction("&Save", self)
        self.openAction2.setShortcut(QKeySequence("Ctrl+S"))

        self.openAction3 = QAction("&Save As...", self)
        self.openAction3.setShortcut(QKeySequence("Ctrl+Shift+S"))

        self.openAction4 = QAction("&Close", self)
        self.openAction5 = QAction("&About", self)

        # 이벤트 함수
        self.openAction1.triggered.connect(self.openMessage)
        self.openAction2.triggered.connect(self.saveMessage)
        self.openAction3.triggered.connect(self.saveasMessage)
        self.openAction4.triggered.connect(self.close)
        self.openAction5.triggered.connect(self.helpMessage)

        self.menuFile.addAction(self.openAction1)
        self.menuFile.addAction(self.openAction2)
        self.menuFile.addAction(self.openAction3)
        self.menuFile.addAction(self.openAction4)
        self.menuExit.addAction(self.openAction5)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
