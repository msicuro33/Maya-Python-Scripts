import maya.cmds as cmds

#Creates a Null, Zero and Buff group above the currently selected object at it's location

def createBufferGroups():
	selection = cmds.ls(sl=True)

	for each in selection:
	    grp1 = cmds.group(empty=True, n = each + "_NULL_GRP")
	    cmds.delete(cmds.parentConstraint(each, grp1)[0])
	    grp2 = cmds.group(empty=True, n = each + "_ZERO_GRP")
	    cmds.delete(cmds.parentConstraint(each, grp2)[0])
	    grp3 = cmds.group(empty=True, n = each + "_BUFF_GRP")
	    cmds.delete(cmds.parentConstraint(each, grp3)[0])
	    cmds.parent(each, grp3)
	    cmds.parent(grp3, grp2)
	    cmds.parent(grp2, grp1)
	    cmds.makeIdentity(each, t=1, r=1,s=1, apply=True)
