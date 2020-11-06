import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox,QMainWindow,QInputDialog,QLineEdit
from PyQt5.QtCore import QThread,pyqtSignal
from DSmain import Ui_DataShow
from DataGraph import Graph
import json
import numpy as np
import MDSplus
import socket
import pyqtgraph as pg
from setting import Setting
class DSmain(QMainWindow,Ui_DataShow):
    def __init__(self):
        super(DSmain,self).__init__()
        self.setupUi(self)
        self.DSBtns=[self.DS1Button,self.DS2Button,self.DS3Button,self.DS4Button,self.DS5Button,
                     self.DS6Button,self.DS7Button,self.DS8Button,self.DS9Button,self.DS10Button]
        self.settingWidget=Setting()
        self.settingWidget.settingSignal.connect(self.getcfg)
        self.initAction()
        self.sons={}
        self.cfg = {}
        # if self.load_default_cfg()==0:
        self.set_default_cfg()
    def load_default_cfg(self):
        if os.path.exists(os.path.join(os.getcwd(),"DSsetting.json")):
            with open(r"C:\DSsetting.json") as f:
                self.cfg=json.load(f)
                self.DS1Node.setText(self.cfg.get("DS1", ""))
                self.DS2Node.setText(self.cfg.get("DS2", ""))
                self.DS3Node.setText(self.cfg.get("DS3", ""))
                self.DS4Node.setText(self.cfg.get("DS4", ""))
                self.DS5Node.setText(self.cfg.get("DS5", ""))
                self.DS6Node.setText(self.cfg.get("DS6", ""))
                self.DS7Node.setText(self.cfg.get("DS7", ""))
                self.DS8Node.setText(self.cfg.get("DS8", ""))
                self.DS9Node.setText(self.cfg.get("DS9", ""))
                self.DS10Node.setText(self.cfg.get("DS10", ""))
                self.LocalMode.setChecked(self.cfg["getDataMode"] == "local")
                self.RemoteMode.setChecked(self.cfg["getDataMode"] == "remote")
            return 1
        else:
            print(0)
            return 0
    def set_default_cfg(self):
        self.cfg["sampleStart"] = -5
        self.cfg["sampleEnd"] = 10
        self.cfg["sampleStep"] = 0.001
        self.cfg["udpIp"] = "192.168.20.199"
        self.cfg["udpPort"] = 12301
        self.cfg["screenWidth"] = 1920
        self.cfg["ScreenHeight"] = 1080
        self.cfg["TickSize"] = 20
        self.cfg["XLeftWidth"] = 100
        self.cfg["BottomHeight"] = 40
        self.cfg["TitleSize"] = 40
        self.cfg["LegendSize"] = 5
        self.cfg["LineWidth"] = 5
        self.cfg["LineColor1"] = "#FF0000"
        self.cfg["LineColor2"] = "#0000FF"
        self.cfg["TreeName"] = "EXL50"
        self.cfg["TreeIp"] = "192.168.20.11"
        self.cfg["getDataMode"] = "local"
    def getcfg(self,param):
        self.cfg=param
    def run_func(self,btn):
        if btn.text()=="Stop":
            self.udp.is_on=0
            self.udp.closeUdp()
            self.udp.quit()
            btn.setStyleSheet("background-color:green")
            self.sons={}
            for dsb in self.DSBtns:
                dsb.setDisabled(True)
                dsb.setStyleSheet("background-color:red")
            self.UDPButton.setDisabled(True)
            btn.setText("Run")
        else:

            try:
                self.udp = udpRecv(self.cfg["udpIp"], int(self.cfg["udpPort"]))
                self.udp.flashDataSignal.connect(self.plot_slot)
                for i in range(10):
                    self.son=Graph(i*self.cfg["screenWidth"],"DS"+str(i+1),self.cfg["screenWidth"],self.cfg["ScreenHeight"],self.cfg["TickSize"],
                                   self.cfg["LineWidth"],self.cfg["LegendSize"],self.cfg["XLeftWidth"],self.cfg["BottomHeight"],
                                   self.cfg["LineColor1"],
                                   self.cfg["LineColor2"]
                                  )
                    self.sons["DS"+str(i+1)]=self.son
                for dsb in self.DSBtns:
                    dsb.setEnabled(True)
                    dsb.setStyleSheet("background-color:gray")
                self.UDPButton.setEnabled(True)
                btn.setText("Stop")
                btn.setStyleSheet("background-color:red")
            except Exception as e:
                QMessageBox.warning(self, "Error","Error occor when to run: {}".format(e),QMessageBox.Yes)
    def initAction(self):
        for dsb in self.DSBtns:
            dsb.setDisabled(True)
        # self.RunButton.setDisabled(True)
        self.UDPButton.setDisabled(True)
        self.DS1Button.clicked.connect(lambda: self.displayData(self.DS1Button))
        self.DS2Button.clicked.connect(lambda: self.displayData(self.DS2Button))
        self.DS3Button.clicked.connect(lambda: self.displayData(self.DS3Button))
        self.DS4Button.clicked.connect(lambda: self.displayData(self.DS4Button))
        self.DS5Button.clicked.connect(lambda: self.displayData(self.DS5Button))
        self.DS6Button.clicked.connect(lambda: self.displayData(self.DS6Button))
        self.DS7Button.clicked.connect(lambda: self.displayData(self.DS7Button))
        self.DS8Button.clicked.connect(lambda: self.displayData(self.DS8Button))
        self.DS9Button.clicked.connect(lambda: self.displayData(self.DS9Button))
        self.DS10Button.clicked.connect(lambda: self.displayData(self.DS10Button))
        self.CloseButton.clicked.connect(self.close_func)
        self.UDPButton.clicked.connect(self.switchUdp)
        self.RunButton.clicked.connect(lambda: self.run_func(self.RunButton))
        self.actionopen_Cfg.setShortcut("Ctrl+L")
        self.actionopen_Cfg.triggered.connect(self.loadCfg_func)
        self.actionSave_Cfg.setShortcut("Ctrl+S")
        self.actionSave_Cfg.triggered.connect(self.saveCfg_func)
        self.actionParam.triggered.connect(self.setParam)
        self.actionabout.triggered.connect(self.about)
        self.LocalMode.toggled.connect(lambda: self.getDataMode(self.LocalMode))
    def getDataMode(self,btn):
        if btn.isChecked():
            self.cfg["getDataMode"]="local"
        else:
            self.cfg["getDataMode"] = "remote"

    def about(self):
        QMessageBox.information(self, "about", "Version：1.0  Author：hunter ", QMessageBox.Yes)
    def setParam(self):
        self.settingWidget.updateCfg(self.cfg)
        self.settingWidget.show()
    def switchUdp(self):
        if self.udp.is_on:
            self.udp.is_on=0
            self.UDPButton.setText("UDP OFF")
            self.RunButton.setEnabled(True)
        else:
            self.udp.is_on=1
            self.udp.start()
            self.UDPButton.setText("UDP ON")
            self.RunButton.setDisabled(True)
    def displayData(self,btn):
        if self.sons[btn.text()].isVisible():
            self.sons[btn.text()].close()
            btn.setStyleSheet("background-color:red")
        else:
            self.sons[btn.text()].show()
            btn.setStyleSheet("background-color:green")
    def close_func(self):
        for son in self.sons.values():
            if son.isVisible():
                son.close()
        for dsb in self.DSBtns:
            if dsb.palette().button().color().name() =="#008000":
                dsb.setStyleSheet("background-color:red")
    def saveCfg_func(self):
        self.cfg["DS1"]=self.DS1Node.text()
        self.cfg["DS2"]=self.DS2Node.text()
        self.cfg["DS3"]=self.DS3Node.text()
        self.cfg["DS4"]=self.DS4Node.text()
        self.cfg["DS5"]=self.DS5Node.text()
        self.cfg["DS6"]=self.DS6Node.text()
        self.cfg["DS7"]=self.DS7Node.text()
        self.cfg["DS8"]=self.DS8Node.text()
        self.cfg["DS9"]=self.DS9Node.text()
        self.cfg["DS10"]=self.DS10Node.text()
        saveJsonFile=QFileDialog.getSaveFileName(self,"save cfg file","./","json file(*.json)")
        if saveJsonFile[0]:
            with open(saveJsonFile[0],"w") as f:
                json.dump(self.cfg,f)
            with open(os.path.join(os.getcwd(),"DSsetting.json"),"w") as sf:
                json.dump(self.cfg,sf)
            QMessageBox.information(self, "tip", "save successfully！", QMessageBox.Yes)
    def loadCfg_func(self):
        loadJsonFile = QFileDialog.getOpenFileName(self, "load cfg file", "./", "json file(*.json)")
        if loadJsonFile[0]:
            with open(loadJsonFile[0],"r") as f:
                self.cfg=json.load(f)
                self.DS1Node.setText(self.cfg.get("DS1",""))
                self.DS2Node.setText(self.cfg.get("DS2",""))
                self.DS3Node.setText(self.cfg.get("DS3",""))
                self.DS4Node.setText(self.cfg.get("DS4",""))
                self.DS5Node.setText(self.cfg.get("DS5",""))
                self.DS6Node.setText(self.cfg.get("DS6",""))
                self.DS7Node.setText(self.cfg.get("DS7",""))
                self.DS8Node.setText(self.cfg.get("DS8",""))
                self.DS9Node.setText(self.cfg.get("DS9",""))
                self.DS10Node.setText(self.cfg.get("DS10",""))
                self.LocalMode.setChecked(self.cfg["getDataMode"]=="local")
                self.RemoteMode.setChecked(self.cfg["getDataMode"]=="remote")
            self.RunButton.setEnabled(True)
            QMessageBox.information(self, "tip", "load successfully！", QMessageBox.Yes)


    def plot_slot(self,shot):
        data=self.getDataFromMds(shot,self.cfg["getDataMode"])
        for dsk,dsv in data.items():
            self.sons[dsk].pw1.setTitle("<p style='font-size:{}px'>{}</p>".format(self.cfg["TitleSize"],shot))
            if len(dsv)>2:
                for (nodek,nodev),nodenum in zip(dsv.items(),range(len(dsv))):
                    if len(nodev[1])>0 and nodev[1].max()>1000:
                        nodev[1]=nodev[1]/1000
                        nodek=nodek+"(K)"
                    if nodenum==0:
                        self.sons[dsk].pw1.getPlotItem().addLegend().clear()
                        self.sons[dsk].pw1.getPlotItem().addLegend().addItem(self.sons[dsk].pw1_data1,nodek)
                        self.sons[dsk].pw1_data1.setData(nodev[0],nodev[1],name=nodek,pen=pg.mkPen(self.cfg["LineColor1"],width=self.cfg["LineWidth"]))
                    elif nodenum==1:
                        self.sons[dsk].pw1.getPlotItem().addLegend().addItem(self.sons[dsk].pw1_data2, nodek)
                        self.sons[dsk].pw1_data2.setData(nodev[0],nodev[1],name=nodek,pen=pg.mkPen(self.cfg["LineColor2"],width=self.cfg["LineWidth"]))
                    elif nodenum==2:
                        self.sons[dsk].pw2.getPlotItem().addLegend().clear()
                        self.sons[dsk].pw2.getPlotItem().addLegend().addItem(self.sons[dsk].pw2_data1, nodek)
                        self.sons[dsk].pw2_data1.setData(nodev[0],nodev[1],name=nodek,pen=pg.mkPen(self.cfg["LineColor1"],width=self.cfg["LineWidth"]))
                    else:
                        self.sons[dsk].pw2.getPlotItem().addLegend().addItem(self.sons[dsk].pw2_data2, nodek)
                        self.sons[dsk].pw2_data2.setData(nodev[0],nodev[1],name=nodek,pen=pg.mkPen(self.cfg["LineColor2"],width=self.cfg["LineWidth"]))
            else:
                for (nodek, nodev), nodenum in zip(dsv.items(), range(len(dsv))):
                    if len(nodev[1])>0 and nodev[1].max()>1000:
                        nodev[1]=nodev[1]/1000
                        nodek=nodek+"(K)"
                    if nodenum == 0:
                        self.sons[dsk].pw1.getPlotItem().addLegend().clear()
                        self.sons[dsk].pw1.getPlotItem().addLegend().addItem(self.sons[dsk].pw1_data1, nodek)
                        self.sons[dsk].pw1_data1.setData(nodev[0],nodev[1], name=nodek,pen=pg.mkPen(self.cfg["LineColor1"],width=self.cfg["LineWidth"]))
                    else:
                        self.sons[dsk].pw2.getPlotItem().addLegend().clear()
                        self.sons[dsk].pw2.getPlotItem().addLegend().addItem(self.sons[dsk].pw2_data1, nodek)
                        self.sons[dsk].pw2_data1.setData(nodev[0],nodev[1], name=nodek,pen=pg.mkPen(self.cfg["LineColor2"],width=self.cfg["LineWidth"]))
    def getDataFromMds(self,shot,mode="local"):
        data={}
        temcfg={}
        temcfg["DS1"]=self.DS1Node.text().split(",")
        temcfg["DS2"]=self.DS2Node.text().split(",")
        temcfg["DS3"]=self.DS3Node.text().split(",")
        temcfg["DS4"]=self.DS4Node.text().split(",")
        temcfg["DS5"]=self.DS5Node.text().split(",")
        temcfg["DS6"]=self.DS6Node.text().split(",")
        temcfg["DS7"]=self.DS7Node.text().split(",")
        temcfg["DS8"]=self.DS8Node.text().split(",")
        temcfg["DS9"]=self.DS9Node.text().split(",")
        temcfg["DS10"]=self.DS10Node.text().split(",")
        if mode == "local":
            print("local")
            tree=MDSplus.Tree(self.cfg["TreeName"],shot,path="192.168.20.11::media/ennfusion/trees/exl50")
            tree.setTimeContext(self.cfg["sampleStart"],self.cfg["sampleEnd"],self.cfg["sampleStep"])
            for k,v in temcfg.items():
                if "" not in v:
                    for node in v:
                        n=tree.getNode("\\"+node)
                        try:
                            data.setdefault(k,{})[node]=[n.dim_of().data(),n.data()]
                        except MDSplus.mdsExceptions.TreeNODATA:
                            data.setdefault(k,{})[node]=[np.array([]),np.array([])]
                        except Exception as e:
                            QMessageBox.warning(self,"warning","Error occor when to get data from node: {},error: {}".format(node,e),QMessageBox.Yes)
            tree.close()
            return data
        else:
            print("remote")
            con=MDSplus.Connection(self.cfg["TreeIp"])
            con.openTree(self.cfg["TreeName"],shot)
            con.get("SetTimeContext({},{},{})".format(self.cfg["sampleStart"],self.cfg["sampleEnd"],self.cfg["sampleStep"]))
            for k,v in temcfg.items():
                if "" not in v:
                    for node in v:
                        try:
                            data.setdefault(k,{})[node]=[con.get("dim_of(\\{})".format(node)).data(),con.get("value_of(\\{})".format(node)).data()]
                        except MDSplus.mdsExceptions.TreeNODATA:
                            data.setdefault(k,{})[node]=[np.array([]),np.array([])]
                        except Exception as e:
                            QMessageBox.warning(self,"warning","Error occor when to get data from node: {},error: {}".format(node,e),QMessageBox.Yes)
            con.closeTree(self.cfg["TreeName"],shot)
            con.disconnect()
            return data
    def closeEvent(self, *args, **kwargs):
        self.close_func()
class udpRecv(QThread):
    flashDataSignal=pyqtSignal(int)
    def __init__(self,host,port):
        super(udpRecv,self).__init__()
        self.is_on=0
        self.udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpserver.bind((host,port))
    def run(self):
        while self.is_on:
            self.msleep(100)
            data, addr = self.udpserver.recvfrom(1024)
            content = data.decode("utf-8")
            if content.startswith("+DS_"):
                print(content)
                self.flashDataSignal.emit(int(content[4:]))
    def closeUdp(self):
        self.udpserver.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    DSM=DSmain()
    DSM.show()
    sys.exit(app.exec_())