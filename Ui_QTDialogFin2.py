# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\WinAuto\Automation\QTDialogVer2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import time
class AutomationThread(QThread):
    val_buf = []
    def __init__(self):
        super(AutomationThread,self).__init__()
    def run(self):
        for i in range(10):
            print(self.val_buf)
            time.sleep(1)
    def SettingTarget(self, val_list):
        self.val_buf = val_list
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1117, 537)
        self.autowork = AutomationThread()
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(860, 460, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(121, 51, 731, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_3.setMaximum(2999)
        self.horizontalSlider_3.setProperty("value", 0)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout.addWidget(self.horizontalSlider_3)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setMaximum(2999)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_6.setMaximum(2999)
        self.horizontalSlider_6.setProperty("value", 0)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.verticalLayout.addWidget(self.horizontalSlider_6)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_5.setMaximum(2999)
        self.horizontalSlider_5.setProperty("value", 0)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout.addWidget(self.horizontalSlider_5)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_4.setMaximum(2999)
        self.horizontalSlider_4.setProperty("value", 0)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout.addWidget(self.horizontalSlider_4)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_7.setMaximum(2999)
        self.horizontalSlider_7.setProperty("value", 0)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.verticalLayout.addWidget(self.horizontalSlider_7)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_2.setMaximum(2999)
        self.horizontalSlider_2.setProperty("value", 0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(860, 60, 121, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(990, 60, 101, 371))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 60, 63, 361))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 460, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.horizontalSlider_3, self.horizontalSlider)
        Dialog.setTabOrder(self.horizontalSlider, self.horizontalSlider_6)
        Dialog.setTabOrder(self.horizontalSlider_6, self.horizontalSlider_5)
        Dialog.setTabOrder(self.horizontalSlider_5, self.horizontalSlider_4)
        Dialog.setTabOrder(self.horizontalSlider_4, self.horizontalSlider_7)
        Dialog.setTabOrder(self.horizontalSlider_7, self.horizontalSlider_2)
        Dialog.setTabOrder(self.horizontalSlider_2, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Dialog.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Dialog.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        Dialog.setTabOrder(self.lineEdit_7, self.pushButton)
        self.horizontalSlider_3.valueChanged['int'].connect(self.Slider3changeEdit)
        self.lineEdit.editingFinished.connect(self.EditchangeSlider3)
        self.horizontalSlider.valueChanged['int'].connect(self.SliderchangeEdit2)
        self.lineEdit_2.editingFinished.connect(self.Edit2changeSlider)
        self.horizontalSlider_6.valueChanged['int'].connect(self.Slider6changeEdit3)
        self.lineEdit_3.editingFinished.connect(self.Edit3changeSlider6)
        self.horizontalSlider_5.valueChanged['int'].connect(self.Slider5changeEdit4)
        self.lineEdit_4.editingFinished.connect(self.Edit4changeSlider5)
        self.horizontalSlider_4.valueChanged['int'].connect(self.Slider4changeEdit5)
        self.lineEdit_5.editingFinished.connect(self.Edit5changeSlider4)
        self.horizontalSlider_7.valueChanged['int'].connect(self.Slider7changeEdit6)
        self.lineEdit_6.editingFinished.connect(self.Edit6changeSlider7)
        self.horizontalSlider_2.valueChanged['int'].connect(self.Slider2changeEdit7)
        self.lineEdit_7.editingFinished.connect(self.Edit7changeSlider2)
        self.pushButton.clicked.connect(self.startThread)
        self.pushButton_2.clicked.connect(self.value_set)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)
    def startThread(self):
        self.autowork.start()
    def value_set(self):
        self.autowork.SettingTarget([1,2,3,4,5,6,7,8,9,10])
    def Slider3changeEdit(self, position):
        self.lineEdit.setText(str(position/100.0))
    def EditchangeSlider3(self):
        fval = float(self.lineEdit.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_3.setValue(int(fval))
    def SliderchangeEdit2(self, position):
        self.lineEdit_2.setText(str(position/100.0))
    def Edit2changeSlider(self):
        fval = float(self.lineEdit_2.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider.setValue(int(fval))
    def Slider6changeEdit3(self, position):
        self.lineEdit_3.setText(str(position/100.0))
    def Edit3changeSlider6(self):
        fval = float(self.lineEdit_3.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_6.setValue(int(fval))
    def Slider5changeEdit4(self, position):
        self.lineEdit_4.setText(str(position/100.0))
    def Edit4changeSlider5(self):
        fval = float(self.lineEdit_4.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_5.setValue(int(fval))
    def Slider4changeEdit5(self, position):
        self.lineEdit_5.setText(str(position/100.0))
    def Edit5changeSlider4(self):
        fval = float(self.lineEdit_5.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_4.setValue(int(fval))
    def Slider7changeEdit6(self, position):
        self.lineEdit_6.setText(str(position/100.0))
    def Edit6changeSlider7(self):
        fval = float(self.lineEdit_6.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_7.setValue(int(fval))
    def Slider2changeEdit7(self, position):
        self.lineEdit_7.setText(str(position/100.0))
    def Edit7changeSlider2(self):
        fval = float(self.lineEdit_7.text())*100 
        fval = fval if fval <= 2999 else 2999
        fval = fval if fval >=0 else 0
        self.horizontalSlider_2.setValue(int(fval))
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "INIT"))
        self.lineEdit.setText(_translate("Dialog", "0.00"))
        self.lineEdit_2.setText(_translate("Dialog", "0.00"))
        self.lineEdit_3.setText(_translate("Dialog", "0.00"))
        self.lineEdit_4.setText(_translate("Dialog", "0.00"))
        self.lineEdit_5.setText(_translate("Dialog", "0.00"))
        self.lineEdit_6.setText(_translate("Dialog", "0.00"))
        self.lineEdit_7.setText(_translate("Dialog", "0.00"))
        self.label_8.setText(_translate("Dialog", "0.0"))
        self.label_9.setText(_translate("Dialog", "0.0"))
        self.label_10.setText(_translate("Dialog", "0.0"))
        self.label_11.setText(_translate("Dialog", "0.0"))
        self.label_12.setText(_translate("Dialog", "0.0"))
        self.label_13.setText(_translate("Dialog", "0.0"))
        self.label_14.setText(_translate("Dialog", "0.0"))
        self.label.setText(_translate("Dialog", "Back 2"))
        self.label_2.setText(_translate("Dialog", "Back 4"))
        self.label_3.setText(_translate("Dialog", "Back 6"))
        self.label_4.setText(_translate("Dialog", "Back 8"))
        self.label_5.setText(_translate("Dialog", "Back 12"))
        self.label_6.setText(_translate("Dialog", "Back 14"))
        self.label_7.setText(_translate("Dialog", "Back 24"))
        self.pushButton_2.setText(_translate("Dialog", "InputVal"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

