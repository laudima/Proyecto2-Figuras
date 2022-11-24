import imageProcessor.imageReader as ir
import imageProcessor.figuresFinder as ff
import imageProcessor.noisyPeakFinder as pf
if __name__ == '__main__':
    print("Hello Mundo")
    x = ir.read_bitmap("example_1.bmp")
    # print(pf.count_peaks(array))
    print(ff.get_colors(x))
else:
    print("Hello not in main")
