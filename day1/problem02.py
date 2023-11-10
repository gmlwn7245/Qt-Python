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

    def addName(self):
        name = self.edit.text()
        self.msg = QMessageBox()
        if (name in self.nameArr) or len(name) == 0 or len(self.nameArr) == 10:
            self.msg.setText("사용할 수 없는 이름입니다.")
        else:
            self.msg.setText("추가되었습니다.")
            self.nameArr.append(name)
        self.msg.exec()

    def removeName(self):
        name = self.edit.text()
        self.msg = QMessageBox()

        if len(name) == 0 or len(self.nameArr) == 0 or name not in self.nameArr:
            self.msg.setText("제거할 수 없습니다.")
        else:
            self.msg.setText("제거되었습니다.")
            self.nameArr.remove(name)

        self.msg.exec()

    def exitFrame(self):
        quit()


    def main(self):
        self.setWindowTitle("My")
        self.setGeometry(0, 0, 300, 300)

        # 이름 리스트 저장 변수
        self.nameArr = []

        # mainWidget에 등록할 vlayout
        self.vlay = QVBoxLayout()

        # 화면 구성 요소들
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&메뉴")
        self.menuExit = self.menu.addMenu("&종료")

        self.form = QFormLayout(self)
        self.edit = QLineEdit()

        self.btn1 = QPushButton("추가")
        self.btn2 = QPushButton("제거")

        # 버튼 이벤트 함수
        self.btn1.clicked.connect(self.addName)
        self.btn2.clicked.connect(self.removeName)

        # 버튼 나란히 정렬
        hlay = QHBoxLayout()
        hlay.addWidget(self.btn1)
        hlay.addWidget(self.btn2)

        self.form.addRow("name", self.edit)
        self.form.addRow(hlay)


        self.vlay.addLayout(self.form)
        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # 메뉴탭
        self.openAction1 = QAction("&추가", self)
        self.openAction2 = QAction("&제거", self)
        self.openAction3 = QAction("&프로그램종료", self)

        # 이벤트 함수
        self.openAction1.triggered.connect(self.addName)
        self.openAction2.triggered.connect(self.removeName)
        self.openAction3.triggered.connect(self.exitFrame)

        self.menuFile.addAction(self.openAction1)
        self.menuFile.addAction(self.openAction2)
        self.menuExit.addAction(self.openAction3)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
