# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class ProgressDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(300, 250)
        self.setMaximumSize(QtCore.QSize(300, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bitmap_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        flags = QtCore.Qt.WindowFlags()
        self.setWindowFlags(flags)

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(20, 210, 271, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 281, 151))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Progress Dialog"))
        self.label.setText(_translate("Dialog", "Converting..."))
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ProgressDialog()
    ui.show()
    sys.exit(app.exec_())
