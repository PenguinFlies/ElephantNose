def conv_convert (hsv, precise = False, more_stage = False):

	""" Convection Converter

	Parameters
	----------
	hsv : list, [H, S, V]
	precise : boolean, optional (default = False), the output precision
	more_stage : boolean, optional (default = False), affect on precise is true. Caution: may lead misjudge.

	Returns
	-------
	integer : 1 to 5 for different strength IN NOT precise mode.
		  1 to 12(13 in more_stage mode) for different strength IN precise mode.
		  -1 while cannot classify.
	"""

	assert hsv[0] >= 0 and hsv[0] <= 179, 'Hue value is not valid'
	assert hsv[1] >= 0 and hsv[0] <= 255, 'Saturation value is not valid'
	assert hsv[2] >= 0 and hsv[2] <= 255, 'Value value is not valid'
 
	
	if precise == False:
		if hsv[0] >= 50 and hsv[0] <= 70 and hsv[1] >= 200 and hsv[2] >= 140:
			return 1
		elif hsv[0] >= 10 and hsv[0] <= 40 and hsv[1] >= 200 and hsv[2] >= 200:
			return 2
		elif (hsv[0] >= 160 or hsv[0] <= 10) and hsv[1] >= 200 and hsv[2] >= 140:
			return 3
		elif hsv[0] >= 145 and hsv[0] <= 155 and hsv[1] >= 200 and hsv[2] >= 200:
			return 4
		elif hsv[0] >= 135 and hsv[0] <= 140 and hsv[1] >= 200 and hsv[2] >= 200:
			return 5
		elif hsv[1] <= 5 and hsv[2] >= 250:
			return 5
		else:
			return -1
	elif precise == True:
		if hsv[0] >= 50 and hsv[0] <= 70 and hsv[1] >= 200 and hsv[2] >= 140 and hsv[2] <= 170:
			return 3
		elif hsv[0] >= 50 and hsv[0] <= 70 and hsv[1] >= 200 and hsv[2] > 190 and hsv[2] <= 205:
			return 2
		elif hsv[0] >= 50 and hsv[0] <= 70 and hsv[1] >= 200 and hsv[2] > 240 and hsv[2] <= 255:
			return 1
		elif hsv[0] >= 10 and hsv[0] <= 18 and hsv[1] >= 200 and hsv[2] >= 200:
			return 6
		elif hsv[0] >= 20 and hsv[0] <= 28 and hsv[1] >= 200 and hsv[2] >= 200:
			return 5
		elif hsv[0] > 28 and hsv[0] <= 35 and hsv[1] >= 200 and hsv[2] >= 200:
			return 4
		elif (hsv[0] >= 160 or hsv[0] <= 10) and hsv[1] >= 200 and hsv[2] >= 140 and hsv[2] <= 170:
			return 9
		elif (hsv[0] >= 160 or hsv[0] <= 10) and hsv[1] >= 200 and hsv[2] >= 180 and hsv[2] <= 205:
			return 8
		elif (hsv[0] >= 160 or hsv[0] <= 10) and hsv[1] >= 200 and hsv[2] >= 230 and hsv[2] <= 255:
			return 7
		elif hsv[1] <= 5 and hsv[2] >= 250:
			return 12
		elif hsv[0] >= 135 and hsv[0] <= 140 and hsv[1] >= 200 and hsv[2] >= 200:
			return 11
		elif hsv[0] >= 145 and hsv[0] <= 155 and hsv[1] >= 200 and hsv[2] >= 200:
			return 10
		elif more_stage == True and hsv[0] >= 125 and hsv[0] <= 135 and hsv[1] >= 29 and hsv[1] <= 38 and hsv[2] >= 200:
			return 13
		else:
			return -1
		
