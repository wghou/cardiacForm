# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(620, 370, 151, 151))
        self.widget.setObjectName("widget")
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_exit = QtWidgets.QPushButton(self.widget)
        self.pushButton_exit.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_suspend = QtWidgets.QPushButton(self.widget)
        self.pushButton_suspend.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.pushButton_suspend.setObjectName("pushButton_suspend")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(630, 30, 151, 121))
        self.widget_2.setObjectName("widget_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(60, 320, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(130, 320, 16, 160))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_exit.setText(_translate("MainWindow", "停止"))
        self.pushButton_suspend.setText(_translate("MainWindow", "暂停"))
