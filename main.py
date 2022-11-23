import imageProcessor.imageReader as ir
import imageProcessor.figuresFinder as ff
import imageProcessor.figuresContour as fc
if __name__ == '__main__':
    print("Hello Mundo")
    x = ir.read_bitmap("example_1.bmp")
    print(ff.get_colors(x))
    print(fc.get_centers(x))
else:
    print("Hello not in main")
