import sys
import imageProcessor.imageReader as ir
import imageProcessor.noisyPeakFinder as pf
import imageProcessor.figuresContour as figCon
import imageProcessor.figuresColors as figCol
import matplotlib.pyplot as plt

def printColor(color, text):
    """
    Print a given text with the color and with the color hex in front of it.
    """
    rgb = figCol.hex_to_rgb(color)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    textColor = '\033[{};2;{};{};{}m'.format(38, r, g, b)
    print(textColor + color + text)

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        file = str(sys.argv[1])
    else:
        print("Please provide file correctly")
        exit()
    
    x = ir.read_bitmap(file)

    colors = list(figCol.get_colors(x))
 
    distances = figCon.get_distances(x,colors)

    for i,color in enumerate(colors):
        peaks = pf.count_peaks(distances[i])
        if peaks <= 3:
            printColor(color, " = T")
        elif peaks == 4:
            printColor(color," = C")
        elif peaks > 9:
            printColor(color," = O")
        else:
            printColor(color," = X")
   