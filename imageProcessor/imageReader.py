import os
import cv2


def read_bitmap(file):
    """
    Reads an image from the inputs directory given a file.
    """
    return cv2.imread(os.getcwd() + "/inputs/"  + file)
