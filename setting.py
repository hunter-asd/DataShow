from PyQt5.QtWidgets import  QDialog, QApplication,QColorDialog
from PyQt5.QtCore import pyqtSignal
from SettingUI import Ui_Setting
import sys

class Setting(QDialog,Ui_Setting):
    settingSignal=pyqtSignal(dict)
    def __init__(self):
        super(Setting, self).__init__()
        self.setupUi(self)
        self.cfg ={}
        self.LineColor1.clicked.connect(lambda:self.setColor(self.LineColor1))
        self.LineColor2.clicked.connect(lambda:self.setColor(self.LineColor2))
    def setColor(self,btn):
        self.color=QColorDialog.getColor()
        if self.color.isValid():
            self.cfg[btn.objectName()]=self.color.name()
            btn.setStyleSheet("background-color:{}".format(self.color.name()))

    def closeEvent(self, QCloseEvent):
        self.cfg["sampleStart"]=self.Start.value()
        self.cfg["sampleEnd"]=self.End.value()
        self.cfg["sampleStep"]=self.Step.value()
        self.cfg["udpIp"]=self.UdpIP.text()
        self.cfg["udpPort"]=self.UdpPort.value()
        self.cfg["screenWidth"]=self.ScreenWidth.value()
        self.cfg["ScreenHeight"]=self.ScreenHeight.value()
        self.cfg["TickSize"]=self.TickSize.value()
        self.cfg["XLeftWidth"]=self.XleftWidth.value()
        self.cfg["BottomHeight"]=self.BottomHeight.value()
        self.cfg["TitleSize"]=self.TitleSize.value()
        self.cfg["LegendSize"]=self.LegendSize.value()
        self.cfg["LineWidth"]=self.LineWidth.value()
        self.settingSignal.emit(self.cfg)
    def updateCfg(self,newCfg):
        self.cfg=newCfg
        self.Start.setValue(self.cfg.get("sampleStart", -5))
        self.End.setValue(self.cfg.get("sampleEnd", 10))
        self.Step.setValue(self.cfg.get("sampleStep", 0.001))
        self.UdpIP.setText(self.cfg.get("udpIp", "192.168.20.199"))
        self.UdpPort.setValue(self.cfg.get("udpPort", 12301))
        self.ScreenWidth.setValue(self.cfg.get("screenWidth", 1920))
        self.ScreenHeight.setValue(self.cfg.get("ScreenHeight", 1080))
        self.TickSize.setValue(self.cfg.get("TickSize", 40))
        self.XleftWidth.setValue(self.cfg.get("XLeftWidth", 100))
        self.BottomHeight.setValue(self.cfg.get("BottomHeight", 40))
        self.TitleSize.setValue(self.cfg.get("TitleSize", 40))
        self.LegendSize.setValue(self.cfg.get("LegendSize", 2))
        self.LineWidth.setValue(self.cfg.get("LineWidth", 5))
        self.LineColor1.setStyleSheet("background-color:{}".format(self.cfg.get("LineColor1", "r")))
        self.LineColor2.setStyleSheet("background-color:{}".format(self.cfg.get("LineColor2", "b")))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    DSM = Setting()
    DSM.show()
    sys.exit(app.exec_())