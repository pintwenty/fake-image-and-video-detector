


from PyQt5 import QtCore, QtGui, QtWidgets
from Detection  import fakedetection
from Camera2 import CaptureImage
class Ui_Camera(object):

    def getCameraImage(self, event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def detect(self):
        result = fakedetection("cameraimg.jpg")
        if result == "unknown/fake":
            self.label_2.setText("Result :  Fake")
        else:
            self.label_2.setText("Result :  Authentic")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 493)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 50, 341, 51))
        self.label.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(230, 120, 161, 121))
        self.camera.setStyleSheet("image: url(../FakeImageDetection/image/camera.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent=self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 250, 181, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 310, 121, 41))
        self.pushButton.setStyleSheet("font: 75 12pt \"Vani\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.detect)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 400, 401, 61))
        self.label_2.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fake Image Detection"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))
        self.pushButton.setText(_translate("Dialog", "Detect"))
        self.label_2.setText(_translate("Dialog", "Result :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
