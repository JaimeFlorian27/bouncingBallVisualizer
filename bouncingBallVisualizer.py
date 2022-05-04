import maya.cmds as cmds
import maya.mel as mel

#Get selected controller
controller = cmds.ls(sl = 1)

#Create sphere

sphere = cmds.polySphere(ch=1)

#Parent shape node (deleting old transform node)

sphere_shape = cmds.listRelatives(s=1, pa=1)
cmds.parent(sphere_shape,controller, r=1, s=1)
cmds.sl(sphere)
mel.eval("doDelete")