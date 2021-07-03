import maya.cmds as cmds

def cleanJoint():
	'''
	Aims to the next limb joint and creates a clean joint underneath
	'''
	#Selection should be the joint that will be aimed at, then the joint that will be aimed
	selection = cmds.ls(sl=True)
	#create-delete an aim constraint to aim the second joint to the first one
	cmds.delete(cmds.aimConstraint(selection[0], selection[1], aimVector = (1,0,0)))
	#Isolate selection to the second joint, create a clean one underneath with clean Joint Orients and delete the parent
	cmds.select(selection[1])
	cmds.joint()
	cmds.parent(world=1)
	cmds.delete(selection[1])