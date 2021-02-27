import maya.cmds as cmds

#Sets the outlinerColor attribute coloring the corresponding outliner text

def lightBlue(selection):
	selection = cmds.ls(sl=True)
	for each in selection:
		cmds.setAttr(each + ".useOutlinerColor", 1)
		cmds.setAttr(each + ".outlinerColor", 0, 1, 1)

def pink(selection):
	selection = cmds.ls(sl=True)
	for each in selection:
		cmds.setAttr(each + ".useOutlinerColor", 1)
		cmds.setAttr(each + ".outlinerColor", 1, 0.378, 1)

def yellow(selection):
	selection = cmds.ls(sl=True)
	for each in selection:
		cmds.setAttr(each + ".useOutlinerColor", 1)
		cmds.setAttr(each + ".outlinerColor", 1, 1, 0)

def createWindow():
	cmds.window(title = "outlinerColorWindow")
	cmds.columnLayout()
	cmds.button(label = "Light Blue", backgroundColor = [0, 1, 1], command = lightBlue)
	cmds.button(label = "Pink", backgroundColor = [1, 0.378, 1], command = pink)
	cmds.button(label = "Yellow", backgroundColor = [1, 1, 0], command = yellow)
	cmds.showWindow()