import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout,QDialog,QApplication
from PyQt5.QtGui import QFont
import numpy as np
from PyQt5.QtCore import Qt
import sys
class Graph(QDialog):
    def __init__(self,x,title,width,height,tickSize,lineWidth,ledgendSize,lw,bh,lineColor1,lineColor2):
        # x:数据图的序数，用来定位显示位置
        # title:数据图标题
        # width：数据图宽度
        # height：数据图高度
        # tickSize：图标尺尺寸
        # lineWidth：数据图线宽
        # ledgendSize：图例尺寸
        # lw：图示左坐标轴宽度
        # bh：图示下坐标轴高度
        # lineColor1：线颜色
        # lineColor2：线颜色
        super(Graph, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(title)
        self.setGeometry(x,0,width,height)
        self.vlayout=QVBoxLayout()
        self.setAttribute(Qt.WA_DeleteOnClose)
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')
        time = np.array([])
        y = np.array([])
        # r_symbol = np.random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        # r_color = np.random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
        #区域
        self.pw1=pg.PlotWidget(self,name="plot1")
        self.pw2=pg.PlotWidget(self,name="plot2")
        self.pw1.addLegend(size=(50,30),offset=(1,1)).setScale(ledgendSize)
        self.pw2.addLegend(size=(50,30),offset=(1,1)).setScale(ledgendSize)
        #画图
        self.pw1_data1=self.pw1.plot(time, y, pen=pg.mkPen(lineColor1,width=lineWidth),name="p1d1")
        self.pw1_data2=self.pw1.plot(time, y+10, pen=pg.mkPen(lineColor2,width=lineWidth),name="p1d2")
        self.pw2_data1=self.pw2.plot(time, y, pen=pg.mkPen(lineColor1,width=lineWidth),name="p2d1")
        self.pw2_data2=self.pw2.plot(time, y+10, pen=pg.mkPen(lineColor2,width=lineWidth),name="p2d2")
        #标线
        self.pw1.getPlotItem().showGrid(True, True)
        self.pw2.getPlotItem().showGrid(True, True)
        self.axisfont=QFont()
        self.axisfont.setPointSize(tickSize)
        # 设置X轴Tick
        # self.pw1.getPlotItem().getAxis("bottom").setLabel("time","s")
        # self.pw2.getPlotItem().getAxis("bottom").setLabel("time","s")
        self.pw1.getPlotItem().getAxis("bottom").setStyle(tickLength=15,tickFont=self.axisfont)
        self.pw2.getPlotItem().getAxis("bottom").setStyle(tickLength=15,tickFont=self.axisfont)
        self.pw2.getPlotItem().getAxis("left").linkedView().setAutoVisible()
        #设置y轴Tick
        # self.pw1.getPlotItem().getAxis("left").setLabel("vol", "v")
        self.pw1.getPlotItem().getAxis("left").setStyle(tickLength=15,tickFont=self.axisfont)
        self.pw2.getPlotItem().getAxis("left").setStyle(tickLength=15,tickFont=self.axisfont)
        #设置左轴tick宽度
        self.pw1.getPlotItem().getAxis("left").setWidth(lw)
        self.pw1.getPlotItem().getAxis("bottom").setHeight(bh)
        self.pw2.getPlotItem().getAxis("left").setWidth(lw)
        self.pw2.getPlotItem().getAxis("bottom").setHeight(bh)



        #设置title
        self.pw1.setTitle("<p style='font-size:{}px'>{}</p>".format(50,"shotnum"))

        #图例
        # self.legend1=pg.LegendItem((50,30),offset=(70,30))
        # self.legend2=pg.LegendItem((50,30),offset=(70,30))
        # #
        # self.legend1.setParentItem(self.pw1.graphicsItem())
        # self.legend1.addItem(self.pw1_data1,"p1d1")
        # self.legend1.addItem(self.pw1_data2,"p1d2")
        # self.legend2.setParentItem(self.pw2.graphicsItem())
        # self.legend2.addItem(self.pw2_data1,"p2d1")
        # self.legend2.addItem(self.pw1_data2,"p1d2")


        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        self.vlayout.addWidget(self.pw1)
        self.vlayout.addWidget(self.pw2)
        self.setLayout(self.vlayout)

if __name__=="__main__":
    app=QApplication(sys.argv)
    DSM=Graph(0, "ds", 700, 600,20,10,5,5,40,"r","b")
    DSM.show()
    sys.exit(app.exec_())