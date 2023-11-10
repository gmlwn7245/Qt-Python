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
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(410, 120, 75, 24))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 311, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pb1 = QProgressBar(self.verticalLayoutWidget)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setValue(24)

        self.verticalLayout.addWidget(self.pb1)

        self.pb2 = QProgressBar(self.verticalLayoutWidget)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setValue(24)

        self.verticalLayout.addWidget(self.pb2)

        self.pb4 = QProgressBar(self.verticalLayoutWidget)
        self.pb4.setObjectName(u"pb4")
        self.pb4.setValue(24)

        self.verticalLayout.addWidget(self.pb4)

        self.pb3 = QProgressBar(self.verticalLayoutWidget)
        self.pb3.setObjectName(u"pb3")
        self.pb3.setValue(24)

        self.verticalLayout.addWidget(self.pb3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn.clicked.connect(MainWindow.go)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

