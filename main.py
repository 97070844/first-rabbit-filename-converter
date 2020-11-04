from mainUI import ui
from PyQt5.QtWidgets import (QApplication,QMainWindow,QMessageBox,
							QFileDialog,QListWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot,QSize
from  dialog import ProgressDialog
import sys,re,os,enum,time
import lib.Rabbit as rabbit
import lib.extfile as _extfile

style_sheet = """
    QWidget{
        background-color: #121212;
    }

    QLabel{
        color: #FFFFFF;
    }


    QComboBox{
        background-color: #363636;
        color: #FFFFFF;
        border: 0.1px solid white;
        height: 50px;
    }

    QComboBox QAbstractItemView{
        color:#FFFFFF;
        selection-background-color: #476d7c
    }

    
    QPushButton{
        background-color: #363636;
        color: #FFFFFF;
        border: 0.1px solid white;
        padding: 5px;
    }

    QPushButton:pressed{
        background-color: #476d7c;
        color: #DFD8D7;
    }

    QPushButton:hover{
        background-color: #476d7c;
        border: 0.3px solid #476d7c;
    }

    QListWidget::item{
        background-color: #363636;
        color: #FFF;
    }
    
    QListWidget::item:hover{
        background-color: #476d7c;
    }

"""


class TYPE(enum.Enum):
	FILE = 0
	FOLDER = 1
	SUBDIR = 2

class ConvertMode(enum.IntEnum):
	ZAW2UNI = 0
	UNI2ZAW = 1

class Worker(QThread):
	"""
	This class performs to convert fonts, using PyQt5 QThread mechanism.
	"""
	updateValueSignal = pyqtSignal(int)
	updateTextEditSignal = pyqtSignal(str, str)

	def __init__(self, files,cmode):
		super().__init__()
		self.files = files
		self.cmode = cmode

	def stopRunning(self):
		"""
		Terminate the thread.
		"""
		self.terminate()
		self.wait()

	def run(self):
		"""
		Convert zawgyi text to unicode and vici visa

		This method is immediately triggered when the QThread is started.
		"""
		for (i,filename) in enumerate(self.files):
			if self.cmode == ConvertMode.ZAW2UNI:
				uni_filename = rabbit.zg2uni(filename)
				os.rename(filename,uni_filename)
				self.updateValueSignal.emit(i+1)
				self.updateTextEditSignal.emit(filename,uni_filename)
				time.sleep(4.0)

			if self.cmode == ConvertMode.UNI2ZAW:
				zg_filename = rabbit.uni2zg(filename)
				os.rename(filename,zg_filename)
				self.updateValueSignal.emit(i+1)
				self.updateTextEditSignal.emit(filename,zg_filename)
				time.sleep(4.0)

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.files = list()
		self.initializeUI()

	def initializeUI(self):
		ui.setupUi(self)
		#ui.centralwidget.setStyleSheet(style_sheet)
		self.addSignals()

	def addSignals(self):
		ui.addFileButton.clicked.connect(self.addFileItem)
		ui.addFolderButton.clicked.connect(self.addFolderItem)
		ui.clearAllButton.clicked.connect(self.clearItems)
		ui.convertButton.clicked.connect(self.convert)

		ui.actionAdd.triggered.connect(self.addFileItem)
		ui.actionRemove.triggered.connect(self.removeItem)
		ui.actionAddFolder.triggered.connect(self.addFolderItem)
		ui.actionQuit.triggered.connect(self.exitDialog)
		ui.actionAboutUs.triggered.connect(self.aboutDialog)

	def addFileItem(self):
		filepath = self.openFileDialog() #return a list containing selected file(s)
		if filepath:
			self.files.extend(filepath)
			
			for file in filepath:
				self.addItem(file,TYPE.FILE)

	def addFolderItem(self):
		folderpath = self.openFolderDialog()
		if folderpath:
			self.files.append(folderpath)
			self.addItem(folderpath,TYPE.FOLDER)

			for _, _, files in os.walk(folderpath):
				for file in files:
					self.files.append(folderpath + "/" + file)

					self.addItem(file,TYPE.SUBDIR)

	def addItem(self,filepath,type):
		FILE_ICON = {"image":"icons/imgfile.png",
					"video":"icons/videofile.png",
					"programming":"icons/codefile.png",
					"audio":"icons/audiofile.png",
					"word-related":"icons/docfile.png",
					"spreadsheet":"icons/xlsfile.png",
					"presentation":"icons/ppfile.png",
					"internet-related":"icons/binaryfile.png"}

		if type == TYPE.FILE:
			filetype = _extfile.get_filetype(filepath) #_extfile is imported from site package (lib)
			if filetype:
				imagepath = FILE_ICON[filetype]
			else:
				imagepath = "icons/generalfile.png"

		if type == TYPE.FOLDER:
			imagepath = "icons/folder.png"

		if type == TYPE.SUBDIR:
			imagepath = "icons/more.png"

		listitem = QListWidgetItem()
		listitem.setText(filepath)
		listitem.setIcon(QIcon(imagepath))
		ui.listWidget.addItem(listitem)

	def clearItems(self):
		ui.listWidget.clear()
		self.files.clear()

	def removeItem(self):
		row = ui.listWidget.currentRow()
		ui.listWidget.takeItem(row)
		self.files.pop(row)

	def openFileDialog(self):
		filepath, _ = QFileDialog.getOpenFileNames(self,"Add File","","All Files (*);;Text Files (*.txt)", options=QFileDialog.Options())
		return filepath

	def openFolderDialog(self):
		folderpath = QFileDialog.getExistingDirectory(self,'Add Directory',"")
		return folderpath

	def convert(self):
		if self.files or self.folders:
			cmode = ui.comboBox.currentIndex()
			filecount = len(self.files)
			self.dialog = ProgressDialog()
			self.dialog.progressBar.setRange(0,filecount)
			self.dialog.show()

			#create Worker instance which is inherited from QThread.
			#convertion proccess is moved to QThread in order to perform faster and to flexible.
			#worker obj performs implicitly converting text.
			self.worker = Worker(self.files,cmode)
			self.worker.updateValueSignal.connect(self.updateProgressBar)
			self.worker.updateTextEditSignal.connect(self.updateTextEdit)
			self.worker.finished.connect(self.convertDone)
			self.worker.start()

	def updateProgressBar(self, value):
		self.dialog.progressBar.setValue(value)

	def updateTextEdit(self, old_text, new_text):
		self.dialog.textEdit.append("[INFO] {} changed to {}.\n".format(old_text, new_text))

	def convertDone(self):
		self.dialog.hide()
		QMessageBox.information(self,"Finished","Filename Convertion Finished!")
		self.clearItems()

	def aboutDialog(self):
		QMessageBox.about(self, "About First Rabbit", "This software is developed for free usage. Owned by Thura Soe")

	def exitDialog(self):
		choose = QMessageBox.question(self, "Exit", "Do you really want to quit?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		if choose == QMessageBox.Yes:
			self.close()

if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainwin = Main()
	mainwin.show()
	sys.exit(app.exec_())