def lonlat_convert (x, y, option = 'r'):

	""" Lon, Lat Converter
	
	Parameters
	----------
	x : integer, the image x-axis from left-bottom.
	y : integer, the image y-axis from left-bottom.
	option : string, optional (default = r), for which kind of image to convert.

	Returns
	-------
	[Lon, Lat] : list of Lon and Lat.
	
	"""

	assert isinstance(x, int), "The x value should be an integer"
	assert isinstance(y, int), "The y value should be an integer"

	if option == 'r':
		assert x >= 0 and x < 1024, "The x value should be >= 0 and < 1024"
		assert y >= 0 and y < 1024, "The y value should be >= 0 and < 1024"
		return [x * 0.00732422  + 117.3, y * 0.00732422 + 19.7]
	elif option == 's':
		assert x >= 0 and x < 800, "The x value should be >= 0 and < 800"
		assert y >= 0 and y < 800, "The y value should be >= 0 and < 800"
		return [x * 0.01255764031875 + 115.976888855, y * 0.01255764031875 + 19.100625745]
	elif option == 'q':
		assert x >= 0 and x < 75, "The x value should be >= 0 and < 75"
		assert y >= 0 and y < 95, "The y value should be >= 0 and < 95"
		return [x * 0.075 + 117.975, y * 0.075 + 19.975]
	else:
		return [-1, -1]

