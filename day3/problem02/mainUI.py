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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb = QProgressBar(self.centralwidget)
        self.pb.setObjectName(u"pb")
        self.pb.setGeometry(QRect(30, 50, 161, 171))
        self.pb.setLayoutDirection(Qt.LeftToRight)
        self.pb.setValue(50)
        self.pb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pb.setOrientation(Qt.Vertical)
        self.pb.setInvertedAppearance(True)
        self.pb.setTextDirection(QProgressBar.TopToBottom)
        self.slider = QSlider(self.centralwidget)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(220, 190, 131, 31))
        self.slider.setValue(50)
        self.slider.setOrientation(Qt.Horizontal)
        self.upBtn = QPushButton(self.centralwidget)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setGeometry(QRect(240, 50, 91, 51))
        self.downBtn = QPushButton(self.centralwidget)
        self.downBtn.setObjectName(u"downBtn")
        self.downBtn.setGeometry(QRect(240, 110, 91, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 170, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.upBtn.clicked.connect(MainWindow.upClicked)
        self.upBtn.pressed.connect(MainWindow.upPressed)
        #self.upBtn.released.connect(MainWindow.stop)
        self.downBtn.clicked.connect(MainWindow.downClicked)
        self.downBtn.pressed.connect(MainWindow.downPressed)
        #self.downBtn.released.connect(MainWindow.stop)
        self.slider.valueChanged.connect(MainWindow.slide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.upBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.downBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc18d\ub3c4 \uc81c\uc5b4", None))
    # retranslateUi

