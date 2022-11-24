import cv2
from cv2 import Mat

def hex_to_rgb(hex: str):
    return [int(hex[0:2], 16), int(hex[2:4],16), int(hex[4:6],16)]

def hex_to_bgr(hex: str):
    return [int(hex[4:6], 16), int(hex[2:4],16), int(hex[0:2],16)]

def hex_color(tupla):
    res = ""
    
    prov1 = hex(tupla[2]).removeprefix("0x")
    if(len(prov1) == 1 ):
        res += "0" + prov1
    else:
        res += prov1
    prov2 = hex(tupla[1]).removeprefix("0x") 
    if(len(prov2) == 1 ):
        res += "0" + prov2
    else:
        res += prov2
    prov3 = hex(tupla[0]).removeprefix("0x")
    if(len(prov3) == 1):
        res += "0" + prov3
    else:
        res += prov3
    return res


def get_colors(bmp  : Mat):
    color_set = set()
    backgroud = hex_color(bmp[0][0])
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            color_set.add(hex_color(bmp[i][j]))
    
    color_set.remove(backgroud)
    return list(color_set)