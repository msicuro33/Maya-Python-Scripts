import maya.cmds as cmds

class unlockVisibility(object):
	"""docstring for unlockVisibility"""
	def __init__(self, *args):
		self.variables = {}
		self.createUI()
		
	#Create the UI window
	def createUI(self, *args):
		self.variables["window"] = cmds.window(title = "unlock_visibility_window")
		self.variables["rowLayout"] = cmds.rowColumnLayout(numberOfRows = 1)
		self.variables["layout_text"] = cmds.text(label='Selection')
		self.variables["text_field"] = cmds.textField("text_select")
		self.variables["make_keyable_button"] = cmds.button(label='Make Visibility Keyable', command = self.)
		self.variables["unlock_attr_button"] = cmds.button(label='Unlock Attribute', command = self.)
		self.variables["turn_visibility_attr_on"] = cmds.button(label='Turn On Attribute', command = self.)
		cmds.showWindow()
	
	#Select hierarchy and remove end joints
	def deselectEndJoints(self, *args):
		cmds.select(self.variables["current_selection"][0], hierarchy = 1)
		full_selection = cmds.ls(sl = 1)
		for i in full_selection:
			if "_end" in i:
				cmds.select(i, deselect = 1)

	#Input the name of the selected item into the text box
	def inputText(self, *args):
		self.variables["current_selection"] = cmds.ls(selection=True)
		cmds.textField(self.variables["text_field"], edit=True, text=self.variables["current_selection"][0])

	