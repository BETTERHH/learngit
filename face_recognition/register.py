from face2 import QtCore, QtGui, QtWidgets
from face2 import Ui_Form as ui
import sys
import mysql_create
import pymysql
import cv2


class MyWindow(QtWidgets.QMainWindow, ui):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("新用户注册")
        self.setWindowIcon(QtGui.QIcon("pre_data/logo.jpg"))  # 设置程序的图标
        self.status_num = 0
        palettel = QtGui.QPalette()
        palettel.setColor(self.backgroundRole(), QtGui.QColor(100, 150, 200))   #设置背景颜色
        #palettel.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("C://Users/lenovo/Desktop/test-data/test1.jpg")))
        self.setPalette(palettel)

        self.stu_name = None
        self.stu_number = None


    def confirm(self):
        stu_number = str(self.lineEdit_2.text())
        stu_name = str(self.lineEdit.text())

        conn, cur = mysql_create.connect_sql()   #与数据库建立联系

        if len(stu_number)!=10 or (stu_number.isdigit()!=True):#判断输入学号是否正确  不正确则弹框提示
            my_button = QtWidgets.QMessageBox.information(self, '输入错误', u'请输入正确的学号')

        elif len(stu_number)==10 and stu_number.isdigit():#输入学号正确则检测是否已经注册 及数据库中书否存在该学号

            input_id = stu_number
            sql_query = 'select * from students where id = "' + input_id + '" '  # 转义    中间的两个” 用来转义
            cur.execute(sql_query)#sql_query为组合查询
            result = cur.fetchone()#数据库查询并返回结果



            if result == None:  #如果不存在 则新建
                print("不存在")
                self.stu_name = stu_name
                self.stu_number = stu_number
                self.status_num = 1
                '''
                #存入人脸的照片
                cap = cv2.VideoCapture(0)
                new_path = 'image_data/' + str(stu_number) + '.jpg'

                face_cascade = cv2.CascadeClassifier(
                    'LBP/lbpcascade_frontalface.xml')  # 打开LBP模型文件  
                '''

            else:    #如果存在则弹框提示
                my_button1 = QtWidgets.QMessageBox.information(self, '学号输入错误', u'该学生已经注册')


