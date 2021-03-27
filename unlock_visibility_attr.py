import maya.cmds as cmds

current_selection = cmds.ls(selection=True)

def function(current_selection):
	for i in current_selection:
		is_keyable = cmds.getAttr(i + ".visibility", k = 1)
		is_unlocked = cmds.getAttr(i + ".visibility", se = 1)
		on_off = cmds.getAttr(i + ".visibility")

		if is_keyable == False:
			cmds.setAttr(selection + ".visibility", k = 1)
		else:
			print("Attribute is already keyable")
		if is_unlocked == False:
			cmds.setAttr(selection + ".visibility", l = False)
		else:
			print("Attribute is already unlocked")
		if on_off == False:
			cmds.setAttr(selection + ".visibility", True)
		else:
			print("Attribute is already on")

class unlockVisibility(object):
	"""docstring for unlockVisibility"""
	def __init__(self, *args):
		self.variables = {}
		self.variables["current_selection"] = cmds.ls(selection=True)

	def check_attribute(self, *args):
		for i in self.variables["current_selection"]:
			self.variables["is_keyable"] = cmds.getAttr(i + ".visibility", k = 1)
			self.variables["is_unlocked"] = cmds.getAttr(i + ".visibility", se = 1)
			self.variables["on_off"] = cmds.getAttr(i + ".visibility")
			if self.variables["is_keyable"] == False:
				raise errpr
			if self.variables["is_unlocked"] == True:
				raise error
			if self.variables["on_off"] == False:
				raise error

	def set_visibility_attribute(self, selection):
		cmds.setAttr(selection + ".visibility", k = 1)
		cmds.setAttr(selection + ".visibility", l = False)
		cmds.setAttr(selection + ".visibility", True)


	