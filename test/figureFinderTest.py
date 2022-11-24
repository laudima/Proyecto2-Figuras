import unittest
import sys
sys.path.insert(0, './')
import imageProcessor.figuresColors as ff
import imageProcessor.imageReader as ir

class test_figure_color(unittest.TestCase):

    def test_hex_to_rgb(self):
        self.assertEqual([0,0,0], ff.hex_to_rgb("000000"))
        self.assertEqual([255,255,255], ff.hex_to_rgb("FFFFFF"))
        self.assertEqual([4,6,234], ff.hex_to_rgb("0406EA"))
    

    def test_hex_to_bgr(self):
        self.assertEqual([0,0,0], ff.hex_to_bgr("000000"))
        self.assertEqual([255,255,255], ff.hex_to_bgr("FFFFFF"))
        self.assertEqual([234,6,4], ff.hex_to_bgr("0406EA"))

    def test_get_colors(self):
        bitmap_test_1 = ir.read_bitmap("example_1.bmp")
        test_1_colors = ff.get_colors(bitmap_test_1)
        test_1_color_list = {"c8a566","965c32","7b6a4e"}
        for color in test_1_color_list:
            if(color not in test_1_colors):
                self.assertFalse()

    def test_hex_color(self):
        test = [55,15,4]
        self.assertEqual("040f37", ff.hex_color(test))


if __name__ == '__main__':
    unittest.main()