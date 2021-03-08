import maya.cmds as cmds

class deselectEndJointsClass(object):
	"""docstring for deselectEndJointsClass"""
	def __init__(self, *args):
		self.variables = {}
		
	#Create the UI window
	def createUI(self, *args):
		self.variables["window"] = cmds.window(title = "Deselect_Joints_Window")
		self.variables["rowLayout"] = cmds.rowColumnLayout(numberOfRows = 1)
		self.variables["layout_text"] = cmds.text(label='Selection')
		self.variables["text_field"] = cmds.textField("text_select")
		self.variables["input_text_button"] = cmds.button(label='Assign Surface', command = inputText)
		self.variables["deselect_endJoints_button"] = cmds.button(label='Do Thing', command = deselectEndJoints)
		cmds.showWindow()
	
	#Select hierarchy and remove end joints
	def deselectEndJoints(self, *args):
		selection = cmds.ls(sl = 1)
		cmds.select(selection, hierarchy = 1)
		full_selection = cmds.ls(sl = 1)
		for i in full_selection:
			if "_end" in i:
				cmds.select(i, deselect = 1)

	#Input the name of the selected item into the text box
	def inputText(self, *args):
		self.variables["current_selection"] =  = cmds.ls(selection=True)
		cmds.textField(self.variables["text_field"], edit=True, text=sel[0])

	