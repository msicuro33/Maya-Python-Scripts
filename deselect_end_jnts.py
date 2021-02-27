import maya.cmds as cmds

#Select hierarchy and remove end joints
def deselectEndJoints(*args):
	selection = cmds.ls(sl = 1)
	cmds.select(selection, hierarchy = 1)
	full_selection = cmds.ls(sl = 1)
	for i in full_selection:
		if "_end" in i:
			cmds.select(i, deselect = 1)

#Input the name of the selected item into the text box
def inputText(*args):
	sel = cmds.ls(selection=True)
	add = cmds.textField("text_select", edit=True, text=sel[0])

#Create the UI window
def createWindow():
	window = cmds.window()
	cmds.rowColumnLayout()
	cmds.text(label='Selection')
	text_field = cmds.textField("text_select")
	cmds.button(label='Assign Surface', command = inputText)
	cmds.button(label='Do Thing', command = deselectEndJoints)
	cmds.showWindow()