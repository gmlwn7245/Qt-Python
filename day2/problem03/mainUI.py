# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 507)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 531, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nameBtn = QPushButton(self.gridLayoutWidget)
        self.nameBtn.setObjectName(u"nameBtn")

        self.gridLayout.addWidget(self.nameBtn, 1, 0, 1, 1)

        self.colorBtn = QPushButton(self.gridLayoutWidget)
        self.colorBtn.setObjectName(u"colorBtn")

        self.gridLayout.addWidget(self.colorBtn, 1, 1, 1, 1)

        self.startBtn = QPushButton(self.gridLayoutWidget)
        self.startBtn.setObjectName(u"startBtn")

        self.gridLayout.addWidget(self.startBtn, 1, 2, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(203, 255, 252)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl = QLabel(self.frame)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(100, 120, 21, 16))
        self.lbl.setStyleSheet(u"background-color:rgb(170, 255, 127)")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 543, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.nameBtn.clicked.connect(MainWindow.nameChange)
        self.colorBtn.clicked.connect(MainWindow.colorChange)
        self.startBtn.clicked.connect(MainWindow.start)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameBtn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.colorBtn.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd\uc0c9 \ubcc0\uacbd", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"KFC", None))
    # retranslateUi

