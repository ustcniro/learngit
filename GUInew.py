import sys
import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit,QMenu, QLineEdit,QInputDialog,QButtonGroup,QRadioButton )
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication,Qt
from APInew import apifunction #导入自己编写的API文件

#注释中标识study的是学习相关操作 ，大部分与天气预报这个系统本身无关

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QLabel, QVBoxLayout,QHeaderView
from VICEUInew import Demo


class  guifunction(QMainWindow):

     def __init__(self):
        super().__init__()                         #study超类，用以解决多重继承问题
        self.alldata = apifunction("", 1, "合肥")  #默认合肥的天气读取 ，继承apifuction的对象
        self.selectweek=0                       #0表示今天，1表示明天，2表示后天

        self.date = QLabel('日期')                 #创建各种QLabel用于显示获取的天气数据
        self.week = QLabel('星期')
        self.city = QLabel('城市(区域)')
        self.dawn = QLabel('黎明')
        self.day = QLabel('白天')
        self.night = QLabel('夜晚')
        self.weather = QLabel('天气')
        self.tempature= QLabel('气温')
        self.wind = QLabel('风')
        self.humid=QLabel('湿度')
        self.pm25 = QLabel('pm2.5')
        self.quality=QLabel('空气质量')
        self.lable11 = QLabel(self)
        self.lable12 = QLabel(self)
        self.lable13 = QLabel(self)
        self.lable21 = QLabel(self)
        self.lable22=  QLabel(self)
        self.lable23 = QLabel(self)

        self.lable31 = QLabel(self)
        self.lable32 = QLabel(self)
        self.lable33 = QLabel(self)
        self.lable41 = QLabel(self)
        self.lable42 = QLabel(self)
        self.lable43 = QLabel(self)
        self.lable51 = QLabel(self)
        self.lable52 = QLabel(self)
        self.lable53 = QLabel(self)

        self.viceUI1 = Demo()                       #显示天气类型窗口,城市类型窗口  demo类
        self.viceUI2 = Demo()
        self.viceUI3 = Demo()
        self.initUI()



     def obtaindata(self,city):                    #获取所要查询的城市的天气
        self.alldata.city=city
        self.alldata.urltype(1)
        self.alldata.urlget()
        self.alldata.mydata()
        print(self.alldata.data)
     def obtainweathertype(self):                  #获取所要查询的天气类型
        self.alldata.urltype(2)
        self.alldata.urlget()
        self.alldata.mydata()
        print(self.alldata.weathertype)
     def obtaincitytype(self):                     #获取所要查询的城市信息
        self.alldata.urltype(3)
        self.alldata.urlget()
        self.alldata.mydata()
        print(self.alldata.citytype)


     def initUI(self):
         #构建初始化
         self.alldata.getkey()
        # self.obtaincitytype()
         print("2")
         # self.obtainweathertype()
         print("1")
      #  self.obtaindata("合肥")
         print("3")
         self.statusBar().showMessage('准备就绪')     #状态条
         self.setGeometry(500, 500, 700, 350)        # 设置窗口的位置和大小
         self.setWindowTitle('天气预报')              # 设置窗口的标题
         self.setWindowIcon(QIcon('forecast.jpg'))   # 设置窗口的图标，引用当前目录下的天气图片

         exitAct = QAction('退出(&E)', self)         #设置状态栏选项
         exitAct.setShortcut('Ctrl+Q')
         exitAct.setStatusTip('退出程序')
         exitAct.triggered.connect(qApp.quit)
         weathertypeAct =QAction('可查询的天气类型(&R)',self)
         weathertypeAct.setStatusTip('显示各种天气类型')
         weathertypeAct.triggered.connect(self.Showweathertype)
         citytypeAct =QAction('可查询的城市列表(&T)',self)
         citytypeAct.setStatusTip('显示可查询的城市')
         citytypeAct.triggered.connect(self.Showcitytype)


         menubar = self.menuBar()
         fileMenu = menubar.addMenu('选项(&F)')
         fileMenu.addAction(weathertypeAct)
         fileMenu.addAction(citytypeAct)
         fileMenu.addAction(exitAct)



         drawAct =QAction('温度变化图',self)
         drawAct.triggered.connect(self.Drawfunction)

         menubar = self.menuBar()
         fileMenu = menubar.addMenu('相关功能')
         fileMenu.addAction(drawAct)





         
         cityAct = QAction('选择城市',self)
         cityAct.setStatusTip('输入所需要查询的城市')
         cityAct1 = QAction('合肥', self)
         cityAct1.triggered.connect(self.gethefei)
         cityAct1.setStatusTip('合肥的天气')
         cityAct2 = QAction('长丰', self)
         cityAct2.triggered.connect(self.getchangfeng)
         cityAct2.setStatusTip('长丰的天气')
         cityAct3 = QAction('肥东', self)
         cityAct3.triggered.connect(self.getfeidong)
         cityAct3.setStatusTip('肥东的天气')
         cityAct4 = QAction('肥西', self)
         cityAct4.triggered.connect(self.getfeixi)
         cityAct4.setStatusTip('肥西的天气')




         # 工具棒
         self.toolbar = self.addToolBar('选择城市')
         self.toolbar.addAction(cityAct)
         self.toolbar = self.addToolBar('合肥')
         self.toolbar.addAction(cityAct1)
         self.toolbar = self.addToolBar('长丰')
         self.toolbar.addAction(cityAct2)
         self.toolbar = self.addToolBar('肥东')
         self.toolbar.addAction(cityAct3)
         self.toolbar = self.addToolBar('肥西')
         self.toolbar.addAction(cityAct4)

         self.btn = QPushButton('点击输入', self)
         self.btn.move(20, 60)
         self.btn.clicked.connect(self.showDialog)
         self.le = QLineEdit(self)
         self.le.setMaximumWidth(100)
         self.le.setPlaceholderText("例如：北京")
         self.le.move(130, 60)

         # 单选框
         self.rb1 = QRadioButton('今天', self)
         self.rb1.move(250, 60)
         self.rb2 = QRadioButton('明天', self)
         self.rb2.move(320, 60)
         self.rb3 = QRadioButton('后天', self)
         self.rb3.move(390, 60)
         self.bt1 = QPushButton('查询', self)
         self.bt1.move(460, 60)
         self.bg1 = QButtonGroup(self)
         self.bg1.addButton(self.rb1, 1)
         self.bg1.addButton(self.rb2, 2)
         self.bg1.addButton(self.rb3, 3)
         self.bg1.buttonClicked.connect(self.rbclicked)
         self.bt1.clicked.connect(self.finddata)

         #self.structure()

        #mainUI()
         self.show()                                 # 显示窗口
         self.center()                               # 设置窗口到中心

     def finddata(self):
         print(self.alldata.city)
         self.structure()
     def rbclicked(self):
         sender = self.sender()
         if sender == self.bg1:
             if self.bg1.checkedId() == 1:
                 self.selectweek = 0
                 print(self.selectweek)
             elif self.bg1.checkedId() == 2:
                 self.selectweek= 1
                 print(self.selectweek)

             elif self.bg1.checkedId() == 3:
                 self.selectweek = 2
                 print(self.selectweek)


     def showDialog(self):                    #输入城市，并读取
         text, ok = QInputDialog.getText(self, '城市', '请输入城市名:')

         if ok:
            self.le.setText(str(text))
            self.alldata.city=str(text)
            self.obtaindata(self.alldata.city)
            print(self.alldata.city)
     def gethefei(self):
         self.obtaindata("合肥")
         self.le.setText("合肥")
         self.structure()

     def getchangfeng(self):
         self.obtaindata("长丰")
         self.le.setText("长丰")
         self.structure()

     def getfeidong(self):
         self.obtaindata("肥东")
         self.le.setText("肥东")
         self.structure()


     def getfeixi(self):
         self.obtaindata("肥西")
         self.le.setText("肥西")
         self.structure()


     def structure(self):  # 用于显示天气信息
         self.central_widget = QWidget()              # 建一个 central widget
         self.setCentralWidget(self.central_widget)   # 设置 centralWidget

         self.lable11.setText(self.alldata.city)      # 城市信息
         self.lable12.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['date'])  # 日期信息
         self.lable13.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['week'])  # 星期信息
         self.lable21.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['dawn'][1])  # 天气信息 dawn
         print("ok1")
         self.lable22.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['day'][1])  # 天气信息 day
         self.lable23.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['night'][1])  # 天气信息 night
         print("ok2")
         self.lable31.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['dawn'][2])  # 温度信息
         self.lable32.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['day'][2])
         self.lable33.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['night'][2])
         print("ok3")
         self.lable41.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['dawn'][3] +
                              self.alldata.data['result']['data']['weather'][self.selectweek]['info']['dawn'][4])  # 风信息
         self.lable42.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['day'][3] +
                              self.alldata.data['result']['data']['weather'][self.selectweek]['info']['day'][4])
         self.lable43.setText(self.alldata.data['result']['data']['weather'][self.selectweek]['info']['night'][3] +
                              self.alldata.data['result']['data']['weather'][self.selectweek]['info']['night'][4])
         print("ok4")
         print(self.alldata.data['result']['data']['realtime']['weather']['humidity'])
         if  self.selectweek==0:
              print("222222")
              self.lable51.setText(self.alldata.data['result']['data']['realtime']['weather']['humidity'])
              print("jinlaile")
              self.lable52.setText(self.alldata.data['result']['data']['pm25']['pm25']['pm25'])
              self.lable53.setText(self.alldata.data['result']['data']['pm25']['pm25']['quality'])
         else :
              self.lable51.setText("无数据")
              self.lable52.setText("无数据")
              self.lable53.setText("无数据")



         print(self.lable32.text())

         grid = QGridLayout()  # 采用格栅布局
         self.centralWidget().setLayout(grid)
         grid.setSpacing(10)  # 设置网格间的间隔
         print("b")
         grid.addWidget(self.btn, 1, 1)
         grid.addWidget(self.le, 1, 2)
         grid.addWidget(self.rb1, 1, 3)
         grid.addWidget(self.rb2, 1, 4)
         grid.addWidget(self.rb3, 1, 5)
         grid.addWidget(self.bt1, 1, 6)
         grid.addWidget(self.city, 3, 1)
         grid.addWidget(self.date, 3, 3)
         grid.addWidget(self.week, 3, 5)
         grid.addWidget(self.dawn, 5, 2)
         grid.addWidget(self.day, 5, 4)
         grid.addWidget(self.night, 5, 6)
         grid.addWidget(self.weather, 6, 1)
         grid.addWidget(self.tempature,7, 1)
         print("c")
         grid.addWidget(self.wind, 8, 1)



         grid.addWidget(self.humid, 4, 1)
         grid.addWidget(self.pm25, 4, 3)
         grid.addWidget(self.quality, 4, 5)
         grid.addWidget(self.lable51, 4, 2)
         grid.addWidget(self.lable52, 4, 4)
         grid.addWidget(self.lable53, 4, 6)
         print("成功")
         grid.addWidget(self.lable11, 3, 2)
         grid.addWidget(self.lable12, 3, 4)
         grid.addWidget(self.lable13, 3, 6)
         grid.addWidget(self.lable21, 6, 2)
         grid.addWidget(self.lable22, 6, 4)
         grid.addWidget(self.lable23, 6, 6)
         grid.addWidget(self.lable31, 7, 2)
         grid.addWidget(self.lable32, 7, 4)
         grid.addWidget(self.lable33, 7, 6)
         grid.addWidget(self.lable41, 8, 2)
         grid.addWidget(self.lable42, 8, 4)
         grid.addWidget(self.lable43, 8, 6)

         self.setLayout(grid)

     def contextMenuEvent(self, event):              #study学习gui方法 ，右击出现上下文菜单
         cmenu = QMenu(self)
         newAct = cmenu.addAction("合肥天气")
         quitAct = cmenu.addAction("退出")
         action = cmenu.exec_(self.mapToGlobal(event.pos()))
         if action == quitAct:
             qApp.quit()
         if action == newAct:
             self.alldata.city="合肥"
            # self.structure()

     def keyPressEvent(self, e):    # study 按Ese可退出
         if e.key() == Qt.Key_Escape:
             self.close()
     def Showweathertype(self):
         self.obtainweathertype()
         self.viceUI1.kind1=self.alldata.weathertype   #天气类型字典的读取
         self.viceUI1.fillinweathertype()
         self.viceUI1.show()
     def Drawfunction(self):
         self.viceUI3.kind3=self.alldata.data        #查询信息字典的读取
         print("可以")
         self.viceUI3.draw()
         print("还行")


     def Showcitytype(self):
         self.obtaincitytype()
         self.viceUI2.kind2 = self.alldata.citytype  # 城市类型字典的读取
         self.viceUI2.fillincitytype()
         self.viceUI2.show()

     def center(self):           #study
         # 获得窗口
         qr = self.frameGeometry()
         # 获得屏幕中心点
         cp = QDesktopWidget().availableGeometry().center()
         # 显示到屏幕中心
         qr.moveCenter(cp)
         self.move(qr.topLeft())

"""  def closeEvent(self, event):  #study退出消息框的构建

         reply = QMessageBox.question(self, '提示',
                                      "确定要退出吗", QMessageBox.yes|
                                      QMessageBox.No, QMessageBox.no)
         if reply == QMessageBox.Yes:
             event.accept()
         else:
             event.ignore() """

if __name__ == '__main__':
     app = QApplication(sys.argv)  # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
     run = guifunction()
     run.show()
     sys.exit(app.exec_())         # 系统exit()方法确保应用程序干净的退出
                                   # exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
