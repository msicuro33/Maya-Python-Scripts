import maya.cmds as cmds

def unlockVisibility():
	current_selection = cmds.ls(selection=True)
	for i in current_selection:
		is_keyable = cmds.getAttr(i + ".visibility", k = 1)
		is_unlocked = cmds.getAttr(i + ".visibility", se = 1)
		on_off = cmds.getAttr(i + ".visibility")

		if is_keyable == False:
			cmds.setAttr(i + ".visibility", k = 1)
		else:
			print("Attribute is already keyable")
		if is_unlocked == False:
			cmds.setAttr(i + ".visibility", l = False)
		else:
			print("Attribute is already unlocked")
		if on_off == False:
			cmds.setAttr(i + ".visibility", True)
		else:
			print("Attribute is already on")