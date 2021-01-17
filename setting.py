from PyQt5.QtWidgets import  QDialog, QApplication,QColorDialog
from PyQt5.QtCore import pyqtSignal
from SettingUI import Ui_Setting
import sys

class Setting(QDialog,Ui_Setting):
    settingSignal=pyqtSignal(dict)
    def __init__(self):
        super(Setting, self).__init__()
        self.setupUi(self)
        self.cfg_graph ={}
        self.LineColor1.clicked.connect(lambda:self.setColor(self.LineColor1))
        self.LineColor2.clicked.connect(lambda:self.setColor(self.LineColor2))
    def setColor(self,btn):
        self.color=QColorDialog.getColor()
        if self.color.isValid():
            self.cfg_graph[btn.objectName()]=self.color.name()
            btn.setStyleSheet("background-color:{}".format(self.color.name()))
        print(self.cfg_graph)

    def closeEvent(self, QCloseEvent):
        self.cfg_graph["sampleStart"]=self.Start.value()
        self.cfg_graph["sampleEnd"]=self.End.value()
        self.cfg_graph["sampleStep"]=self.Step.value()
        self.cfg_graph["screenWidth"]=self.ScreenWidth.value()
        self.cfg_graph["ScreenHeight"]=self.ScreenHeight.value()
        self.cfg_graph["TickSize"]=self.TickSize.value()
        self.cfg_graph["XLeftWidth"]=self.XleftWidth.value()
        self.cfg_graph["BottomHeight"]=self.BottomHeight.value()
        self.cfg_graph["TitleSize"]=self.TitleSize.value()
        self.cfg_graph["LegendSize"]=self.LegendSize.value()
        self.cfg_graph["LineWidth"]=self.LineWidth.value()
        self.settingSignal.emit(self.cfg_graph)
    def updateCfg(self,newCfg):
        self.cfg_graph=newCfg
        self.Start.setValue(self.cfg_graph.get("sampleStart", -5))
        self.End.setValue(self.cfg_graph.get("sampleEnd", 10))
        self.Step.setValue(self.cfg_graph.get("sampleStep", 0.001))
        self.ScreenWidth.setValue(self.cfg_graph.get("screenWidth", 1920))
        self.ScreenHeight.setValue(self.cfg_graph.get("ScreenHeight", 1080))
        self.TickSize.setValue(self.cfg_graph.get("TickSize", 40))
        self.XleftWidth.setValue(self.cfg_graph.get("XLeftWidth", 100))
        self.BottomHeight.setValue(self.cfg_graph.get("BottomHeight", 40))
        self.TitleSize.setValue(self.cfg_graph.get("TitleSize", 40))
        self.LegendSize.setValue(self.cfg_graph.get("LegendSize", 2))
        self.LineWidth.setValue(self.cfg_graph.get("LineWidth", 5))
        self.LineColor1.setStyleSheet("background-color:{}".format(self.cfg_graph.get("LineColor1", "r")))
        self.LineColor2.setStyleSheet("background-color:{}".format(self.cfg_graph.get("LineColor2", "b")))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    DSM = Setting()
    DSM.show()
    sys.exit(app.exec_())