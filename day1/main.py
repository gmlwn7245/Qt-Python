# QFormLayout 샘플코드
# Form 레이아웃은 text와 함께 widget을 추가 할 수 있다.
# Form 형식의 App 개발 시 개발속도를 단축시켜준다.
# .addRow() : text와 함께 widget을 추가하는 API

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def clickBtn1(self):
        print(self.edit2.text())
        L = int(str(self.edit2.text()))
        if L <= 30 or L >= 1:
            self.lbl.setVisible(True)
            return True
        else:
            self.lbl.setVisible(False)
            return False

    def clickBtn2(self):
        name = len(self.edit1.text())
        age = int(str(self.edit2.text()))
        self.msg = QMessageBox()
        if name < 1 or name > 4:
            self.msg.setText("이름이 너무 깁니다.")
            self.msg.exec()
        elif self.clickBtn1:
            self.msg.setText("회원가입 성공!")
            self.msg.exec()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.edit1 = QTextEdit()
        self.btn1 = QPushButton()
        self.vlay = QVBoxLayout()

        # Form 레이아웃 생성
        self.form = QFormLayout(self)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.btn1 = QPushButton("나이 확인")
        self.btn2 = QPushButton("회원가입")
        self.lbl = QLabel("경고: 나이가 너무 많습니다.", self)
        self.lbl.setVisible(False)

        hlay = QHBoxLayout()

        hlay.addWidget(self.edit2)
        hlay.addWidget(self.btn1)

        # btn 클릭시
        self.btn1.clicked.connect(self.clickBtn1)
        self.btn2.clicked.connect(self.clickBtn2)


        self.form.addRow("name", self.edit1)
        self.form.addRow("age", hlay)
        self.form.addRow("", self.lbl)
        self.form.addRow("", self.btn2)
        self.vlay.addLayout(self.form)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
