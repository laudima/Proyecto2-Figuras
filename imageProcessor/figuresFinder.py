import cv2
from cv2 import Mat

def hex_to_rgb(hex: str):
    return [int(hex[0:2], 16), int(hex[2:4],16), int(hex[4:6],16)]

def hex_to_bgr(hex: str):
    return [int(hex[4:6], 16), int(hex[2:4],16), int(hex[0:2],16)]

def hexColor(tupla):
    res = ""
    res += hex(tupla[2]).removeprefix("0x")
    res += hex(tupla[1]).removeprefix("0x")
    res += hex(tupla[0]).removeprefix("0x")
    return res


def get_colors(bmp  : Mat):
    color_set = set()
    backgroud = hexColor(bmp[0][0])
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            color_set.add(hexColor(bmp[i][j]))
    
    color_set.remove(backgroud)
    return list(color_set)

