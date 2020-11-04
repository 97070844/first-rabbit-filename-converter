# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setMinimumSize(QtCore.QSize(500, 450))
        MainWindow.setMaximumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bitmap_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 20, 239, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addFileButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addFileButton.setObjectName("Button")
        self.horizontalLayout.addWidget(self.addFileButton)
        self.addFolderButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addFolderButton.setObjectName("Button")
        self.horizontalLayout.addWidget(self.addFolderButton)
        self.clearAllButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearAllButton.setObjectName("Button")
        self.horizontalLayout.addWidget(self.clearAllButton)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 461, 211))
        self.listWidget.setIconSize(QtCore.QSize(15, 15))
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 300, 471, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(370, 360, 111, 31))
        self.convertButton.setObjectName("Button")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 10, 91, 51))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("icons/bitmap.png"))
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("QStatusBar{background-color: #363636;color: #FFF;}")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/addfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon1)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/deletefile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon2)
        self.actionRemove.setObjectName("actionRemove")
        self.actionAddFolder = QtWidgets.QAction(MainWindow)
        self.actionAddFolder.setObjectName("actionAddFolder")
        # self.actionRemoveFolder = QtWidgets.QAction(MainWindow)
        # self.actionRemoveFolder.setObjectName("actionRemoveFolder")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/closewin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAboutUs = QtWidgets.QAction(MainWindow)
        self.actionAboutUs.setObjectName("actionAboutUs")
        self.menuTools.addAction(self.actionAdd)
        self.menuTools.addAction(self.actionRemove)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionAddFolder)
        #self.menuTools.addAction(self.actionRemoveFolder)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAboutUs)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "First Rabbit"))
        self.addFileButton.setText(_translate("MainWindow", "Add File"))
        self.addFolderButton.setText(_translate("MainWindow", "Add Folder"))
        self.clearAllButton.setText(_translate("MainWindow", "Clear All"))
        self.label.setText(_translate("MainWindow", "Format:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Zawgyi to Unicode"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Unicode to Zawgyi"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.menuTools.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd.setText(_translate("MainWindow", "Add File"))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionRemove.setText(_translate("MainWindow", "Remove File"))
        self.actionRemove.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionAddFolder.setText(_translate("MainWindow", "Add Folder"))
        self.actionAddFolder.setShortcut(_translate("MainWindow", "Ctrl+F"))
        # self.actionRemoveFolder.setText(_translate("MainWindow", "Remove Folder"))
        # self.actionRemoveFolder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAboutUs.setText(_translate("MainWindow", "About Us"))

# Create one instance as module-level usage.
ui = Ui_MainWindow()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())