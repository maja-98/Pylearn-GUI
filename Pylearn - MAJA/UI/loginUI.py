# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pylearn = QtWidgets.QLabel(self.centralwidget)        
        self.pylearn.setGeometry(QtCore.QRect(270, 170, 90, 20))
        
        self.pylearn.setObjectName("pylearn")

        #print(QtGui.QFontDatabase().families())
        
        self.username_lbl = QtWidgets.QLabel(self.centralwidget)
        self.username_lbl.setGeometry(QtCore.QRect(210, 240, 60, 13))
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(210, 270, 60, 13))
        self.password_lbl.setObjectName("password_lbl")
        

        
        self.username = QtWidgets.QLineEdit(self.centralwidget) 
        self.username.setGeometry(QtCore.QRect(280, 240, 113, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(280, 270, 113, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(270, 320, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(270, 350, 75, 23))
        self.signup_btn.setObjectName("signup_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 210, 40, 16))       
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.pylearn.setFont(QtGui.QFont('72 Condensed', 15,weight=QtGui.QFont.Bold))       
        self.username_lbl.setFont(QtGui.QFont('Calibri Light',10))
        self.password_lbl.setFont(QtGui.QFont('Calibri Light',10))
        self.login_btn.setStyleSheet("QPushButton {background-color: black; color: white;font-family='Times-Italic'}")
        self.signup_btn.setStyleSheet("QPushButton {background-color: black; color: white;font-family='Times-Italic'}")
        self.username.setStyleSheet("background-color:white;font-family='Times-Italic'")
        self.password.setStyleSheet("background-color:white")
        self.label.setFont(QtGui.QFont('Courier',9))
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pylearn.setText(_translate("MainWindow", "PYLEARN"))
        self.username_lbl.setText(_translate("MainWindow", "Username"))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "login"))
        self.signup_btn.setText(_translate("MainWindow", "signup"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))