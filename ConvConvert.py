import numpy as np

def conv (hsv):
	h = hsv[0]
	s = hsv[1]
	v = hsv[2]
	
	assert hsv[0] >= 0 and hsv[0] <= 179, 'Hue value is not valid'
	assert hsv[1] >= 0 and hsv[0] <= 255, 'Saturation value is not valid'
	assert hsv[2] >= 0 and hsv[2] <= 255, 'Value value is not valid'
 
	
	if hsv[0] >= 55 and hsv[0] <= 65 and hsv[1] >= 230 and hsv[2] >= 140:
		return 1
	elif hsv[0] >= 12 and hsv[0] <= 35 and hsv[1] >= 230 and hsv[2] >= 230:
		return 2
	elif hsv[0] >= 160 or hsv[0] <= 10 and hsv[1] >= 230 and hsv[2] >= 140:
		return 3
	elif hsv[0] >= 145 and hsv[0] <= 155 and hsv[1] >= 230 and hsv[2] >= 230:
		return 4
	elif hsv[0] >= 135 and hsv[0] <= 140 and hsv[1] >= 230 and hsv[2] >= 230:
		return 5
	else:
		return -1

		
