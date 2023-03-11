# -*- coding: utf-8 -*-

class Ui_MainWindow(object):
    ##################################################
    ################ GUI
    ##################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 532)
        MainWindow.setFixedSize(661, 532)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget) # Field PDF file location
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 421, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda: self.press_browse_pdf()) # Button search PDF
        self.pushButton.setGeometry(QtCore.QRect(570, 70, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda: self.press_browse_destination()) # Button search destination
        self.pushButton_2.setGeometry(QtCore.QRect(570, 100, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget) # Field Destination folder
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 421, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget,
                                            stateChanged = lambda: self.press_checkbox_everypage()) # Checkbox single pages
        self.checkBox.setGeometry(QtCore.QRect(390, 170, 231, 17))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget,
                                              textChanged = lambda: self.parse_range_pages()) # Field page ranges
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 91, 16))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 140, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget,
                                              stateChanged = lambda: self.press_checkbox_email()) # Checkbox send by email
        self.checkBox_2.setGeometry(QtCore.QRect(40, 270, 231, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget) # Field email recipient
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 270, 391, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 270, 21, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 300, 81, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget) # Field email content
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(250, 300, 391, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda: self.press_execute()) # Button Execute
        self.pushButton_3.setGeometry(QtCore.QRect(70, 410, 521, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget) # Progress bar
        self.progressBar.setGeometry(QtCore.QRect(70, 470, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget) # Greyed field for output documents
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 200, 231, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 101, 16))
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 240, 561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget) # Label to display no. of pages
        self.label_8.setGeometry(QtCore.QRect(390, 200, 161, 16))
        self.label_8.setObjectName("label_8")
        
        self.error_box = QtWidgets.QMessageBox()    # Error box
        self.error_box.setWindowTitle("PDF Slicer - Error")
        self.error_box.setIcon(QtWidgets.QMessageBox.Critical)
        
        self.confirmation_box = QtWidgets.QMessageBox() # Confirmation box
        self.confirmation_box.setWindowTitle("PDF Slicer - PDF is sliced")
        self.confirmation_box.setIcon(QtWidgets.QMessageBox.Information)
        self.confirmation_box.setText("The PDF file has been sliced.")
        
        self.pushButton_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.checkBox.raise_()
        self.lineEdit_3.raise_()
        self.label_4.raise_()
        self.line.raise_()
        self.checkBox_2.raise_()
        self.lineEdit_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textEdit.raise_()
        self.pushButton_3.raise_()
        self.progressBar.raise_()
        self.lineEdit_5.raise_()
        self.label_7.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Icon
        # app_icon = QtGui.QIcon()
        # app_icon.addFile('icons/icons8-split-files-16.png', QtCore.QSize(16,16))
        # app_icon.addFile('icons/icons8-split-files-30.png', QtCore.QSize(30,30))
        # app_icon.addFile('icons/icons8-split-files-40.png', QtCore.QSize(40,40))
        # app_icon.addFile('icons/icons8-split-files-80.png', QtCore.QSize(80,80))
        # app.setWindowIcon(app_icon)
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF Slicer"))
        self.label.setText(_translate("MainWindow", "PDF Slicer"))
        self.label_2.setText(_translate("MainWindow", "PDF to slice:"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Destination folder:"))
        self.checkBox.setText(_translate("MainWindow", "Slice and save each page separately"))
        self.label_4.setText(_translate("MainWindow", "Page ranges:"))
        self.checkBox_2.setText(_translate("MainWindow", "Email sliced pages"))
        
        # Input email address
        for account in outlook.GetNamespace("MAPI").Accounts:
            # In case of multiple accounts set in Outlook, the last found email address from outlook account will be used as a default
            default_email = account.DeliveryStore.DisplayName
        self.lineEdit_4.setText(_translate("MainWindow", default_email.lower()))
        
        self.label_5.setText(_translate("MainWindow", "To:"))
        self.label_6.setText(_translate("MainWindow", "Email content:"))
        self.pushButton_3.setText(_translate("MainWindow", "Slice (and email)"))
        self.label_7.setText(_translate("MainWindow", "Output documents:"))
        self.label_8.setText(_translate("MainWindow", "(No file loaded)"))
    
    
    ##################################################
    ################ Actions
    ##################################################
    
    # Upon press buton "Browse PDF" 
    def press_browse_pdf(self):
        global filepath, folderpath
        file, check = QtWidgets.QFileDialog.getOpenFileName(None, "Select PDF to slice", 
                                                            "", "PDF Files (*.pdf)")
        if check: # Checks PDF
            filepath = file
            self.lineEdit.setText(filepath)
            self.progressBar.setProperty("value", 0)
            
            try:
                source_file = Pdf.open(filepath)
                nb_pages = len(source_file.pages)
                source_file.close()
            except Exception as e:
                filepath = ""
                self.lineEdit.setText(filepath)
                self.label_8.setText("(No file loaded)")
            else: # Update UI with infos
                self.label_8.setText(f"(Original PDF contains {nb_pages} pages)")
                if self.lineEdit_2.text() == "": # If extract path doesn't exists, we propose to extract to same folder
                    folderpath = os.path.split(os.path.abspath(filepath))[0].replace("\\", "/")
                    self.lineEdit_2.setText(folderpath)
    
    # Upon press buton "Browse Folder" 
    def press_browse_destination(self):
        global folderpath
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder')
        if folder != "": # Check
            folderpath = folder
            self.lineEdit_2.setText(folderpath)
    
    # Upon press checkbox "Slice each page separately"
    def press_checkbox_everypage(self):
        global every_page_separate
        every_page_separate = self.checkBox.isChecked()
        if every_page_separate:
            self.lineEdit_3.setText(display_every_page)
            self.lineEdit_3.setEnabled(False)
        else:
            self.lineEdit_3.setText("")
            self.lineEdit_3.setEnabled(True)
    
    # Upon press checkbox "email sliced PDF"
    def press_checkbox_email(self):
        global send_email
        send_email = self.checkBox_2.isChecked() # True or False
        self.lineEdit_4.setEnabled(send_email)
        self.textEdit.setEnabled(send_email)
    
    # Upon click on "Split  (and email)"
    def press_execute(self): 
        global send_email
        
        # Check page ranges
        page_ranges = self.parse_range_pages()
        if len(page_ranges) == 0 and not self.checkBox.isChecked():
            self.error_box.setText("Error: No valid range of pages selected.<br>The PDF file has not been sliced.")
            self.error_box.setInformativeText('Please input a valid range of pages, or select "Slice and save each page separately"')
            self.error_box.exec()
            return None
        
        # Check Destination folder
        if not os.path.isdir(folderpath):
            self.error_box.setText("Error: No valid destination folder.<br>The PDF file has not been sliced.")
            self.error_box.setInformativeText('Please select a valid destination folder.')
            self.error_box.exec()
            return None
        
        self.progressBar.setProperty("value", 0)
        
        # Everything is OK to proceed
        try:
            source_file = Pdf.open(filepath)
            nb_pages = len(source_file.pages)
            
            # Make up the page_ranges if every page separate
            if every_page_separate:
                page_ranges = [[i+1, i+1] for i in range(nb_pages)]
            no_of_docs = len(page_ranges)
            
            # Loop through different PDf to create
            for progress, page_range in enumerate(page_ranges, 1):
                k = 0
                tmp_pdf_name = folderpath + "/p" +  str(page_range[0])
                if page_range[1] != page_range[0]:
                    tmp_pdf_name += "-" + str(page_range[1])
                tmp_pdf_name += "_" + os.path.basename(filepath)
                
                # Create new PDF and fills with pages
                tmp_pdf = Pdf.new()
                right = max(page_range)
                left = min(page_range)
                for n, page in enumerate(source_file.pages):
                    k = n+1
                    if k in list(range(left, right+1)):
                        tmp_pdf.pages.append(page)
                tmp_pdf.save(tmp_pdf_name)
                tmp_pdf.close()
                
                self.progressBar.setProperty("value", round(100*(progress-0.5)/no_of_docs,0))

                #attach split PDF and send out
                if send_email:
                    mail = outlook.CreateItem(0)
                    mail.To = self.lineEdit_4.text()
                    mail.Subject = 'Sliced PDF'
                    mail.Body = self.textEdit.toPlainText()
                    mail.Attachments.Add(tmp_pdf_name)
                    mail.Send()
                    time.sleep(1)
                self.progressBar.setProperty("value", round(100*progress/no_of_docs,0))
            self.confirmation_box.exec()
            
        except Exception as e: # Catching potential errors
            self.error_box.setText("Error in opening the file.")
            self.error_box.setInformativeText(str(e))
            self.error_box.exec()
            return None
        
    # Upon input into range field AND when click on "Slice"
    def parse_range_pages(self):
        # User can enter multiple ranges. Acceptable range formats are: 
        # 1) continous range, for example pages 3 to 6: 3-6
        # 2) single page, for example page 10: 10
        # To combine multiple ranges, separate them by coma: 3-6, 10
        # Function returns an empty list if any error occured during parsing entered ranges
        
        input_range = self.lineEdit_3.text()
        
        if input_range == display_every_page:
            self.lineEdit_5.setText(display_every_page)
            return []
        else:
            range_str = ""
            
            for c in input_range:
                if c in allowed_chr:
                    range_str += c
            
            result = []
            temp_list_ranges = []
            
            try:
                for rng in range_str.split(","):
                    rng_sub = rng.split("-")
                    n = len(rng_sub)
                    if n == 1:
                        result.append([int(rng), int(rng)])
                        temp_list_ranges.append(rng)
                    elif n == 2:
                        result.append([int(rng_sub[0]), int(rng_sub[1])])
                        temp_list_ranges.append(rng_sub[0] + "-" + rng_sub[1])
            except: # one or more page ranges entered in wrong format
                pass
            
            if len(result) == 0:
                self.lineEdit_5.setText(default_display_range)
            else:
                self.lineEdit_5.setText(f"{len(result)} files: {', '.join(temp_list_ranges)}")
                
            return result

##################################################
################ Main run
##################################################

if __name__ == "__main__":
    import sys
    import os
    import time
    import win32com.client
    from PyQt5 import QtCore, QtGui, QtWidgets
    from pikepdf import Pdf
    
    filepath = None
    folderpath = None
    
    pageranges = "" #str
    every_page_separate = False
    allowed_chr = "1234567890-,"
    display_every_page = "1, 2, 3, etc..."
    default_display_range = "Ex: 2, 5, 8-10, 15-25"
    
    send_email = False
    outlook = win32com.client.Dispatch('outlook.application')
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())