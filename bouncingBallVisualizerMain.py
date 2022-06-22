# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\bouncingBallVisualizer\\bouncingBallVisualizer"))
sys.path.append(os.path.abspath("C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\bouncingBallVisualizer\\bouncingBallVisualizer\\bouncingBallVisualizerExtra"))
#maya imports
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
#ui imports
from PySide2 import QtCore,QtWidgets,QtGui

#bouncingBall imports
import bouncingBallVisualizerExtra.bouncingBall
reload(bouncingBallVisualizerExtra.bouncingBall)
from bouncingBallVisualizerExtra.bouncingBall import BouncingBall, Error, Warning
from bouncingBallVisualizerExtra.ui.mainDialogUi import Ui_BBDialog

from shiboken2 import wrapInstance

"Get Maya's main window"
def mayaMainWindow():
    mainWindow = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mainWindow), QtWidgets.QWidget)

#Error class definition

class bouncingBallVisDialog(QtWidgets.QDialog):
    dlg_instance = None

    @classmethod
    def run(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = bouncingBallVisDialog()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    def __init__(self,parent = mayaMainWindow()):
        super(bouncingBallVisDialog,self).__init__(parent)

        self.bouncingBall = BouncingBall()
        self.ui = Ui_BBDialog(self)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.createConnections()
        self.sJob = cmds.scriptJob(event=['SelectionChanged', self.selectionChanged])
        self.checkScriptJob()

    def createConnections(self):
       self.ui.createButton.clicked.connect(self.createBouncingBall)
       self.ui.ballVisibilityButton.clicked.connect(self.toggleBallVisibility)
       self.ui.controllerVisibilityButton.clicked.connect(self.toggleControllerVisibility)
       self.ui.controllerAllOnButton.clicked.connect(self.AllObjectsVisibility)
       self.ui.controllerAllOffButton.clicked.connect(self.AllObjectsVisibility)
       self.ui.ballAllOnButton.clicked.connect(self.AllObjectsVisibility)
       self.ui.ballAllOffButton.clicked.connect(self.AllObjectsVisibility)
       self.ui.isolateViewButton.clicked.connect(self.isolateViewOnControllers)
       self.ui.deleteSelectedButton.clicked.connect(self.deleteBouncingBalls)
       self.ui.deleteAllButton.clicked.connect(self.deleteBouncingBalls)
       self.ui.radiusSlider.valueChanged.connect(self.updateRadius)
       self.ui.radiusSpinBox.valueChanged.connect(self.updateRadius)
       self.ui.radiusSlider.sliderReleased.connect(self.changeRadius)
       self.ui.radiusSpinBox.editingFinished.connect(self.changeRadius)
    def createBouncingBall(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        try:    
            self.bouncingBall.create()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def checkScriptJob(self):
        controllers = cmds.ls(sl = 1, tr=1)
        exists = False
        if self.sJob:
            exists = cmds.scriptJob(ex= int(self.sJob))
        if not exists:
            self.sJob = cmds.scriptJob(event=['SelectionChanged', self.selectionChanged])
        cmds.select(controllers)

    def toggleBallVisibility(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        try:
            self.bouncingBall.toggleBallVisibility()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def toggleControllerVisibility(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        try:
            self.bouncingBall.toggleControllerVisibility(deleting = False)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def AllObjectsVisibility(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        sender = self.sender()
        try:
            if sender == self.ui.controllerAllOffButton:
                self.bouncingBall.AllObjectsVisibility(False,"nurbsCurve")
            if sender == self.ui.controllerAllOnButton:
                self.bouncingBall.AllObjectsVisibility(True,"nurbsCurve")
            if sender == self.ui.ballAllOffButton:
                self.bouncingBall.AllObjectsVisibility(False,"mesh")
            if sender == self.ui.ballAllOnButton:
                self.bouncingBall.AllObjectsVisibility(True,"mesh")
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)
    def isolateViewOnControllers(self):
        self.checkScriptJob()
        try:
            self.bouncingBall.isolateViewOnControllers()
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
    def deleteBouncingBalls(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        sender = self.sender()
        try:
            if sender == self.ui.deleteAllButton:
                self.bouncingBall.deleteBalls(all = True)
            if sender == self.ui.deleteSelectedButton:
                self.bouncingBall.deleteBalls(all = False)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def selectionChanged(self):
        selected = cmds.ls(sl=1,tr=1)
        if self.bouncingBall.check(selected):
           self.ui.radiusFrame.setVisible(True)
        else:
           self.ui.radiusFrame.setVisible(False)

    def updateRadius(self):
        self.checkScriptJob()
        try:
            sender = self.sender()
            
            if sender == self.ui.radiusSlider:
                radius = float(self.ui.radiusSlider.value())/100
                self.ui.radiusSpinBox.setValue(radius)
            else:
                radius = int(float(self.ui.radiusSpinBox.value())*100)
                self.ui.radiusSlider.setValue(radius)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def changeRadius(self):
        cmds.undoInfo(ock=1)
        self.checkScriptJob()
        try:
            radius = float(self.ui.radiusSlider.value())/100
            self.bouncingBall.changeRadius(radius)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
    
    def closeEvent(self,event):
        cmds.scriptJob(k=self.sJob)
        event.accept()
        

if __name__ == "__main__":
    pass

""" def showTestWindow():
    global win
    try:
        win.close()
    except: pass
    win = bouncingBallVisDialog()
    win.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    win.show()

showTestWindow() """