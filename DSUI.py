# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DSUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataShow(object):
    def setupUi(self, DataShow):
        DataShow.setObjectName("DataShow")
        DataShow.resize(973, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/liuyongag/.designer/backup/screen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.DS1Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS1Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS1Node.setFont(font)
        self.DS1Node.setText("")
        self.DS1Node.setObjectName("DS1Node")
        self.gridLayout_2.addWidget(self.DS1Node, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 4, 1, 1)
        self.DS4Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS4Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS4Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS4Button.setObjectName("DS4Button")
        self.gridLayout_2.addWidget(self.DS4Button, 3, 2, 1, 1)
        self.DS4Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS4Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS4Node.setFont(font)
        self.DS4Node.setText("")
        self.DS4Node.setObjectName("DS4Node")
        self.gridLayout_2.addWidget(self.DS4Node, 3, 1, 1, 1)
        self.DS9Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS9Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS9Node.setFont(font)
        self.DS9Node.setText("")
        self.DS9Node.setObjectName("DS9Node")
        self.gridLayout_2.addWidget(self.DS9Node, 3, 5, 1, 1)
        self.DS5Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS5Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS5Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS5Button.setObjectName("DS5Button")
        self.gridLayout_2.addWidget(self.DS5Button, 4, 2, 1, 1)
        self.DS10Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS10Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS10Node.setFont(font)
        self.DS10Node.setText("")
        self.DS10Node.setObjectName("DS10Node")
        self.gridLayout_2.addWidget(self.DS10Node, 4, 5, 1, 1)
        self.DS10Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS10Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS10Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS10Button.setObjectName("DS10Button")
        self.gridLayout_2.addWidget(self.DS10Button, 4, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 4, 1, 1)
        self.DS5Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS5Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS5Node.setFont(font)
        self.DS5Node.setText("")
        self.DS5Node.setObjectName("DS5Node")
        self.gridLayout_2.addWidget(self.DS5Node, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 4, 1, 1)
        self.DS6Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS6Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS6Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS6Button.setObjectName("DS6Button")
        self.gridLayout_2.addWidget(self.DS6Button, 0, 6, 1, 1)
        self.DS6Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS6Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS6Node.setFont(font)
        self.DS6Node.setText("")
        self.DS6Node.setObjectName("DS6Node")
        self.gridLayout_2.addWidget(self.DS6Node, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.DS1Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DS1Button.sizePolicy().hasHeightForWidth())
        self.DS1Button.setSizePolicy(sizePolicy)
        self.DS1Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS1Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS1Button.setObjectName("DS1Button")
        self.gridLayout_2.addWidget(self.DS1Button, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 4, 1, 1)
        self.DS2Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS2Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS2Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS2Button.setObjectName("DS2Button")
        self.gridLayout_2.addWidget(self.DS2Button, 1, 2, 1, 1)
        self.DS3Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS3Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS3Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS3Button.setObjectName("DS3Button")
        self.gridLayout_2.addWidget(self.DS3Button, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 4, 1, 1)
        self.DS7Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS7Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS7Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS7Button.setObjectName("DS7Button")
        self.gridLayout_2.addWidget(self.DS7Button, 1, 6, 1, 1)
        self.DS2Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS2Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS2Node.setFont(font)
        self.DS2Node.setText("")
        self.DS2Node.setObjectName("DS2Node")
        self.gridLayout_2.addWidget(self.DS2Node, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.DS3Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS3Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS3Node.setFont(font)
        self.DS3Node.setText("")
        self.DS3Node.setObjectName("DS3Node")
        self.gridLayout_2.addWidget(self.DS3Node, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.DS7Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS7Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS7Node.setFont(font)
        self.DS7Node.setText("")
        self.DS7Node.setObjectName("DS7Node")
        self.gridLayout_2.addWidget(self.DS7Node, 1, 5, 1, 1)
        self.DS8Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS8Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS8Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS8Button.setObjectName("DS8Button")
        self.gridLayout_2.addWidget(self.DS8Button, 2, 6, 1, 1)
        self.DS9Button = QtWidgets.QPushButton(self.centralwidget)
        self.DS9Button.setMinimumSize(QtCore.QSize(100, 35))
        self.DS9Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DS9Button.setObjectName("DS9Button")
        self.gridLayout_2.addWidget(self.DS9Button, 3, 6, 1, 1)
        self.DS8Node = QtWidgets.QLineEdit(self.centralwidget)
        self.DS8Node.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DS8Node.setFont(font)
        self.DS8Node.setText("")
        self.DS8Node.setObjectName("DS8Node")
        self.gridLayout_2.addWidget(self.DS8Node, 2, 5, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 0, 3, 5, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 1, 2, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Message = QtWidgets.QTextBrowser(self.groupBox_2)
        self.Message.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.Message.setObjectName("Message")
        self.horizontalLayout.addWidget(self.Message)
        self.line_5 = QtWidgets.QFrame(self.groupBox_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Voice = QtWidgets.QLabel(self.groupBox_2)
        self.Voice.setObjectName("Voice")
        self.gridLayout.addWidget(self.Voice, 0, 0, 1, 1)
        self.UDPButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UDPButton.sizePolicy().hasHeightForWidth())
        self.UDPButton.setSizePolicy(sizePolicy)
        self.UDPButton.setMinimumSize(QtCore.QSize(100, 35))
        self.UDPButton.setMaximumSize(QtCore.QSize(100, 35))
        self.UDPButton.setObjectName("UDPButton")
        self.gridLayout.addWidget(self.UDPButton, 3, 3, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(100, 35))
        self.CloseButton.setMaximumSize(QtCore.QSize(100, 35))
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout.addWidget(self.CloseButton, 3, 4, 1, 1)
        self.Source = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Source.sizePolicy().hasHeightForWidth())
        self.Source.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Source.setFont(font)
        self.Source.setObjectName("Source")
        self.gridLayout.addWidget(self.Source, 1, 0, 1, 1)
        self.Volume = QtWidgets.QSlider(self.groupBox_2)
        self.Volume.setOrientation(QtCore.Qt.Horizontal)
        self.Volume.setObjectName("Volume")
        self.gridLayout.addWidget(self.Volume, 0, 5, 1, 1)
        self.RemoteMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.RemoteMode.setMaximumSize(QtCore.QSize(100, 35))
        self.RemoteMode.setObjectName("RemoteMode")
        self.gridLayout.addWidget(self.RemoteMode, 1, 4, 1, 1)
        self.Speaker = QtWidgets.QCheckBox(self.groupBox_2)
        self.Speaker.setObjectName("Speaker")
        self.gridLayout.addWidget(self.Speaker, 0, 4, 1, 1)
        self.SpeakNode = QtWidgets.QLineEdit(self.groupBox_2)
        self.SpeakNode.setMaximumSize(QtCore.QSize(75, 16777215))
        self.SpeakNode.setObjectName("SpeakNode")
        self.gridLayout.addWidget(self.SpeakNode, 0, 3, 1, 1)
        self.Operate = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Operate.sizePolicy().hasHeightForWidth())
        self.Operate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Operate.setFont(font)
        self.Operate.setObjectName("Operate")
        self.gridLayout.addWidget(self.Operate, 3, 0, 1, 1)
        self.LocalMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.LocalMode.setMaximumSize(QtCore.QSize(150, 50))
        self.LocalMode.setIconSize(QtCore.QSize(16, 16))
        self.LocalMode.setChecked(False)
        self.LocalMode.setObjectName("LocalMode")
        self.gridLayout.addWidget(self.LocalMode, 1, 3, 1, 1)
        self.QueryButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QueryButton.sizePolicy().hasHeightForWidth())
        self.QueryButton.setSizePolicy(sizePolicy)
        self.QueryButton.setMinimumSize(QtCore.QSize(100, 35))
        self.QueryButton.setMaximumSize(QtCore.QSize(100, 35))
        self.QueryButton.setObjectName("QueryButton")
        self.gridLayout.addWidget(self.QueryButton, 2, 4, 1, 1)
        self.ShotNum = QtWidgets.QSpinBox(self.groupBox_2)
        self.ShotNum.setMinimumSize(QtCore.QSize(0, 0))
        self.ShotNum.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ShotNum.setFont(font)
        self.ShotNum.setMinimum(1)
        self.ShotNum.setMaximum(50000)
        self.ShotNum.setObjectName("ShotNum")
        self.gridLayout.addWidget(self.ShotNum, 2, 3, 1, 1)
        self.QueryLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QueryLabel.sizePolicy().hasHeightForWidth())
        self.QueryLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.QueryLabel.setFont(font)
        self.QueryLabel.setObjectName("QueryLabel")
        self.gridLayout.addWidget(self.QueryLabel, 2, 0, 1, 1)
        self.FakeMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.FakeMode.setMaximumSize(QtCore.QSize(100, 35))
        self.FakeMode.setObjectName("FakeMode")
        self.gridLayout.addWidget(self.FakeMode, 1, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_4.addWidget(self.groupBox_2, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 4, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 1, 0, 3, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_4.addWidget(self.line_6, 2, 1, 1, 1)
        DataShow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataShow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSet = QtWidgets.QMenu(self.menubar)
        self.menuSet.setObjectName("menuSet")
        self.menuNetWork = QtWidgets.QMenu(self.menuSet)
        self.menuNetWork.setObjectName("menuNetWork")
        self.menuDataBase = QtWidgets.QMenu(self.menuSet)
        self.menuDataBase.setObjectName("menuDataBase")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        DataShow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataShow)
        self.statusbar.setObjectName("statusbar")
        DataShow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(DataShow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(DataShow)
        self.actionSave.setObjectName("actionSave")
        self.actionGraph = QtWidgets.QAction(DataShow)
        self.actionGraph.setObjectName("actionGraph")
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
        self.actionDataBase = QtWidgets.QAction(DataShow)
        self.actionDataBase.setObjectName("actionDataBase")
        self.actionExit = QtWidgets.QAction(DataShow)
        self.actionExit.setObjectName("actionExit")
        self.actionVersion = QtWidgets.QAction(DataShow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionAuthor = QtWidgets.QAction(DataShow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionPort = QtWidgets.QAction(DataShow)
        self.actionPort.setObjectName("actionPort")
        self.actionIP = QtWidgets.QAction(DataShow)
        self.actionIP.setAutoRepeat(False)
        self.actionIP.setObjectName("actionIP")
        self.actionTreeIP = QtWidgets.QAction(DataShow)
        self.actionTreeIP.setObjectName("actionTreeIP")
        self.actionTreeName = QtWidgets.QAction(DataShow)
        self.actionTreeName.setObjectName("actionTreeName")
        self.actionHelp = QtWidgets.QAction(DataShow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionGraph)
        self.menuNetWork.addAction(self.actionIP)
        self.menuNetWork.addAction(self.actionPort)
        self.menuDataBase.addAction(self.actionTreeIP)
        self.menuDataBase.addAction(self.actionTreeName)
        self.menuSet.addAction(self.menuNetWork.menuAction())
        self.menuSet.addAction(self.menuDataBase.menuAction())
        self.menuAbout.addAction(self.actionVersion)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSet.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(DataShow)
        QtCore.QMetaObject.connectSlotsByName(DataShow)

    def retranslateUi(self, DataShow):
        _translate = QtCore.QCoreApplication.translate
        DataShow.setWindowTitle(_translate("DataShow", "DataShow"))
        self.label_5.setText(_translate("DataShow", "DS5:"))
        self.label_7.setText(_translate("DataShow", "DS6:"))
        self.DS4Button.setText(_translate("DataShow", "DS4"))
        self.DS5Button.setText(_translate("DataShow", "DS5"))
        self.DS10Button.setText(_translate("DataShow", "DS10"))
        self.label_10.setText(_translate("DataShow", "DS9:"))
        self.label_2.setText(_translate("DataShow", "DS2:"))
        self.label_11.setText(_translate("DataShow", "DS10:"))
        self.DS6Button.setText(_translate("DataShow", "DS6"))
        self.label_4.setText(_translate("DataShow", "DS4:"))
        self.DS1Button.setText(_translate("DataShow", "DS1"))
        self.label_9.setText(_translate("DataShow", "DS8:"))
        self.DS2Button.setText(_translate("DataShow", "DS2"))
        self.DS3Button.setText(_translate("DataShow", "DS3"))
        self.label_8.setText(_translate("DataShow", "DS7:"))
        self.DS7Button.setText(_translate("DataShow", "DS7"))
        self.label.setText(_translate("DataShow", "DS1:"))
        self.label_3.setText(_translate("DataShow", "DS3:"))
        self.DS8Button.setText(_translate("DataShow", "DS8"))
        self.DS9Button.setText(_translate("DataShow", "DS9"))
        self.Voice.setText(_translate("DataShow", "Voice:"))
        self.UDPButton.setText(_translate("DataShow", "UDP"))
        self.CloseButton.setText(_translate("DataShow", "Close"))
        self.Source.setText(_translate("DataShow", "DataMode:"))
        self.RemoteMode.setText(_translate("DataShow", "Remote"))
        self.Speaker.setText(_translate("DataShow", "Speaker"))
        self.Operate.setText(_translate("DataShow", "Operate:"))
        self.LocalMode.setText(_translate("DataShow", "Local"))
        self.QueryButton.setText(_translate("DataShow", "Query"))
        self.QueryLabel.setText(_translate("DataShow", "DataQuery:"))
        self.FakeMode.setText(_translate("DataShow", "Fake"))
        self.menuFile.setTitle(_translate("DataShow", "File"))
        self.menuView.setTitle(_translate("DataShow", "View"))
        self.menuSet.setTitle(_translate("DataShow", "Set"))
        self.menuNetWork.setTitle(_translate("DataShow", "NetWork"))
        self.menuDataBase.setTitle(_translate("DataShow", "DataBase"))
        self.menuAbout.setTitle(_translate("DataShow", "About"))
        self.actionOpen.setText(_translate("DataShow", "Open"))
        self.actionSave.setText(_translate("DataShow", "Save"))
        self.actionGraph.setText(_translate("DataShow", "Graph"))
        self.actionScreen.setText(_translate("DataShow", "Screen"))
        self.actionNetwork.setText(_translate("DataShow", "Udp"))
        self.actionAxis.setText(_translate("DataShow", "Axis"))
        self.actionTitle.setText(_translate("DataShow", "Title"))
        self.actionLineWidth.setText(_translate("DataShow", "LineWidth"))
        self.actionDataBase.setText(_translate("DataShow", "DataBase"))
        self.actionExit.setText(_translate("DataShow", "Exit"))
        self.actionVersion.setText(_translate("DataShow", "Version"))
        self.actionAuthor.setText(_translate("DataShow", "Author"))
        self.actionPort.setText(_translate("DataShow", "Port"))
        self.actionIP.setText(_translate("DataShow", "IP"))
        self.actionTreeIP.setText(_translate("DataShow", "IP"))
        self.actionTreeName.setText(_translate("DataShow", "Name"))
        self.actionHelp.setText(_translate("DataShow", "Help"))
