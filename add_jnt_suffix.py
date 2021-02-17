import maya.cmds as cmds

#Add the _JNT suffix to all currently selected objects

selection = cmds.ls(sl = 1)

for i in selection:
	current_name = i
	cmds.rename(i, i +"_JNT")