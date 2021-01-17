import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox,QMainWindow,QInputDialog,QLineEdit
from PyQt5.QtCore import QThread,pyqtSignal
from DSUI import Ui_DataShow
from DataGraph import Graph
import json
import numpy as np
import MDSplus
import socket
import pyqtgraph as pg
from setting import Setting
import pyttsx3
import datetime
class DSmain(QMainWindow,Ui_DataShow):
    def __init__(self):
        super(DSmain,self).__init__()
        self.setupUi(self)
        self.DSBtns=[self.DS1Button,self.DS2Button,self.DS3Button,self.DS4Button,self.DS5Button,
                     self.DS6Button,self.DS7Button,self.DS8Button,self.DS9Button,self.DS10Button]
        self.graph_cfg=Setting()
        self.graph_cfg.settingSignal.connect(self.get_graph_cfg)
        self.cfg = {}
        self.load_default_cfg_file()
        self.initAction()
        self.Sengine = SpeakerEngine("")
        self.sons={}
        self.udp=None
        self.statusbar.showMessage(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d"))


        # for b in self.DSBtns:
        #     b.setDisabled(True)
    # load the cfg file ,create a new empty one if no exist and use the default cfg
    def load_default_cfg_file(self):
        if  os.path.exists(os.path.join(os.getcwd(),"DS.json")):
            f=open(os.path.join(os.getcwd(),"DS.json"),"r")
            try:
                self.cfg = json.load(f)
            except json.decoder.JSONDecodeError as e:
                QMessageBox.warning(self, "Warning", "Get Error When Load Cfg File! Will Load Default Setting",
                                    QMessageBox.Yes)
                self.set_default_graph_cfg()
        else:
            f=open(os.path.join(os.getcwd(),"DS.json"),"w")
            QMessageBox.warning(self, "Warning", "No Setting File Is Found! Will Load Default Setting", QMessageBox.Yes)
            # if file is empty, set the deault cfg
            self.set_default_graph_cfg()
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
        self.LocalMode.setChecked(self.cfg.get("getDataMode","Fake") == "Local")
        self.RemoteMode.setChecked(self.cfg.get("getDataMode","Fake") == "Remote")
        self.FakeMode.setChecked(self.cfg.get("getDataMode","Fake") == "Fake")
        self.Speaker.setChecked(self.cfg.get("Speaker",0)!=0)
        self.Volume.setValue(self.cfg.get("Volume",0))
        self.SpeakNode.setText(self.cfg.get("SpeakNode", ""))
        f.close()

    # set the default cfg
    def set_default_graph_cfg(self):
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
    def get_graph_cfg(self, param):
        self.cfg.update(param)

    #初始化
    def initAction(self):
        # self.UDPButton.setDisabled(True)
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
        self.actionOpen.setShortcut("Ctrl+L")
        self.actionOpen.triggered.connect(self.load_cfg_file)
        self.actionExit.setShortcut("Ctrl+E")
        self.actionExit.triggered.connect(self.close)
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save_cfg_file)
        self.actionGraph.triggered.connect(self.set_graph_param)
        self.actionVersion.triggered.connect(lambda :self.about(self.actionVersion))
        self.actionAuthor.triggered.connect(lambda: self.about(self.actionAuthor))
        self.actionIP.triggered.connect(self.set_ip)
        self.actionPort.triggered.connect(self.set_port)
        self.actionTreeIP.triggered.connect(self.set_db_ip)
        self.actionTreeName.triggered.connect(self.set_db_name)
        self.actionTreeName.triggered.connect(self.set_db_name)
        self.LocalMode.clicked.connect(lambda :self.set_data_mode(self.LocalMode))
        self.RemoteMode.clicked.connect(lambda :self.set_data_mode(self.RemoteMode))
        self.FakeMode.clicked.connect(lambda :self.set_data_mode(self.FakeMode))
        self.Volume.sliderReleased.connect(lambda :self.Sengine.setVolume(self.Volume.value()))
        self.Volume.sliderReleased.connect(lambda :self.message_show("Volume changed to {}".format(str(self.Volume.value()/100))))
        self.QueryButton.clicked.connect(lambda: self.message_show("Query Data Of Shot:" + str(self.ShotNum.value())))
        self.QueryButton.clicked.connect(lambda:self.plot_slot(self.ShotNum.value()))
        self.Speaker.toggled.connect(self.set_speaker)
        self.actionHelp.triggered.connect(self.help)
    def help(self):
        text="""
            this software only for exl50 fusion experiment data show by muilt screem
        
        """
        self.message_show(text)
    def choose_better_source(self,res_net):
        if res_net!="0":
            self.FakeMode.setChecked(True)
            self.cfg["getDataMode"]="Fake"
            self.message_show("Database Network is bad,use fake source")
        else:
            self.message_show("Database Network is ok")
    def set_speaker(self):
        self.cfg["Speaker"]=int(self.Speaker.isChecked())
        self.message_show("Enable Speaker" if self.Speaker.isChecked() else "Disable Speaker")
    def check_network(self):
        self.message_show("Checking connection of database ")
        check=CheckNetwork(self.cfg["TreeIp"])
        check.res_net.connect(self.choose_better_source)
        check.start()
        check.exec()
    def message_show(self,message):
        time=datetime.datetime.strftime(datetime.datetime.now(),"%H:%M:%S")
        old=self.Message.toPlainText()+"\n"
        self.Message.setText(old+time+" "+str(message))
    def set_data_mode(self,button):
        self.cfg["getDataMode"]=button.text()
        self.message_show("set data source mode to {}".format(self.cfg["getDataMode"]))
        if self.cfg["getDataMode"]!="Fake":
            self.check_network()

    def set_ip(self):
        ip,ok=QInputDialog.getText(self,"IP:","xxx.xxx.20.xxx",text=self.cfg["udpIp"])
        if ok:
            self.cfg["udpIp"]=ip
    def set_port(self):
        port,ok=QInputDialog.getInt(self,"Port:","like 12301",value=self.cfg["udpPort"])
        if ok:
            self.cfg["udpPort"]=port

    def set_db_ip(self):
        ip, ok = QInputDialog.getText(self, "IP:", "xxx.xxx.20.xxx", text=self.cfg["TreeIp"])
        if ok:
            self.cfg["TreeIp"] = ip
            self.check_network()
    def set_db_name(self):
        name, ok = QInputDialog.getText(self, "Name:", "Tree Name", text=self.cfg["TreeName"])
        if ok:
            self.cfg["TreeName"] = name
    def about(self,about):
        if about.text()=="Author":
            texts="Author:控制组 刘勇"
        else:
            texts = "Version：1.1"
        QMessageBox.information(self, "about", texts, QMessageBox.Yes)
    def set_graph_param(self):
        self.graph_cfg.updateCfg(self.cfg)
        self.graph_cfg.show()
    def switchUdp(self):
        try:
            if not self.udp:
                self.udp = udpRecv(self.cfg["udpIp"], int(self.cfg["udpPort"]))
                self.udp.flashDataSignal.connect(self.plot_slot)
                self.udp.flashDataSignal.connect(self.message_show)
            if self.udp.is_on:
                self.udp.is_on=0
                self.UDPButton.setText("UDP OFF")
                self.udp.quit()
                self.UDPButton.setStyleSheet("background-color:{}".format("#f0f0f0"))
                self.message_show("udp is off now")

            else:
                self.udp.is_on=1
                self.udp.start()
                self.UDPButton.setText("UDP ON")
                self.UDPButton.setStyleSheet("background-color:{}".format("green"))
                self.message_show("udp is on now")
        except OSError as e:
            self.message_show(e)

    def displayData(self,btn):
        if not self.sons.get(btn.text(),None):
            i = int(btn.text()[2:])-1
            self.sons[btn.text()] = Graph(i * self.cfg["screenWidth"], "DS" + str(i + 1), self.cfg["screenWidth"],
                                          self.cfg["ScreenHeight"], self.cfg["TickSize"],
                                          self.cfg["LineWidth"], self.cfg["LegendSize"], self.cfg["XLeftWidth"],
                                          self.cfg["BottomHeight"],
                                          self.cfg["LineColor1"],
                                          self.cfg["LineColor2"]
                                          )
            self.sons[btn.text()].show()
            btn.setStyleSheet("background-color:green")
        else:

            self.sons[btn.text()].close()
            btn.setStyleSheet("background-color:{}".format("#f0f0f0"))
            self.sons.pop(btn.text())



    def close_func(self):
        for k,son in self.sons.items():
            son.close()
            self.DSBtns[int(k[2:])-1].setStyleSheet("background-color:#f0f0f0")
        self.sons.clear()
        self.message_show("close all ds graphs")


    def save_cfg_file(self,closeSave=0):
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
        self.cfg["SpeakNode"]=self.SpeakNode.text()
        self.cfg["Volume"] = self.Volume.value()
        self.cfg["Speaker"]=int(self.Speaker.isChecked())
        if closeSave:
            with open(os.path.join(os.getcwd(),"DS.json"),"w") as sf:
                json.dump(self.cfg,sf)
        else:
            saveJsonFile=QFileDialog.getSaveFileName(self,"save cfg file","./","json file(*.json)")

            if saveJsonFile[0]:
                with open(saveJsonFile[0],"w") as f:
                    json.dump(self.cfg,f)
                with open(os.path.join(os.getcwd(),"DS.json"),"w") as sf:
                    json.dump(self.cfg,sf)
                    self.message_show("save cfg file successfully")
    def load_cfg_file(self):
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
                self.LocalMode.setChecked(self.cfg["getDataMode"]=="Local")
                self.RemoteMode.setChecked(self.cfg["getDataMode"]=="Remote")
                self.FakeMode.setChecked(self.cfg["getDataMode"]=="Fake")
                self.Speaker.setChecked(self.cfg.get("Speaker", 0) != 0)
                self.Volume.setValue(self.cfg.get("Volume", 0))
                self.SpeakNode.setText(self.cfg.get("SpeakNode", ""))
            self.message_show("open cfg file successfully")


    def plot_slot(self,shot):
        data=self.getDataFromMds(shot,self.cfg["getDataMode"])
        for dsk,dsv in data.items():
            if self.sons.get(dsk,None):
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
            else:
                self.message_show("No {} graph to plot".format(dsk))

    def getDataFromMds(self,shot,mode="Local"):
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
        if mode == "Local":
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
        elif mode=="Remote":
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
        else:
            for k,v in temcfg.items():
                if "" not in v:
                    for node in v:
                        data.setdefault(k,{})[node]=[np.arange(-2,7,0.003),np.sin(np.arange(-2,7,0.003)+np.random.randn())]
            return data
    def closeEvent(self, *args, **kwargs):
        self.close_func()
        self.save_cfg_file(closeSave=1)
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
                self.flashDataSignal.emit(int(content[4:]))
    def closeUdp(self):
        self.udpserver.close()
class SpeakerEngine(QThread):
    def __init__(self,word):
        super(SpeakerEngine,self).__init__()
        self.engine=pyttsx3.init()
        self.word=word
    def run(self):
        self.engine.say(self.word)
        try:
            self.engine.runAndWait()
        except Exception as e:
            pass
    def setVolume(self,volume):
        print(volume)
        self.engine.setProperty("volume",volume/100)
class CheckNetwork(QThread):
    res_net=pyqtSignal(str)
    def __init__(self,ip):
        super(CheckNetwork,self).__init__()
        self.ip=ip
    def run(self):
        print("check")
        res=os.system("ping {}".format(self.ip))
        self.res_net.emit(str(res))

if __name__=="__main__":
    app=QApplication(sys.argv)
    DSM=DSmain()
    DSM.show()
    if DSM.cfg.get("TreeIp",None) and DSM.cfg.get("getDataMode","Fake")!="Fake":
        DSM.check_network()
    sys.exit(app.exec_())