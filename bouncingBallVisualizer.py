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
        self.bouncingBallVisualizer = ""
        if not cmds.objExists('bouncingBallVisualizer'):
            self.bouncingBallVisualizer = cmds.createNode( 'bouncingBallVisualizer', n="bouncingBallVisualizer")
        try:
            cmds.editDisplayLayerGlobals( cdl='BouncingBalls_SphereShapes' )
        except:
            cmds.createDisplayLayer(e=1, n= "BouncingBalls_SphereShapes")
        pass

    def create(self):
        #Get selected controller
        cmds.undoInfo(ock=1)
        controllers = cmds.ls(sl = 1, tr=1)
        notAdded = []
        for controller in controllers:
            if self.check(controller):
                notAdded.append(controller)
                continue
            controllerUuid = cmds.ls(controller, uuid=1)
            attrName = "uuid_"+controller.replace(":","")
            cmds.addAttr("bouncingBallVisualizer", longName=attrName, dt='string')
            cmds.setAttr("bouncingBallVisualizer.%s" %attrName,controllerUuid[0],type="string")
            #Create sphere
            sphere = cmds.polySphere(ch=1)
            #Parent shape node
            sphere_shape = cmds.listRelatives(s=1, pa=1)
            cmds.parent(sphere_shape,controller, r=1, s=1)
            sphere_shape = cmds.ls(sl=1, l=1)
            #save sphere's shape new long name 
            #set checker texture (REMEMBER TO ADD THE CREATION OF THE TEXTURE TO THE CODE)
            cmds.sets( e=True, forceElement= 'checkerSG' )
            #Selectes adn deletes old transform node
            sphere = cmds.ls (sphere, tr=1)
            cmds.delete(sphere)
            #selects sphere's shape
            cmds.select(sphere_shape)
            self.controllers.append(controller)
        cmds.undoInfo(cck=1)
        print
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
            cmds.undoInfo(ock=1)
            controllers = cmds.ls(sl = 1, tr=1)
            noBall = []
            for controller in controllers:
                if not self.check(controller):
                    noBall.append(controller)
                    continue
                shapes = cmds.listRelatives(s=1, pa=1)
                print(shapes)
                for shape in shapes:
                    print(shape)
                    cmds.select(shape)
                    shapeType = cmds.ls(sl=1,s=1,showType=1)
                    print(shapeType)
                    if  shapeType[1] =="mesh":
                        vis = cmds.getAttr("%s.visibility" %(shape))
                        if vis:
                            cmds.setAttr("%s.visibility" %(shape), 0)
                        else:
                            cmds.setAttr("%s.visibility" %(shape), 1)
            cmds.select(controllers)
            cmds.undoInfo(cck=1)
            if noBall:
                om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a bouncing ball." %(",".join(noBall)) )

    def toggleControllerVisibility(self):
        cmds.undoInfo(ock=1)
        controllers = cmds.ls(sl = 1, tr=1)
        noBall = []
        for controller in controllers:
            if not self.check(controller):
                noBall.append(controller)
                continue
            shapes = cmds.listRelatives(s=1, pa=1)
            print(shapes)
            for shape in shapes:
                print(shape)
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                print(shapeType)
                if  shapeType[1] =="nurbsCurve":
                    vis = cmds.getAttr("%s.visibility" %(shape))
                    if vis:
                        cmds.setAttr("%s.visibility" %(shape), 0)
                    else:
                        cmds.setAttr("%s.visibility" %(shape), 1)
        cmds.select(controllers)
        cmds.undoInfo(cck=1)
        if noBall:
                om.MGlobal.displayWarning("Skipped : %s , Object(s) don't have a nurbsCurve controller." %(",".join(noBall)) )            
    
    def ControllersVisibility(self,vis):
        controllers = []
        uuids = cmds.listAttr("bouncingBallVisualizer", ud=1)
        for uuidName in uuids:
            id = cmds.getAttr("bouncingBallVisualizer.%s" %uuidName)
            controllers.append(cmds.ls(id))
        for controller in controllers:
            shapes = cmds.listRelatives(controller,s=1, pa=1)
            print(shapes)
            for shape in shapes:
                print(shape)
                cmds.select(shape)
                shapeType = cmds.ls(sl=1,s=1,showType=1)
                print(shapeType)
                if  shapeType[1] =="nurbsCurve":
                    cmds.setAttr("%s.visibility" %shape, vis)
    
    def refreshControllersList(self):
        cmds.ls()

    

class bouncingBallVisDialog(QtWidgets.QDialog):
    def __init__(self,parent = mayaMainWindow()):
        super(bouncingBallVisDialog,self).__init__(parent)

        self.bouncingBall = BouncingBall()
        self.ui = Ui_BBDialog(self)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.createConnections()
        #self.sJob = cmds.scriptJob(event=['SelectionChanged', self.selectionChanged])

    def createConnections(self):
       self.ui.createButton.clicked.connect(self.createBouncingBall)
       self.ui.ballVisibilityButton.clicked.connect(self.toggleBallVisibility)
       self.ui.controllerVisibilityButton.clicked.connect(self.toggleControllerVisibility)
       self.ui.controllerAllOnButton.clicked.connect(self.AllControllersOn)
       self.ui.controllerAllOffButton.clicked.connect(self.AllControllersOff)
       pass

    def createBouncingBall(self):
        try:
            selected = cmds.ls(sl=1,tr=1)
            if len(selected) <1:
                raise Error("No controllers selected")
        
            #if self.bouncingBall.check(selected):
            #    raise Warning("Controller already has a bouncing ball")
                
            self.bouncingBall.create()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def toggleBallVisibility(self):
        try:
            selected = cmds.ls(sl=1,tr=1)
            if len(selected) <1:
                raise Error("No controllers selected")
        
            #if self.bouncingBall.check(selected):
            #    raise Warning("Controller already has a bouncing ball")
                
            self.bouncingBall.toggleBallVisibility()
        except Error as e:
           om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def toggleControllerVisibility(self):
        try:
            selected = cmds.ls(sl=1,tr=1)
            if len(selected) <1:
                raise Error("No controllers selected")
        
            #if self.bouncingBall.check(selected):
            #    raise Warning("Controller already has a bouncing ball")
                
            self.bouncingBall.toggleControllerVisibility()
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def AllControllersOff(self):
        try:
            self.bouncingBall.ControllersVisibility(False)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def AllControllersOn(self):
        try:
            self.bouncingBall.ControllersVisibility(True)
        except Error as e:
            om.MGlobal.displayError(e.message)
        except Warning as e:
            om.MGlobal.displayWarning(e.message)

    def selectionChanged(self):
        selected = cmds.ls(sl=1,tr=1)
        if self.bouncingBall.check(selected):
           self.ui.createButton.setDisabled(True)
        else:
           self.ui.createButton.setEnabled(True)


    def closeEvent(self,event):
        #cmds.scriptJob(k= self.sJob)
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



