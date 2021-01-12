# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartblue.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SmartBlueForm(object):
    def setupUi(self, SmartBlueForm):
        SmartBlueForm.setObjectName("SmartBlueForm")
        SmartBlueForm.resize(460, 250)
        SmartBlueForm.setMinimumSize(QtCore.QSize(460, 250))
        SmartBlueForm.setMaximumSize(QtCore.QSize(460, 250))
        self.groupBoxTop = QtWidgets.QGroupBox(SmartBlueForm)
        self.groupBoxTop.setEnabled(True)
        self.groupBoxTop.setGeometry(QtCore.QRect(10, 10, 441, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBoxTop.setFont(font)
        self.groupBoxTop.setWhatsThis("")
        self.groupBoxTop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBoxTop.setAutoFillBackground(False)
        self.groupBoxTop.setStyleSheet("QGroupBox {\n"
"    border: 1px solid silver;\n"
"    border-radius: 5px;\n"
"    margin-top: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 8px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.groupBoxTop.setFlat(True)
        self.groupBoxTop.setCheckable(False)
        self.groupBoxTop.setObjectName("groupBoxTop")
        self.labelLight = QtWidgets.QLabel(self.groupBoxTop)
        self.labelLight.setGeometry(QtCore.QRect(0, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLight.setFont(font)
        self.labelLight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelLight.setObjectName("labelLight")
        self.lineEditLight = QtWidgets.QLineEdit(self.groupBoxTop)
        self.lineEditLight.setEnabled(True)
        self.lineEditLight.setGeometry(QtCore.QRect(110, 30, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditLight.setFont(font)
        self.lineEditLight.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLight.setReadOnly(True)
        self.lineEditLight.setObjectName("lineEditLight")
        self.labelHumidity = QtWidgets.QLabel(self.groupBoxTop)
        self.labelHumidity.setGeometry(QtCore.QRect(20, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelHumidity.setFont(font)
        self.labelHumidity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelHumidity.setObjectName("labelHumidity")
        self.labelTemp = QtWidgets.QLabel(self.groupBoxTop)
        self.labelTemp.setGeometry(QtCore.QRect(10, 90, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTemp.setFont(font)
        self.labelTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTemp.setObjectName("labelTemp")
        self.lineEditHumidity = QtWidgets.QLineEdit(self.groupBoxTop)
        self.lineEditHumidity.setEnabled(True)
        self.lineEditHumidity.setGeometry(QtCore.QRect(110, 60, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditHumidity.setFont(font)
        self.lineEditHumidity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHumidity.setReadOnly(True)
        self.lineEditHumidity.setObjectName("lineEditHumidity")
        self.lineEditTemp = QtWidgets.QLineEdit(self.groupBoxTop)
        self.lineEditTemp.setEnabled(True)
        self.lineEditTemp.setGeometry(QtCore.QRect(110, 90, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTemp.setFont(font)
        self.lineEditTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTemp.setReadOnly(True)
        self.lineEditTemp.setObjectName("lineEditTemp")
        self.labelLux = QtWidgets.QLabel(self.groupBoxTop)
        self.labelLux.setGeometry(QtCore.QRect(190, 30, 31, 18))
        self.labelLux.setObjectName("labelLux")
        self.labelRH = QtWidgets.QLabel(self.groupBoxTop)
        self.labelRH.setGeometry(QtCore.QRect(190, 60, 31, 18))
        self.labelRH.setObjectName("labelRH")
        self.labelC = QtWidgets.QLabel(self.groupBoxTop)
        self.labelC.setGeometry(QtCore.QRect(190, 90, 31, 18))
        self.labelC.setObjectName("labelC")
        self.lineEditTempLED = QtWidgets.QLineEdit(self.groupBoxTop)
        self.lineEditTempLED.setEnabled(True)
        self.lineEditTempLED.setGeometry(QtCore.QRect(350, 90, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTempLED.setFont(font)
        self.lineEditTempLED.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTempLED.setReadOnly(True)
        self.lineEditTempLED.setObjectName("lineEditTempLED")
        self.labelTemp_2 = QtWidgets.QLabel(self.groupBoxTop)
        self.labelTemp_2.setGeometry(QtCore.QRect(220, 90, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTemp_2.setFont(font)
        self.labelTemp_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTemp_2.setObjectName("labelTemp_2")
        self.groupBoxLow = QtWidgets.QGroupBox(SmartBlueForm)
        self.groupBoxLow.setEnabled(True)
        self.groupBoxLow.setGeometry(QtCore.QRect(10, 150, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBoxLow.setFont(font)
        self.groupBoxLow.setWhatsThis("")
        self.groupBoxLow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBoxLow.setAutoFillBackground(False)
        self.groupBoxLow.setStyleSheet("QGroupBox {\n"
"    border: 1px solid silver;\n"
"    border-radius: 5px;\n"
"    margin-top: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 8px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.groupBoxLow.setFlat(True)
        self.groupBoxLow.setCheckable(False)
        self.groupBoxLow.setObjectName("groupBoxLow")
        self.labelTempTh = QtWidgets.QLabel(self.groupBoxLow)
        self.labelTempTh.setGeometry(QtCore.QRect(50, 30, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTempTh.setFont(font)
        self.labelTempTh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTempTh.setObjectName("labelTempTh")
        self.spinBoxTemp = QtWidgets.QSpinBox(self.groupBoxLow)
        self.spinBoxTemp.setGeometry(QtCore.QRect(210, 30, 191, 21))
        self.spinBoxTemp.setMinimum(25)
        self.spinBoxTemp.setMaximum(50)
        self.spinBoxTemp.setObjectName("spinBoxTemp")
        self.buttonStop = QtWidgets.QPushButton(SmartBlueForm)
        self.buttonStop.setGeometry(QtCore.QRect(350, 220, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonStop.setFont(font)
        self.buttonStop.setObjectName("buttonStop")
        self.buttonStart = QtWidgets.QPushButton(SmartBlueForm)
        self.buttonStart.setGeometry(QtCore.QRect(230, 220, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonStart.setFont(font)
        self.buttonStart.setObjectName("buttonStart")
        self.lableQuanquan = QtWidgets.QLabel(SmartBlueForm)
        self.lableQuanquan.setGeometry(QtCore.QRect(10, 220, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lableQuanquan.setFont(font)
        self.lableQuanquan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lableQuanquan.setObjectName("lableQuanquan")

        self.retranslateUi(SmartBlueForm)
        QtCore.QMetaObject.connectSlotsByName(SmartBlueForm)

    def retranslateUi(self, SmartBlueForm):
        _translate = QtCore.QCoreApplication.translate
        SmartBlueForm.setWindowTitle(_translate("SmartBlueForm", "Smart Blue for BG22 Bluetooth Funpack"))
        self.groupBoxTop.setTitle(_translate("SmartBlueForm", "Environment Conditions"))
        self.labelLight.setText(_translate("SmartBlueForm", "Ambient Light:"))
        self.lineEditLight.setText(_translate("SmartBlueForm", "No Data"))
        self.labelHumidity.setText(_translate("SmartBlueForm", "Humidity:"))
        self.labelTemp.setText(_translate("SmartBlueForm", "Temperature:"))
        self.lineEditHumidity.setText(_translate("SmartBlueForm", "No Data"))
        self.lineEditTemp.setText(_translate("SmartBlueForm", "No Data"))
        self.labelLux.setText(_translate("SmartBlueForm", "Lux"))
        self.labelRH.setText(_translate("SmartBlueForm", "%RH"))
        self.labelC.setText(_translate("SmartBlueForm", "C"))
        self.lineEditTempLED.setText(_translate("SmartBlueForm", "No Data"))
        self.labelTemp_2.setText(_translate("SmartBlueForm", ">= Temp. Th. LED :"))
        self.groupBoxLow.setTitle(_translate("SmartBlueForm", "Alarm Settings"))
        self.labelTempTh.setText(_translate("SmartBlueForm", "Temperature Threshold:"))
        self.buttonStop.setText(_translate("SmartBlueForm", "Stop"))
        self.buttonStart.setText(_translate("SmartBlueForm", "START"))
        self.lableQuanquan.setText(_translate("SmartBlueForm", "By Quanqua-BG3MDO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmartBlueForm = QtWidgets.QWidget()
    ui = Ui_SmartBlueForm()
    ui.setupUi(SmartBlueForm)
    SmartBlueForm.show()
    sys.exit(app.exec_())
