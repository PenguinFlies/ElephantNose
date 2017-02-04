import cv2

def rgb_convert (rgb, option = "HSV"):

	""" Convert RGB into HSV or HSL

	Parameters
	----------
	rgb: list of RGB value
	option : string, optional (default = "HSV")
		"HSV" for converting HSV, "HSL" for converting HSL 

	Returns
	-------
	list of HSV value (if option = "HSV")
	list of HSL value (if option = "HSL")
	
	"""
	
	assert len(rgb) == 3, 'rgb should have 3 elements'
	for i in range(3):
		#print(isinstance(rgb[i], int))
		assert isinstance(rgb[i], int) == True, 'rgb list element should be integer'	
	
	ra = rgb[0] / 255
	ga = rgb[1] / 255
	ba = rgb[2] / 255
	cmax = max(ra, ga, ba)
	cmin = min(ra, ga, ba)
	delta = cmax - cmin
	lightness = (cmax - cmin) / 2
	
	# Calculate Hue

	if delta == 0:
		hue = 0
	elif cmax == ra:
		hue = 60 * (((ga - ba) / delta) % 6)
	elif cmax == ga:
		hue = 60 * (((ba - ra) / delta) + 2)
	elif cmax == ba:
		hue = 60 * (((ra - ga) / delta) + 4)

	# Calculate Saturation
	
	if delta == 0:
		saturation = 0
	else:
		saturation = delta / (1 - abs(2 * lightness - 1))

	if option == "HSL":
		if delta == 0:
			saturation = 0
		else:
			saturation = delta / (1 - abs(2 * lightness - 1))
		return [hue, saturation, lightness]
	elif option == "HSV":
		if cmax == 0:
			saturation = 0
		else:
			saturation = delta / cmax
		return [hue, saturation, cmax]
	else:
		return [-1, -1, -1]    
