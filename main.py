import imageProcessor.imageReader as ir
import imageProcessor.figuresFinder as ff
import imageProcessor.noisyPeakFinder as pf
import imageProcessor.figuresContour as fc
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = ir.read_bitmap("example_5.bmp")
    colors = list(ff.get_colors(x))
 
    distances = fc.get_distances(x,colors)

    for i,color in enumerate(colors):
        peaks = pf.count_peaks(distances[i])
        if peaks <= 3:
            print(color,"= T")
        elif peaks == 4:
            print(color,"= C")
        elif peaks > 9:
            print(color,"= O")
        else:
            print(color,"= X")
   
else:
    print("Hello not in main")
