import maya.cmds as cmds

selection = cmds.ls(sl = 1)

for i in selection:
	if "_end" in i:
		cmds.select(i, deselect = 1)