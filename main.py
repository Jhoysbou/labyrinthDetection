import cv2
import numpy


image = cv2.imread("./images/image_1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
low = numpy.array((45, 40, 40), numpy.uint8)
high = numpy.array((50, 250, 250), numpy.uint8)

mask_grass = cv2.inRange(image,low, high)

cv2.imshow("Original image", mask_grass) #
cv2.waitKey(0)