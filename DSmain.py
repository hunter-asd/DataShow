# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DSmain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataShow(object):
    def setupUi(self, DataShow):
        DataShow.setObjectName("DataShow")
        DataShow.resize(926, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("screen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataShow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DataShow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(30, 30, 30, -1)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.DS1Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS1Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS1Node.setFont(font)
        self.DS1Node.setText("")
        self.DS1Node.setObjectName("DS1Node")
        self.gridLayout_2.addWidget(self.DS1Node, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.DS6Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS6Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS6Node.setFont(font)
        self.DS6Node.setText("")
        self.DS6Node.setObjectName("DS6Node")
        self.gridLayout_2.addWidget(self.DS6Node, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.DS2Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS2Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS2Node.setFont(font)
        self.DS2Node.setText("")
        self.DS2Node.setObjectName("DS2Node")
        self.gridLayout_2.addWidget(self.DS2Node, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.DS7Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS7Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS7Node.setFont(font)
        self.DS7Node.setText("")
        self.DS7Node.setObjectName("DS7Node")
        self.gridLayout_2.addWidget(self.DS7Node, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.DS3Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS3Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS3Node.setFont(font)
        self.DS3Node.setText("")
        self.DS3Node.setObjectName("DS3Node")
        self.gridLayout_2.addWidget(self.DS3Node, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.DS8Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS8Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS8Node.setFont(font)
        self.DS8Node.setText("")
        self.DS8Node.setObjectName("DS8Node")
        self.gridLayout_2.addWidget(self.DS8Node, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.DS4Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS4Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS4Node.setFont(font)
        self.DS4Node.setText("")
        self.DS4Node.setObjectName("DS4Node")
        self.gridLayout_2.addWidget(self.DS4Node, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 1)
        self.DS9Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS9Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS9Node.setFont(font)
        self.DS9Node.setText("")
        self.DS9Node.setObjectName("DS9Node")
        self.gridLayout_2.addWidget(self.DS9Node, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.DS5Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS5Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS5Node.setFont(font)
        self.DS5Node.setText("")
        self.DS5Node.setObjectName("DS5Node")
        self.gridLayout_2.addWidget(self.DS5Node, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 2, 1, 1)
        self.DS10Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS10Node.setMinimumSize(QtCore.QSize(270, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS10Node.setFont(font)
        self.DS10Node.setText("")
        self.DS10Node.setObjectName("DS10Node")
        self.gridLayout_2.addWidget(self.DS10Node, 4, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(-1, -1, 3, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RunButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RunButton.sizePolicy().hasHeightForWidth())
        self.RunButton.setSizePolicy(sizePolicy)
        self.RunButton.setMinimumSize(QtCore.QSize(100, 35))
        self.RunButton.setMaximumSize(QtCore.QSize(100, 35))
        self.RunButton.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));")
        self.RunButton.setObjectName("RunButton")
        self.horizontalLayout_2.addWidget(self.RunButton)
        self.UDPButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UDPButton.sizePolicy().hasHeightForWidth())
        self.UDPButton.setSizePolicy(sizePolicy)
        self.UDPButton.setMinimumSize(QtCore.QSize(100, 35))
        self.UDPButton.setMaximumSize(QtCore.QSize(100, 35))
        self.UDPButton.setObjectName("UDPButton")
        self.horizontalLayout_2.addWidget(self.UDPButton)
        self.CloseButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(100, 35))
        self.CloseButton.setMaximumSize(QtCore.QSize(100, 35))
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.CloseButton)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LocalMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.LocalMode.setMaximumSize(QtCore.QSize(100, 35))
        self.LocalMode.setChecked(True)
        self.LocalMode.setObjectName("LocalMode")
        self.gridLayout_3.addWidget(self.LocalMode, 0, 1, 1, 1)
        self.RemoteMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.RemoteMode.setMaximumSize(QtCore.QSize(100, 35))
        self.RemoteMode.setObjectName("RemoteMode")
        self.gridLayout_3.addWidget(self.RemoteMode, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.DS5Button = QtWidgets.QPushButton(self.groupBox)
        self.DS5Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS5Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS5Button.setObjectName("DS5Button")
        self.gridLayout.addWidget(self.DS5Button, 0, 4, 1, 1)
        self.DS3Button = QtWidgets.QPushButton(self.groupBox)
        self.DS3Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS3Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS3Button.setObjectName("DS3Button")
        self.gridLayout.addWidget(self.DS3Button, 0, 2, 1, 1)
        self.DS7Button = QtWidgets.QPushButton(self.groupBox)
        self.DS7Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS7Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS7Button.setObjectName("DS7Button")
        self.gridLayout.addWidget(self.DS7Button, 1, 1, 1, 1)
        self.DS1Button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DS1Button.sizePolicy().hasHeightForWidth())
        self.DS1Button.setSizePolicy(sizePolicy)
        self.DS1Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS1Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS1Button.setObjectName("DS1Button")
        self.gridLayout.addWidget(self.DS1Button, 0, 0, 1, 1)
        self.DS2Button = QtWidgets.QPushButton(self.groupBox)
        self.DS2Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS2Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS2Button.setObjectName("DS2Button")
        self.gridLayout.addWidget(self.DS2Button, 0, 1, 1, 1)
        self.DS9Button = QtWidgets.QPushButton(self.groupBox)
        self.DS9Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS9Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS9Button.setObjectName("DS9Button")
        self.gridLayout.addWidget(self.DS9Button, 1, 3, 1, 1)
        self.DS6Button = QtWidgets.QPushButton(self.groupBox)
        self.DS6Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS6Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS6Button.setObjectName("DS6Button")
        self.gridLayout.addWidget(self.DS6Button, 1, 0, 1, 1)
        self.DS4Button = QtWidgets.QPushButton(self.groupBox)
        self.DS4Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS4Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS4Button.setObjectName("DS4Button")
        self.gridLayout.addWidget(self.DS4Button, 0, 3, 1, 1)
        self.DS10Button = QtWidgets.QPushButton(self.groupBox)
        self.DS10Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS10Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS10Button.setObjectName("DS10Button")
        self.gridLayout.addWidget(self.DS10Button, 1, 4, 1, 1)
        self.DS8Button = QtWidgets.QPushButton(self.groupBox)
        self.DS8Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS8Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS8Button.setObjectName("DS8Button")
        self.gridLayout.addWidget(self.DS8Button, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 1)
        DataShow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataShow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 23))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuSetting_2 = QtWidgets.QMenu(self.menubar)
        self.menuSetting_2.setObjectName("menuSetting_2")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        DataShow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataShow)
        self.statusbar.setObjectName("statusbar")
        DataShow.setStatusBar(self.statusbar)
        self.actionIP = QtWidgets.QAction(DataShow)
        self.actionIP.setObjectName("actionIP")
        self.actionPORT = QtWidgets.QAction(DataShow)
        self.actionPORT.setObjectName("actionPORT")
        self.actionopen_Cfg = QtWidgets.QAction(DataShow)
        self.actionopen_Cfg.setObjectName("actionopen_Cfg")
        self.actionSave_Cfg = QtWidgets.QAction(DataShow)
        self.actionSave_Cfg.setObjectName("actionSave_Cfg")
        self.actionParam = QtWidgets.QAction(DataShow)
        self.actionParam.setObjectName("actionParam")
        self.actionScreen = QtWidgets.QAction(DataShow)
        self.actionScreen.setObjectName("actionScreen")
        self.actionNetwork = QtWidgets.QAction(DataShow)
        self.actionNetwork.setObjectName("actionNetwork")
        self.actionAxis = QtWidgets.QAction(DataShow)
        self.actionAxis.setObjectName("actionAxis")
        self.actionTitle = QtWidgets.QAction(DataShow)
        self.actionTitle.setObjectName("actionTitle")
        self.actionLineWidth = QtWidgets.QAction(DataShow)
        self.actionLineWidth.setObjectName("actionLineWidth")
        self.actionabout = QtWidgets.QAction(DataShow)
        self.actionabout.setObjectName("actionabout")
        self.menuSetting.addAction(self.actionopen_Cfg)
        self.menuSetting.addAction(self.actionSave_Cfg)
        self.menuSetting_2.addAction(self.actionParam)
        self.menuAbout.addAction(self.actionabout)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuSetting_2.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(DataShow)
        QtCore.QMetaObject.connectSlotsByName(DataShow)

    def retranslateUi(self, DataShow):
        _translate = QtCore.QCoreApplication.translate
        DataShow.setWindowTitle(_translate("DataShow", "DataShow"))
        self.label.setText(_translate("DataShow", "DS1:"))
        self.label_7.setText(_translate("DataShow", "DS6:"))
        self.label_2.setText(_translate("DataShow", "DS2:"))
        self.label_8.setText(_translate("DataShow", "DS7:"))
        self.label_3.setText(_translate("DataShow", "DS3:"))
        self.label_9.setText(_translate("DataShow", "DS8:"))
        self.label_4.setText(_translate("DataShow", "DS4:"))
        self.label_10.setText(_translate("DataShow", "DS9:"))
        self.label_5.setText(_translate("DataShow", "DS5:"))
        self.label_11.setText(_translate("DataShow", "DS10:"))
        self.RunButton.setText(_translate("DataShow", "RUN"))
        self.UDPButton.setText(_translate("DataShow", "UDP"))
        self.CloseButton.setText(_translate("DataShow", "Close"))
        self.LocalMode.setText(_translate("DataShow", "Local"))
        self.RemoteMode.setText(_translate("DataShow", "Remote"))
        self.DS5Button.setText(_translate("DataShow", "DS5"))
        self.DS3Button.setText(_translate("DataShow", "DS3"))
        self.DS7Button.setText(_translate("DataShow", "DS7"))
        self.DS1Button.setText(_translate("DataShow", "DS1"))
        self.DS2Button.setText(_translate("DataShow", "DS2"))
        self.DS9Button.setText(_translate("DataShow", "DS9"))
        self.DS6Button.setText(_translate("DataShow", "DS6"))
        self.DS4Button.setText(_translate("DataShow", "DS4"))
        self.DS10Button.setText(_translate("DataShow", "DS10"))
        self.DS8Button.setText(_translate("DataShow", "DS8"))
        self.menuSetting.setTitle(_translate("DataShow", "File"))
        self.menuSetting_2.setTitle(_translate("DataShow", "Setting"))
        self.menuAbout.setTitle(_translate("DataShow", "About"))
        self.actionIP.setText(_translate("DataShow", "IP"))
        self.actionPORT.setText(_translate("DataShow", "PORT"))
        self.actionopen_Cfg.setText(_translate("DataShow", "Open Cfg"))
        self.actionSave_Cfg.setText(_translate("DataShow", "Save Cfg"))
        self.actionParam.setText(_translate("DataShow", "Param"))
        self.actionScreen.setText(_translate("DataShow", "Screen"))
        self.actionNetwork.setText(_translate("DataShow", "Udp"))
        self.actionAxis.setText(_translate("DataShow", "Axis"))
        self.actionTitle.setText(_translate("DataShow", "Title"))
        self.actionLineWidth.setText(_translate("DataShow", "LineWidth"))
        self.actionabout.setText(_translate("DataShow", "About"))

