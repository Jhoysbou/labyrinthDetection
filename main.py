import cv2


image = cv2.imread("./images/image_1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image) #
cv2.waitKey(0)