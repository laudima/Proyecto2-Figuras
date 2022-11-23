import imageProcessor.imageReader as ir
import imageProcessor.figuresFinder as ff
if __name__ == '__main__':
    print("Hello Mundo")
    x = ir.read_bitmap("example_1.bmp")
    print(ff.get_colors(x))
else:
    print("Hello not in main")
