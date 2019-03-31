import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit,QMenu, QLineEdit,QInputDialog,QButtonGroup,QRadioButton )
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication,Qt
import pyqtgraph as pg
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QLabel, QVBoxLayout,QHeaderView

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.kind1={}  #weathertype的存储字典
        self.kind2={}   #citytype的存储字典
        self.kind3={}   #存错用于画图的字典
        self.resize(650, 300)# 设置标题与初始大小
        self.datax=[0 for i in range(9) ]   #存储画图的x数据 时间
        self.datay=[0 for i in range(9)]   #存储画图的y数据 温度

    def draw(self):              # study  想用温度画个图，本来想用matplotlib，后来看到pyqtgraph有点厉害，就学学看
        i = 0
        for i in range(9):
              print("test")
              print(type(self.datax))
              print(self.kind3['result']['data']['f3h']['temperature'][0]['jg'])
              self.datax[i]=self.kind3['result']['data']['f3h']['temperature'][i]['jg'][:10]
              print("star")
              self.datay[i]=int(self.kind3['result']['data']['f3h']['temperature'][i]['jb'])
        print(self.datax)
        print(self.datay)
        print(type(self.datay[1]))



        x = range(9)



        self.win = pg.GraphicsWindow(title=self.kind3['result']['data']['pm25']['cityName'] + "气温走势图")
        print("不错")

        # 定义每一个x坐标值对应的字符列表，其形式为[(0,'20190329200000'),(1,'20190329230000')]
        ticks = [(i, j) for i, j in zip(x, self.datax)]

        strAxis = pg.AxisItem(orientation='bottom')
        strAxis.setTicks([ticks])
        self.plot1 = self.win.addPlot(title='气温走势图', axisItems={'bottom': strAxis})

        self.label = pg.TextItem()     #设置鼠标点的信息输出框
        self.plot1.addItem(self.label)
        #self.plot1.addLegend(size=(50, 50))
        self.plot1.showGrid(x=True, y=True, alpha=0.3)

        self.plot1.plot(x, self.datay,pen='r',name='温度值',symbolBrush=(255, 0, 0))   # 画图
        self.plot1.setLabel(axis='left', text='温度')                                    #设置横纵坐标
        self.plot1.setLabel(axis='bottom', text='时间')
        print("beauty")

        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        self.plot1.addItem(vLine, ignoreBounds=True)
        self.plot1.addItem(hLine, ignoreBounds=True)
        vb = self.plot1.vb

        def mouseMoved(evt):
            print("sttttt")
            pos = evt[0]  ## using signal proxy turns original arguments into a tuple
            if  self.plot1.sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                index = int(mousePoint.x())
                pos_y = int(mousePoint.y())
                print(index)
                if 0 <= index < len(self.datax):
                    print(self.datax[index], self.datay[index])
                    self.label.setHtml(
                        "<p style='color:white'>时间：{0}</p><p style='color:white'>温度：{1}</p>".format(
                            self.datax[index], self.datay[index]))
                    self.label.setPos(mousePoint.x(), mousePoint.y())
                vLine.setPos(mousePoint.x())
                hLine.setPos(mousePoint.y())

        self.proxy = pg.SignalProxy(self.plot1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
        print("okkkk")



    def fillinweathertype(self):
        self.setWindowTitle('天气类型')
        self.model = QStandardItemModel(33, 2,self)  # 1实例化一个QStandItemModel，可直接在实例化时传入行数和列数，或者也可以通过setRowCount()和setColumn()方法来设置。
        self.model.setHorizontalHeaderLabels(['API编号', '天气类型'])  # 设置水平方向头标签文本内容
        for row in range(33):  # 2 QStandItemModel与QStandardItem搭配使用,接着调用setItem()方法将每一个Item放在相应的位置
            item = QStandardItem(self.kind1['result'][row]['wid'])
            self.model.setItem(row, 0, item)
        for row in range(33):
            item = QStandardItem(self.kind1['result'][row]['weather'])
            self.model.setItem(row, 1, item)
        self.table = QTableView(self)  # 5
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)  # 水平方向标签拓展剩下的窗口部分，填满表格
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平方向，表格大小拓展到适当的尺寸
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #   self.table.clicked.connect(self.show_info)                             #  study 点击显示该单元格内容

        self.info_label = QLabel(self)  # 显示单元格文本
        self.info_label.setAlignment(Qt.AlignCenter)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)



    def fillincitytype(self):
        self.setWindowTitle('可查询的城市列表')
        self.model = QStandardItemModel(2587, 4,self)
        self.model.setHorizontalHeaderLabels(['ID', 'City','District','Province'])
        for row in range(2585):
                 item = QStandardItem(self.kind2['result'][row]['id'])
                 self.model.setItem(row, 0, item)
        for row in range(2585):
                 item = QStandardItem(self.kind2['result'][row]['city'])
                 self.model.setItem(row, 1, item)
        for row in range(2585):
                 item = QStandardItem(self.kind2['result'][row]['district'])
                 self.model.setItem(row, 2, item)
        for row in range(2585):
                 item = QStandardItem(self.kind2['result'][row]['province'])
                 self.model.setItem(row, 3, item)
        self.table = QTableView(self)  # 5
        self.table.setModel(self.model)
        self.table.horizontalHeader().setStretchLastSection(True)  # 水平方向标签拓展剩下的窗口部分，填满表格
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平方向，表格大小拓展到适当的尺寸
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.info_label = QLabel(self)  # 显示单元格文本
        self.info_label.setAlignment(Qt.AlignCenter)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

        """ def show_info(self):                                 #study点击显示单元格内容
                row = self.table.currentIndex().row()
                column = self.table.currentIndex().column()
                print('({}, {})'.format(row, column))
                data = self.table.currentIndex().data()
                self.info_label.setText(data)"""


