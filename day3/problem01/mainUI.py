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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 317)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 60, 291, 111))
        self.progressBar.setValue(24)
        self.goBtn = QPushButton(self.centralwidget)
        self.goBtn.setObjectName(u"goBtn")
        self.goBtn.setGeometry(QRect(60, 180, 81, 51))
        self.pauseBtn = QPushButton(self.centralwidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setGeometry(QRect(160, 180, 81, 51))
        self.resetBtn = QPushButton(self.centralwidget)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setGeometry(QRect(260, 180, 81, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 415, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.goBtn.clicked.connect(MainWindow.download)
        self.pauseBtn.clicked.connect(MainWindow.stop)
        self.resetBtn.clicked.connect(MainWindow.reset)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.goBtn.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

