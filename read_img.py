import cv2
import ConvConvert

# read image
img = cv2.imread('/path/to/img')
# change the colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# show the convert result
print(ConvConvert.conv(hsv[y_coordinate][x_coordinate]))
