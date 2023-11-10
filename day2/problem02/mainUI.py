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
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QLCDNumber,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(405, 494)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 371, 431))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout.addWidget(self.lcdNumber, 2, 0, 1, 2)

        self.onBtn = QPushButton(self.gridLayoutWidget)
        self.onBtn.setObjectName(u"onBtn")

        self.gridLayout.addWidget(self.onBtn, 1, 0, 1, 1)

        self.offBtn = QPushButton(self.gridLayoutWidget)
        self.offBtn.setObjectName(u"offBtn")

        self.gridLayout.addWidget(self.offBtn, 1, 1, 1, 1)

        self.dial = QDial(self.gridLayoutWidget)
        self.dial.setObjectName(u"dial")

        self.gridLayout.addWidget(self.dial, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 405, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.onBtn.clicked.connect(MainWindow.ledON)
        self.offBtn.clicked.connect(MainWindow.ledOFF)
        self.dial.valueChanged.connect(MainWindow.setDial)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.onBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.offBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

