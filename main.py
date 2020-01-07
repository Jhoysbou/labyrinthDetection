import math

import cv2
import numpy
import sys

image = 0
def totup(x, y, side):
    global image
    result = 0

    for line in range(side):
        for pixel in range(side):
            result += image[x * side + line][y * side + pixel]
    return result


def main():
    global image

    image = cv2.imread(sys.argv[1])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    low = numpy.array((0, 0, 0), numpy.uint8)
    high = numpy.array((255, 255, 174), numpy.uint8)

    image = cv2.inRange(image, low, high)
    # contours, hierarchy = cv2.findContours(image.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    #
    # cv2.drawContours(image, contours, -1, (255, 255, 0), 3)

    # cv2.imshow("contour", image)
    # cv2.waitKey(0)
    # center = tuple(numpy.array(image.shape[1::-1]) / 2)
    # angle = 0
    # scale = math.sin(math.radians(angle)) + 1
    # matrix = cv2.getRotationMatrix2D(center, angle , scale)
    # image = cv2.warpAffine(image, matrix, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    #
    # cv2.imshow("contour", image)
    # cv2.waitKey(0)

    size = image.shape
    counter = 0

    for part in range(2, 5):
        line = int(size[0] / part)
        for pixel in range(size[1]):
            if image[line][pixel] < 50:
                counter += 1
            if image[line][pixel] > 200 and counter != 0:
                break

    squareSide = counter

    arraySize = (int(size[0] / squareSide), int(size[1] / squareSide))
    maxSum = squareSide ** 2 * 255

    array = numpy.zeros(arraySize)

    for i in range(arraySize[0]):
        for j in range(arraySize[1]):
            squareSum = totup(i, j, squareSide)
            if squareSum < maxSum / 2:
                array[i][j] = 1

    for line in array:
        print(str(line))




    # cv2.imwrite('image1.jpg', image)
    #
    # image = Image.open('image1.jpg')
    # image.load()
    # image = image.resize((21, 21), Image.NEAREST)
    # image.save('image1.jpg')


    # image = image.astype(numpy.float) / 255.
    # image[image > 0.5] = 1.0  # round
    # image[image <= 0.5] = 0.0
    #
    # size = image.shape
    # for line in range(size[0]):
    #     for pixel in range(size[1]):
    #         if image[line][pixel] == 0:
    #             image[line][pixel] = 1
    #         elif image[line][pixel] == 1:
    #             image[line][pixel] = 0

    print("Done")

    # resized = imutils.resize(image, width=50)
    # size = resized.shape


    # for line in range(size[0]):
    #     for pixel in range(size[1]):
    #         if resized[line][pixel] > 200:
    #             resized[line][pixel] = 255
    #
    #         if resized[line][pixel] < 100:
    #             resized[line][pixel] = 0

    # cv2.imshow("Converted", resized)
    # cv2.waitKey(0)

if __name__ == "__main__":
    main()
