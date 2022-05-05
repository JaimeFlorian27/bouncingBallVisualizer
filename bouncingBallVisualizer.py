import sys
import os
sys.path.append(os.path.abspath("C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\bouncingBallVisualizer"))
#maya imports
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui

#ui imports
from PySide2 import QtCore,QtWidgets,QtGui
from bouncingBallVisualizer.ui.mainDialogUi import Ui_BBDialog

from shiboken2 import wrapInstance
def mayaMainWindow():
    mainWindow = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mainWindow), QtWidgets.QWidget)

class bouncingBallVisDialog(QtWidgets.QDialog):
    def __init__(self,parent = mayaMainWindow()):
        super(bouncingBallVisDialog,self).__init__(parent)

        self.ui = Ui_BBDialog(self)
        
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

dialog = bouncingBallVisDialog()
dialog.show()




#*****************************************************************************************************************************************
class BouncingBall:
    def __init__(self):
        pass

    def create(self):
    #Get selected controller
        controller = cmds.ls(sl = 1)

        #Create sphere

        sphere = cmds.polySphere(ch=1)

        #Parent shape node (deleting old transform node)

        sphere_shape = cmds.listRelatives(s=1, pa=1)
        cmds.parent(sphere_shape,controller, r=1, s=1)
        cmds.sl(sphere)

        # doDelete checks for references and skin clusters before running delete, meaning that it wont break connections
        mel.eval("doDelete")

    def check(self):
        '''checks if controller contains a bouncing ball '''
        object = cmds.ls(sl=1)
        shapes = cmds.listRelatives(object,s=1)
        if shapes:
            #if any of the shape nodes is a mesh
            if any("mesh" in cmds.ls(s=1,showType=1) for s in shapes):
                #if any of those meshes is a sphere
                if any("Sphere" in s for s in shapes):
                    return True
        return False
