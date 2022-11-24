import cv2
from cv2 import Mat

def hex_to_rgb(hex: str):
    """
    Takes an hexadecimal color string and converts it to an RGB tuple.
    """
    return [int(hex[0:2], 16), int(hex[2:4],16), int(hex[4:6],16)]

def hex_to_bgr(hex: str):
    """
    Takes an hexadecimal color string and converts it to an BGR tuple.
    """
    return [int(hex[4:6], 16), int(hex[2:4],16), int(hex[0:2],16)]

def hex_color(tuple):
    """
    Takes a tuple in RGB and makes it into an hexadecimal color string.
    """

    res = ""
    
    prov1 = hex(tuple[2]).removeprefix("0x")
    if(len(prov1) == 1 ):
        res += "0" + prov1
    else:
        res += prov1
    prov2 = hex(tuple[1]).removeprefix("0x") 
    if(len(prov2) == 1 ):
        res += "0" + prov2
    else:
        res += prov2
    prov3 = hex(tuple[0]).removeprefix("0x")
    if(len(prov3) == 1):
        res += "0" + prov3
    else:
        res += prov3
    return res


def get_colors(bmp  : Mat):
    """
    Gets all the distict colors, excluding of a given matrix.
    """

    color_set = set()
    backgroud = hex_color(bmp[0][0])
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            color_set.add(hex_color(bmp[i][j]))
    
    color_set.remove(backgroud)
    return list(color_set)

