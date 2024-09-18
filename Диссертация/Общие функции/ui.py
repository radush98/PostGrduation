import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import findWeight2base
import findWeight4base
import nonlin
import nonlin4
import ci2
import matrixToStr
import decompose_method
import base4
import base2

Sboxes = [
    '[0, 4, 12, 85, 93, 174, 255, 89, 162, 81, 247, 251, 8, 166, 243, 170, 20, 28, 101, 16, 190, 207, 105, 109, 97, 199, 203, 178, 182, 195, 186, 24, 44, 117, 32, 36, 223, 121, 125, 142, 215, 219, 130, 113, 211, 138, 40, 134, 69, 48, 52, 60, 73, 77, 158, 239, 235, 146, 65, 231, 154, 56, 150, 227, 68, 76, 149, 64, 238, 63, 153, 157, 145, 55, 59, 226, 230, 51, 234, 72, 92, 165, 80, 84, 15, 169, 173, 254, 7, 11, 242, 161, 3, 250, 88, 246, 181, 96, 100, 108, 185, 189, 206, 31, 27, 194, 177, 23, 202, 104, 198, 19, 112, 116, 124, 133, 141, 222, 47, 137, 210, 129, 39, 43, 120, 214, 35, 218,        140, 213, 128, 132, 127, 217, 221, 46, 119, 123, 34, 209, 115, 42, 136, 38, 229, 144, 148, 156, 233, 237, 62, 79, 75, 50, 225, 71, 58, 152, 54, 67, 160, 164, 172, 245, 253, 14, 95, 249, 2, 241, 87, 91, 168, 6, 83, 10, 180, 188, 197, 176, 30, 111, 201, 205, 193, 103, 107, 18, 22, 99, 26, 184, 21, 192, 196, 204, 25, 29, 110, 191, 187, 98, 17, 183, 106, 200, 102, 179, 208, 212, 220, 37, 45, 126, 143, 41, 114, 33, 135, 139, 216, 118, 131, 122, 228, 236, 53, 224, 78, 159, 57, 61, 49, 151, 155, 66, 70, 147, 74, 232, 252, 5, 240, 244, 175, 9, 13, 94, 167, 171, 82, 1, 163, 90, 248, 86]',
    '[0, 4, 8, 243, 93, 174, 12, 162, 255, 166, 89, 247, 85, 81, 170, 251, 20, 24, 195, 16, 190, 28, 178, 109, 182, 105, 199, 207, 97, 186, 203, 101, 40, 211, 32, 36, 44, 130, 125, 142, 121, 215, 223, 134, 138, 219, 117, 113, 227, 48, 52, 56, 146, 77, 158, 60, 231, 239, 150, 73, 235, 69, 65, 154, 68, 72, 51, 64, 238, 76, 226, 157, 230, 153, 55, 63, 145, 234, 59, 149, 88, 3, 80, 84, 92, 242, 173, 254, 169, 7, 15, 246, 250, 11, 165, 161, 19, 96, 100, 104, 194, 189, 206, 108, 23, 31, 198, 185, 27, 181, 177, 202, 112, 116, 120, 35, 141, 222, 124, 210, 47, 214, 137, 39, 133, 129, 218, 43, 136, 115, 128, 132, 140, 34, 221, 46, 217, 119, 127, 38, 42, 123, 213, 209, 67, 144, 148, 152, 50, 237, 62, 156, 71, 79, 54, 233, 75, 229, 225, 58, 160, 164, 168, 83, 253, 14, 172, 2, 95, 6, 249, 87, 245, 241, 10, 91, 180, 184, 99, 176, 30, 188, 18, 205, 22, 201, 103, 111, 193, 26, 107, 197, 179, 192, 196, 200, 98, 29, 110, 204, 183, 191, 102, 25, 187, 21, 17, 106, 208, 212, 216, 131, 45, 126, 220, 114, 143, 118, 41, 135, 37, 33, 122, 139, 228, 232, 147, 224, 78, 236, 66, 61, 70, 57, 151, 159, 49, 74, 155, 53, 248, 163, 240, 244, 252, 82, 13, 94, 9, 167, 175, 86, 90, 171, 5, 1]',
    '[85, 4, 170, 174, 166, 8, 0, 89, 243, 93, 162, 81, 247, 12, 255, 251, 20, 186, 190, 101, 24, 16, 105, 182, 109, 178, 97, 195, 28, 207, 203, 199, 138, 142, 117, 36, 32, 121, 134, 40, 130, 113, 211, 125, 223, 219, 215, 44, 158, 69, 52, 154, 73, 150, 56, 48, 65, 227, 77, 146, 235, 231, 60, 239, 68, 234, 238, 149, 72, 64, 153, 230, 157, 226, 145, 51, 76, 63, 59, 55, 250, 254, 165, 84, 80, 169, 246, 88, 242, 161, 3, 173, 15, 11, 7, 92, 206, 181, 100, 202, 185, 198, 104, 96, 177, 19, 189, 194, 27, 23, 108, 31, 133, 116, 218, 222, 214, 120, 112, 137, 35, 141, 210, 129, 39, 124, 47, 43, 42, 46, 213, 132, 128, 217, 38, 136, 34, 209, 115, 221, 127, 123, 119, 140, 62, 229, 148, 58, 233, 54, 152, 144, 225, 67, 237, 50, 75, 71, 156, 79, 245, 164, 10, 14, 6, 168, 160, 249, 83, 253, 2, 241, 87, 172, 95, 91, 180, 26, 30, 197, 184, 176, 201, 22, 205, 18, 193, 99, 188, 111, 107, 103, 110, 21, 196, 106, 25, 102, 200, 192, 17, 179, 29, 98, 187, 183, 204, 191, 37, 212, 122, 126, 118, 216, 208, 41, 131, 45, 114, 33, 135, 220, 143, 139, 228, 74, 78, 53, 232, 224, 57, 70, 61, 66, 49, 147, 236, 159, 155, 151, 90, 94, 5, 244, 240, 9, 86, 248, 82, 1, 163, 13, 175, 171, 167, 252]',
    '[93, 12, 170, 166, 247, 89, 174, 85, 255, 251, 243, 8, 0, 81, 162, 4, 28, 186, 182, 109, 105, 190, 101, 199, 203, 195, 24, 207, 97, 178, 20, 16, 138, 134, 125, 44, 142, 117, 215, 121, 211, 40, 223, 219, 130, 36, 32, 113, 150, 77, 60, 154, 69, 231, 73, 158, 56, 239, 235, 227, 52, 48, 65, 146, 76, 234, 230, 157, 153, 238, 149, 55, 59, 51, 72, 63, 145, 226, 68, 64, 250, 246, 173, 92, 254, 165, 7, 169, 3, 88, 15, 11, 242, 84, 80, 161, 198, 189, 108, 202, 181, 23, 185, 206, 104, 31, 27, 19, 100, 96, 177, 194, 141, 124, 218, 214, 39, 137, 222, 133, 47, 43, 35, 120, 112, 129, 210, 116, 42, 38, 221, 140, 46, 213, 119, 217, 115, 136, 127, 123, 34, 132, 128, 209, 54, 237, 156, 58, 229, 71, 233, 62, 152, 79, 75, 67, 148, 144, 225, 50, 253, 172, 10, 6, 87, 249, 14, 245, 95, 91, 83, 168, 160, 241, 2, 164, 188, 26, 22, 205, 201, 30, 197, 103, 107, 99, 184, 111, 193, 18, 180, 176, 102, 29, 204, 106, 21, 183, 25, 110, 200, 191, 187, 179, 196, 192, 17, 98, 45, 220, 122, 118, 135, 41, 126, 37, 143, 139, 131, 216, 208, 33, 114, 212, 236, 74, 70, 61, 57, 78, 53, 151, 155, 147, 232, 159, 49, 66, 228, 224, 90, 86, 13, 252, 94, 5, 167, 9, 163, 248, 175, 171, 82, 244, 240, 1]'
]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 869)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 10, 861, 181))
        self.list.setObjectName("list")
        self.list.addItems(Sboxes)
        self.list.itemClicked.connect(self.decomposeBlock)

        self.gen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gen_btn.setGeometry(QtCore.QRect(130, 420, 93, 28))
        self.gen_btn.setObjectName("gen_btn")
        self.gen_btn.clicked.connect(self.generateGood)

        self.show_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_btn.setGeometry(QtCore.QRect(20, 420, 93, 28))
        self.show_btn.setObjectName("show_btn")
        self.show_btn.clicked.connect(self.calculateResults)

        self.dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.dropdown.setGeometry(QtCore.QRect(750, 420, 101, 22))
        self.dropdown.setObjectName("dropdown")
        self.dropdown.addItems(['2-logic', '4-logic'])

        self.stats = QtWidgets.QGroupBox(self.centralwidget)
        self.stats.setGeometry(QtCore.QRect(20, 470, 851, 331))
        self.stats.setObjectName("stats")

        self.nonlin_lbl = QtWidgets.QLabel(self.stats)
        self.nonlin_lbl.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.nonlin_lbl.setObjectName("nonlin_lbl")

        self.nonlin_input = QtWidgets.QLineEdit(self.stats)
        self.nonlin_input.setGeometry(QtCore.QRect(60, 30, 113, 22))
        self.nonlin_input.setObjectName("nonlin_input")

        self.SAC_lbl = QtWidgets.QLabel(self.stats)
        self.SAC_lbl.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.SAC_lbl.setObjectName("SAC_lbl")

        self.SAC_input = QtWidgets.QTextEdit(self.stats)
        self.SAC_input.setGeometry(QtCore.QRect(13, 96, 401, 221))
        self.SAC_input.setObjectName("SAC_input")

        self.CI_input = QtWidgets.QTextEdit(self.stats)
        self.CI_input.setGeometry(QtCore.QRect(433, 96, 401, 221))
        self.CI_input.setObjectName("CI_input")

        self.CI_lbl = QtWidgets.QLabel(self.stats)
        self.CI_lbl.setGeometry(QtCore.QRect(440, 70, 55, 16))
        self.CI_lbl.setObjectName("CI_lbl")

        self.decomposes = QtWidgets.QListWidget(self.centralwidget)
        self.decomposes.setGeometry(QtCore.QRect(10, 210, 861, 181))
        self.decomposes.setObjectName("decomposes")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generator Demo"))
        self.gen_btn.setText(_translate("MainWindow", "Generate"))
        self.show_btn.setText(_translate("MainWindow", "Show"))
        self.stats.setTitle(_translate("MainWindow", "Stats:"))
        self.nonlin_lbl.setText(_translate("MainWindow", "Nonlin:"))
        self.SAC_lbl.setText(_translate("MainWindow", "SAC:"))
        self.CI_lbl.setText(_translate("MainWindow", "CI"))

    def decomposeBlock(self):
        Sbox = eval(self.list.currentItem().text())
        funcs = base2.funcs2int(base4.divideToFunctions(Sbox, False, len(Sbox)))
        
        self.decomposes.clear()
        self.decomposes.addItems([str(f) for f in funcs])

    def calculateResults(self):
        content = self.list.currentItem().text()
        Sbox = eval(content)

        current_mode = self.dropdown.currentText()

        if current_mode == '2-logic':
            self.base2results(Sbox)
        
        else:
            self.base4results(Sbox)

    def generateGood(self):
        self.list.clear()
        self.list.addItem(str(decompose_method.generateBlock()))

    def base2results(self, Sbox):
        f2 = findWeight2base.calculateWeight(Sbox).createFuns()
        self.SAC_input.setText(matrixToStr.matrixToStr(f2))

        n2 = nonlin.calculateSbox(Sbox)
        self.nonlin_input.setText(str(min(n2)))

        c2 = ci2.correlationCalc(Sbox)
        self.CI_input.setText(matrixToStr.matrixToStr(c2))

    def base4results(self, Sbox):
        f4 = findWeight4base.calculateWeight(Sbox).createFuns()
        self.SAC_input.setText(matrixToStr.matrixToStr(f4))

        n4 = nonlin4.calculateSbox(Sbox)
        self.nonlin_input.setText(str(round(min(n4))))

        c4 = ci2.correlationCalc(Sbox)
        self.CI_input.setText(matrixToStr.matrixToStr(c4))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
