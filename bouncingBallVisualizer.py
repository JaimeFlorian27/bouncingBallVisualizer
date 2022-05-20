import sys
import os
sys.path.append(os.path.abspath("C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\bouncingBallVisualizer"))
#maya imports
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
#ui imports
from PySide2 import QtCore,QtWidgets,QtGui
from bouncingBallVisualizer.ui.mainDialogUi import Ui_BBDialog

from shiboken2 import wrapInstance

"Get Maya's main window"
def mayaMainWindow():
    mainWindow = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mainWindow), QtWidgets.QWidget)

#Error class definition
class Error(Exception):
    pass
#Warning class definition
class Warning(Exception): 
    pass

class BouncingBall:
    def __init__(self):
        self.controllers = []
        self.bouncingBallVisualizerNode = ""
        self.checkNode()

    def create(self):
        self.checkNode()
        #Get selected controller
        controllers = cmds.ls(sl = 1, tr=1)
        if len(controllers) <1:
            raise Error("No controllers selected")
        notAdded = []
        for controller in controllers:
            if self.check(controller):
                notAdded.append(controller)
                continue
            controllerUuid = cmds.ls(controller, uuid=1)
            attrName = "uuid_"+controller.replace(":","")
            self.addControllerToList(attrName,controllerUuid)
            #Create sphere
            sphere = cmds.polySphere(ch=1)
            #Parent shape node
            sphere_shape = cmds.listRelatives(s=1, pa=1)
            cmds.parent(sphere_shape,controller,r=1, s=1)
            #save sphere's shape new long name 
            sphere_shape = cmds.ls(sl=1, l=1)

            pivot = cmds.xform(controller, piv=True , q=True , ws=True)
            vtxs = cmds.ls("%s.vtx[*]"%sphere_shape[0], fl=True)
            for vtx in vtxs:
                cmds.move(pivot[0],pivot[1],pivot[2], vtx,a=1, ws=1)

            #set checker texture 
            cmds.sets( e=True, forceElement= 'bouncingBallSG' )
            #Selectes adn deletes old transform node
            sphere = cmds.ls (sphere, tr=1)
            cmds.delete(sphere)
            #selects sphere's shape
            self.controllers.append(controller)
        cmds.select(controllers)
        if notAdded:
            om.MGlobal.displayWarning("Skipped : %s , Object(s) already had a bouncing ball." %(",".join(notAdded)) )

    def check(self, object):
        '''checks if controller contains a bouncing ball '''
        shapes = cmds.listRelatives(object,s=1)
        if shapes:
            #if any of the shape nodes is a mesh
            if any("mesh" in cmds.ls(s=1,showType=1) for s in shapes):
                #if any of those meshes is a sphere
                if any("Sphere" in s for s in shapes):
                    return True
    
    def toggleBallVisibility(self):
        self.checkNode()
        controllers = cmds.ls(sl = 1, tr=1)
        noBall = []
        if len(controllers) <1:
            raise Error("No controllers selected")
        for controller in controllers:
            if not self.check(controller):
                noBall.append(controller)
                continue
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            for shape in shapes:
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                if  shapeType[1] =="mesh":
                    vis = cmds.getAttr("%s.visibility" %(shape))
                    cmds.setAttr("%s.visibility" %(shape), not vis)
        cmds.select(controllers)
        if noBall:
            om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a bouncing ball." %(",".join(noBall)) )

    def toggleControllerVisibility(self, deleting):
        self.checkNode()
        controllers = []
        if deleting:
            controllers = self.controllersFromUuid()
        else:    
            controllers = cmds.ls(sl = 1, tr=1)
        if len(controllers) <1:
            raise Error("No controllers selected")
        noBall = []
        for controller in controllers:
            if not self.check(controller):
                noBall.append(controller)
                continue
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            for shape in shapes:
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                if  shapeType[1] =="nurbsCurve":
                    if deleting:
                        cmds.setAttr("%s.visibility" %(shape), 1)
                    else:
                        vis = cmds.getAttr("%s.visibility" %(shape))
                        cmds.setAttr("%s.visibility" %(shape), not vis)

        cmds.select(controllers)
        if noBall:
                om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a nurbsCurve controller." %(",".join(noBall)) )            
    
    def AllObjectsVisibility(self,vis,type):
        self.checkNode()
        previousSelected= cmds.ls(sl=1)
        controllers = self.controllersFromUuid()
        if len(controllers) <1:
            raise Error("No controllers selected")
        for controller in controllers:
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            for shape in shapes:
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                if  shapeType[1] ==type:
                    cmds.setAttr("%s.visibility" %shape, vis)
        cmds.select(previousSelected)
    
    def isolateViewOnControllers(self):
        self.checkNode()
        previousSelected = cmds.ls(sl=1)
        currentPanel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        cmds.select(clear=1)
        try:
            controllers = self.controllersFromUuid()
        except Error as e:
            cmds.isolateSelect( currentPanel, s=False)
            om.MGlobal.displayWarning("No bouncing balls on scene")
            return
        cmds.select(controllers)
        state = cmds.isolateSelect( currentPanel,q=1, s=1)
        cmds.isolateSelect( currentPanel, s=not state)
        cmds.isolateSelect( currentPanel, addSelected=True)
        cmds.select(previousSelected)

    def deleteBalls(self, all):
        self.checkNode()
        controllers = []
        if all:
            controllers = self.controllersFromUuid()
        else:
            controllers = cmds.ls(sl = 1, tr=1)
        if len(controllers) <1:
            raise Error("No controllers with bouncing balls on the scene")
        noBall = []
        self.toggleControllerVisibility(deleting = True)
        for controller in controllers:
            if not self.check(controller):
                noBall.append(controller)
                continue
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            for shape in shapes:
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                if  shapeType[1] =="mesh":
                    attrName = "uuid_"+ controller.replace(":","")
                    cmds.deleteAttr("bouncingBallVisualizer.%s" %attrName)
                    cmds.delete(shape)
        cmds.select(controllers)
        if noBall:
            om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a bouncing ball." %(",".join(noBall)) )

    def changeRadius(self,value):
        self.checkNode()
        controllers = cmds.ls(sl = 1, tr=1)
        if len(controllers) <1:
            raise Error("No controllers selected")
        noBall = []
        for controller in controllers:
            if not self.check(controller):
                noBall.append(controller)
                continue
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            for shape in shapes:
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                if  shapeType[1] =="mesh":
                    editable_shape = cmds.listConnections(shape)[1]
                    cmds.setAttr("%s.radius" %(editable_shape), value)
        cmds.select(controllers)
        if noBall:
                om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a bouncing ball controller." %(",".join(noBall)) )

    
    def controllersFromUuid(self):
        self.checkNode()
        controllers = []
        uuids = cmds.listAttr("bouncingBallVisualizer", ud=1)
        if uuids == None:
            raise Error("No controllers with bouncing balls on the scene")
        for uuidName in uuids:
            id = cmds.getAttr("bouncingBallVisualizer.%s" %uuidName)
            controllers.append(cmds.ls(id)[0])
        return controllers

    def addControllerToList(self, attrName,attrValue):
        self.checkNode()
        cmds.addAttr("bouncingBallVisualizer", longName=attrName, dt='string', category = "Controller")
        cmds.setAttr("bouncingBallVisualizer.%s" %attrName,attrValue[0],type="string")

    def checkNode(self):
        if not cmds.objExists('bouncingBallVisualizer'):
            self.bouncingBallVisualizerNode = cmds.createNode( 'bouncingBallVisualizer', n="bouncingBallVisualizer")
        if not cmds.objExists('bouncingBallSG'):
            self.createShader()

    
    def createShader(self):
        checker=cmds.shadingNode("checker", name = 'bouncingBallCheckerTexture', asTexture=True)
        bb2DTexture=cmds.shadingNode("place2dTexture", name = 'bouncingBallPlace2dTexture', asUtility=True)

        cmds.connectAttr('%s.outUV' %bb2DTexture,'%s.uvCoord' %checker)
        cmds.connectAttr('%s.outUvFilterSize' %bb2DTexture, '%s.uvFilterSize' %checker)

        cmds.setAttr("%s.repeatU" %bb2DTexture, 4.0)      
        cmds.setAttr("%s.repeatV" %bb2DTexture, 4.0)

        material = cmds.shadingNode("lambert", name="bouncingBallMaterial", asShader=True)
        cmds.connectAttr("%s.outColor" %checker, "%s.color" %material )
        sg = cmds.sets(name="bouncingBallSG" , empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr("%s.outColor" % material, "%s.surfaceShader" % sg)

    

class bouncingBallVisDialog(QtWidgets.QDialog):
    def __init__(self,parent = mayaMainWindow()):
        super(bouncingBallVisDialog,self).__init__(parent)

        self.bouncingBall = BouncingBall()
        self.ui = Ui_BBDialog(self)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.createConnections()
        self.sJob = cmds.scriptJob(event=['SelectionChanged', self.selectionChanged])

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
        try:    
            self.bouncingBall.create()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def toggleBallVisibility(self):
        cmds.undoInfo(ock=1)
        try:
            self.bouncingBall.toggleBallVisibility()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def toggleControllerVisibility(self):
        cmds.undoInfo(ock=1)
        try:
            self.bouncingBall.toggleControllerVisibility(deleting = False)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)

    def AllObjectsVisibility(self):
        cmds.undoInfo(ock=1)
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
        try:
            self.bouncingBall.isolateViewOnControllers()
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
    def deleteBouncingBalls(self):
        cmds.undoInfo(ock=1)
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
        try:
            sender = self.sender()
            
            if sender == self.ui.radiusSlider:
                radius = self.ui.radiusSlider.value()
                self.ui.radiusSpinBox.setValue(radius)
            else:
                radius = self.ui.radiusSpinBox.value()
                self.ui.radiusSlider.setValue(radius)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def changeRadius(self):
        cmds.undoInfo(ock=1)
        try:
            radius = self.ui.radiusSlider.value()
            self.bouncingBall.changeRadius(radius)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)
        cmds.undoInfo(cck=1)
    
    def closeEvent(self,event):
        cmds.scriptJob(k=self.sJob)
        event.accept()
        



def showTestWindow():
    global win
    try:
        win.close()
    except: pass
    win = bouncingBallVisDialog()
    win.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    win.show()

showTestWindow()

#*****************************************************************************************************************************************



