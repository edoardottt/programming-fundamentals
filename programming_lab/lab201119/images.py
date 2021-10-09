"""
Utility functions to read and save an image.
"""
import png


def load(fname):
    """Upload the PNG image from the fname file.
    A list of pixel lists returns. 
    Each pixel is a tuple (R, G, B) of the 3 colors. 
    Each color is an integer between 0 and 255 inclusive.
    """
    with open(fname, mode="rb") as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l += [(line[i], line[i + 1], line[i + 2])]
            img += [l]
        return img


def save(img, filename):
    """Save the img image in the filename file in PNG8 format. 
    Img is a list of pixel lists. 
    Each pixel is a tuple (R, G, B) of the 3 colors. 
    Each color is an integer between 0 and 255 inclusive.
    """
    pngimg = png.from_array(img, "RGB")
    pngimg.save(filename)
