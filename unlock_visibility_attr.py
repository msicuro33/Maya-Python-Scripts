import maya.cmds as cmds

def unlockVisibility():
	#Stores the current selction(can be anything, mostly intended for joints)
	current_selection = cmds.ls(selection=True)

	#Queries if the Visibility attribute of the current selection is keyable, unlocked and/or already on
	for i in current_selection:
		is_keyable = cmds.getAttr(i + ".visibility", k = 1)
		is_unlocked = cmds.getAttr(i + ".visibility", se = 1)
		on_off = cmds.getAttr(i + ".visibility")
		# Checks if the attribute is keyable, unlocked or on and outputs a message or turns on the attribute
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