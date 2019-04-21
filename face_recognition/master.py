from face import QtCore, QtGui, QtWidgets
from face import Ui_Form as ui
from maininter import MyWindow as maininterface

class MyWindow(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("人脸识别")
        self.setWindowIcon(QtGui.QIcon("pre_data/logo.jpg"))  # 设置程序的图标
        self.label.setPixmap(QtGui.QPixmap("pre_data/logo.jpg"))

    def pushbutton(self):
        username = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())

        if username == "zhongbei":
            if password == "666":
                self.next = maininterface()
                self.close()
                self.next.show()
            else:
                my_button = QtWidgets.QMessageBox.information(self, '输入错误', u'请输入正确的密码')
        else:
            my_button = QtWidgets.QMessageBox.information(self, '输入错误', u'请输入正确的账号')