
import cv2
import math
import numpy as np
from cv2 import Mat
import imageProcessor.figuresFinder as ff
import matplotlib.pyplot as plt 

def get_distances(img : Mat, colors):

    centers = []
    distanceContour = []

    for i in range(len(colors)):
        lower = np.array(ff.hex_to_bgr(colors[i]))
        upper = np.array(ff.hex_to_bgr(colors[i]))
    
        mask = cv2.inRange(img, lower, upper)
        inv_mask = cv2.bitwise_not(mask)
        contours, _ = cv2.findContours(inv_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        sumX = 0.0
        sumY = 0.0
        c = len(contours) - 1
        for point in contours[c]:
            sumX += point[0][0]
            sumY += point[0][1]

        averageX = sumX // len(contours[c])
        averageY = sumY // len(contours[c])
        distanceContour.append(distance(averageX,averageY,contours[c]))
        centers.append([averageX, averageY])


    #print(centers)
    #print(distanceContour[0])
    """
    cv2.imshow("mask", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    return distanceContour

def distance(centerX,centerY,contours):
    distanceContour = []
    for point in contours:
        d = math.sqrt(abs(point[0][0] - centerX)**2 + abs(point[0][1] - centerY)**2)
        distanceContour.append(d)
    return distanceContour
