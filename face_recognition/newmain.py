from master import MyWindow
from master import  QtWidgets, QtGui, QtCore
import PIL
import dlib
import PyQt5
import face_recognition
import pymysql
import numpy
import cv2
import sys
import  os

os.path.abspath(os.path.dirname('D:\\Anaconda3\\envs\\py36\\Scripts\\pyinstaller.exe\\__main__.pyo'))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # pyqt5 必须创建的应用对象
    mywindow = MyWindow()
    mywindow.show()  # show 方法在屏幕上显示
    sys.exit(app.exec_())  # 保证不留垃圾的退出 exec是python 的关键字 所以用exec_代替




