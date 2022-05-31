
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
from PySide2 import QtCore,QtWidgets,QtGui

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
            attrName = "uuid_"+''.join(ch for ch in controller if ch.isalnum())

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
        self.toggleControllerVisibility(deleting=False)
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
                    attrName = "uuid_"+''.join(ch for ch in controller if ch.isalnum())
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

if __name__ == "__main__":
    pass