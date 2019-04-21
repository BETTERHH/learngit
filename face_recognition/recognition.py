from face3 import QtCore, QtGui, QtWidgets
from face3 import Ui_Form as ui


class MyWindow(QtWidgets.QMainWindow, ui):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("设置信息")
        self.setWindowIcon(QtGui.QIcon("pre_data/logo.jpg"))  # 设置程序的图标
        palettel = QtGui.QPalette()
        palettel.setColor(self.backgroundRole(), QtGui.QColor(100, 150, 200))  # 设置背景颜色
        self.setPalette(palettel)

        self.status_num = 0
        self.class_name = None
        self.rec_time = None

    def confirm(self):

        self.rec_time = self.lineEdit_2.text()
        self.class_name = self.lineEdit.text()
        self.status_num = 2





