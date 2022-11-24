import imageProcessor.imageReader as ir
import imageProcessor.figuresColors as ff
import imageProcessor.figuresContour as fc

if __name__ == '__main__':
    x = ir.read_bitmap("example_5.bmp")
    print(ff.get_colors(x))
    print(fc.get_centers(x))