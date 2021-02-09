# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCheckBox
import glob
import re
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.resize(426, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelOpen = QtWidgets.QLabel(self.centralwidget)
        self.labelOpen.setGeometry(QtCore.QRect(10, 0, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.labelOpen.setFont(font)
        self.labelOpen.setObjectName("labelOpen")
        self.actionClassify = QtWidgets.QPushButton(self.centralwidget)
        self.actionClassify.setGeometry(QtCore.QRect(10, 420, 401, 28))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.actionClassify.setFont(font)
        self.actionClassify.setObjectName("actionClassify")
        
         
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 80, 251, 20))
        self.checkBox.setObjectName("checkBox")
        
        # self.checkBox.stateChanged.connect(self.clickBox)
        
        
        self.actionBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.actionBrowser.setGeometry(QtCore.QRect(10, 210, 401, 201))
        self.actionBrowser.setObjectName("actionBrowser")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 361, 31))    
        
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        
        
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 401, 41))
        
        
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 160, 401, 41))
        
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(380, 40, 31, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self._open_file_dialog)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # self.text = self.lineEdit.toPlainText()
        self.actionClassify.clicked.connect(self.renameClick)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelOpen.setText(_translate("MainWindow", "Select directory to rename files"))
        self.actionClassify.setText(_translate("MainWindow", "Replace"))
        self.lineEdit_2.setText(_translate("MainWindow", "Pattern to remove"))
        self.lineEdit_3.setText(_translate("MainWindow", "Replace pattern or blank"))
        self.checkBox.setText(_translate("MainWindow", "Search subfolders to replace names"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        
    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            return True
        else:
            return False
        
    def _open_file_dialog(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText('{}'.format(directory))
        self.refresh_text_box("Editing files in: " + directory)
        
    def refresh_text_box(self, MYSTRING): 
        
        '''This is used to pass strings to the actionBrowser. I'm sure there are better
        ways to do this. '''
        self.actionBrowser.append(MYSTRING) #append string
        QtWidgets.QApplication.processEvents() #update gui for pyqt
        
    def renameClick(self):
        text_pattern = self.lineEdit_2.text() #Get text to change)
        text_replace = self.lineEdit_3.text() #Get text to change)
        self.refresh_text_box("")
        self.refresh_text_box("You're removing %s from these files." %(text_pattern))
        
        x = self.checkBox.isChecked() #check if check box is checked
       
        if x == True: 
            files = glob.glob("test_files/*")
            regex = re.compile(text_pattern) #Compile the string into a regex search
    
            result = [f for f in files if re.search(regex, f)] #Find all the files that match result
            
            files = glob.glob("test_files/**/*")
            regex = re.compile(text_pattern) #Compile the string into a regex search
    
            result2 = [f for f in files if re.search(regex, f)] #Find all the files that match result
            
            result = result + result2
            
            self.refresh_text_box("")
            file_lst_trimmed = [re.sub(regex, text_replace, file) for file in result]
            
        else:
            files = glob.glob("test_files/*")
            regex = re.compile(text_pattern) #Compile the string into a regex search
    
            result = [f for f in files if re.search(regex, f)]  #Find all the files that match result
            
            self.refresh_text_box("")
            file_lst_trimmed = [re.sub(regex, text_replace, file) for file in result]
        
        #Print out files
        for i in range(0,len(result)): 
            self.refresh_text_box(result[i])
            os.rename(result[i], file_lst_trimmed[i])
            
        
        
        self.refresh_text_box("New files names:")
        #Print out files
        for i in file_lst_trimmed: 
            self.refresh_text_box("")
            self.refresh_text_box(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

