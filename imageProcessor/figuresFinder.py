import cv2
from cv2 import Mat

def hexColor(tupla):
    res = ""
    res += hex(tupla[2]).removeprefix("0x")
    res += hex(tupla[1]).removeprefix("0x")
    res += hex(tupla[0]).removeprefix("0x")
    return res


def get_colors(bmp  : Mat):
    color_set = set()
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            color_set.add(hexColor(bmp[i][j]))
    return color_set

