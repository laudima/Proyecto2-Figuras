import os
import cv2


def read_bitmap(file):
    return cv2.imread(os.getcwd() + "/inputs/"  + file)
