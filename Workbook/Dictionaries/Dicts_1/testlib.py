import argparse, csv, glob, time, sys

import unittest, unittest.mock


class ForbiddenError(Exception):
    pass


class TimeoutError(Exception):
    pass


class Timer:
    def __init__(self, timeout):
        self.timeout = timeout

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        tempo = round(time.time() - self.start, 3)
        if tempo > self.timeout:
            raise TimeoutError(f"Timeout ({tempo} > {self.timeout})")


class TestCase(unittest.TestCase):
    def _raise_forbidden(self, forbidden):
        # lancia una eccezione
        raise ForbiddenError(f "It is forbidden to use the function / method {forbidden}")

    def forbidden_function(self, target="builtins.print"):
        #returns a context that prohibits the use of the target function: by default 'builtins.print'
        return unittest.mock.patch(
            target, new=lambda *x, **y: self._raise_forbidden(target)
        )

    def ignored_function(self, target="builtins.print"):
        # returns a context that causes the target function to be ignored: by default 'builtins.print
        return unittest.mock.patch(target, new=lambda *x, **y: None)

    def timer(self, sec):
        """returns a context whose execution time is measured and if necessary an exception for timeout is thrown"""
        return Timer(sec)

    def check(self, value, expected, params=None, explanation=""):
        # TODO: add deepcopy of value to avoid side effects
        msg = ""
        if params:
            msg += "\twhen input={} ".format(params)
        msg += "\n\t\t%r != %r" % (value, expected)
        if explanation:
            msg += "\t<- " + explanation
        self.assertEqual(value, expected, msg)

    def check_text_file(self, a, b):
        with open(a, "rU", encoding="utf8") as f:
            txt_a = f.read()
        with open(b, "rU", encoding="utf8") as f:
            txt_b = f.read()
        lines_a = [l.strip() for l in txt_a.splitlines()]
        lines_b = [l.strip() for l in txt_b.splitlines()]
        # todo: use a diff
        msg = "text differ: " + a + " " + b
        self.assertEqual(lines_a, lines_b, msg)

    def __image_load(self, filename):
        """Upload the image in PNG format from the file 
        filename, converts it to the matrix format 
        of tuples and returns it"""
        import png

        with open(filename, "rb") as f:
            # reads the image as RGB with 256 values
            r = png.Reader(file=f)
            iw, ih, png_img, _ = r.asRGB8()
            # convert to list of tuple lists
            img = []
            for png_row in png_img:
                row = []
                # the PNG image has the colors in 
                # a single array so we read them 
                # three at a time in a tuple
                for i in range(0, len(png_row), 3):
                    row.append((png_row[i + 0], png_row[i + 1], png_row[i + 2]))
                img.append(row)
        return img

    def check_img_file(self, a, b):
        img_a = self.__image_load(a)
        img_b = self.__image_load(b)
        wa, ha = len(img_a[0]), len(img_a)
        wb, hb = len(img_b[0]), len(img_b)
        self.assertEqual(wa, wb, "images have different widts {} != {})".format(wa, wb))
        self.assertEqual(
            ha, hb, "images have different heights {} != {})".format(ha, hb)
        )
        for y in range(ha):
            for x in range(wa):
                ca, cb = img_a[y][x], img_b[y][x]
                msg = "images differ, starting at coordinates {},{} (colors: {} != {})".format(
                    x, y, ca, cb
                )
                self.assertEqual(ca, cb, msg)

    def check_json_file(self, a, b, msg="The two JSON files contain different structures"):
        import json

        with open(a, "r", encoding="utf8") as f1:
            A = json.load(f1)
        with open(b, "r", encoding="utf8") as f2:
            B = json.load(f2)
        self.assertEqual(A, B, msg)

    @classmethod
    def main(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
        result = runner.run(suite)
        failed = len(result.failures)
        passed = result.testsRun - failed
        print("{} test passed, {} tests failed".format(passed, failed))
