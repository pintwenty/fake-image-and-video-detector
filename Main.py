from PyQt5 import QtCore, QtGui, QtWidgets
from Camera import Ui_Camera
from Image import Ui_Image
from rename import rename
from resize import resize
from vid2jpeg import vid2jpg
from FakeImageDetection import train
class Ui_Main(object):

    def train(self):
        print("Image Preprocessing...")
        rename()
        print("Re-naming images complete!")
        resize()
        print("Re-sizing images complete!")
        print("Training KNN classifier...")
        classifier = train("../FakeImageDetection/train",
                           model_save_path="trained_knn_model.clf", n_neighbors=1)
        print("Training complete!")

    def image(self):
        self.home = QtWidgets.QDialog()
        self.ui = Ui_Image()
        self.ui.setupUi(self.home)
        self.home.show()

    def camera(self):
        self.c = QtWidgets.QDialog()
        self.ui = Ui_Camera()
        self.ui.setupUi(self.c)
        self.c.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 467)
        Dialog.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 150, 211, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.train)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 250, 211, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.image)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 350, 211, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.camera)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 30, 521, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.pushButton.setText(_translate("Dialog", "Training Dataset"))
        self.pushButton_2.setText(_translate("Dialog", "Image/Video"))
        self.pushButton_3.setText(_translate("Dialog", "Camera"))

        self.label.setText(_translate("Dialog", "Fake Image Detection"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
