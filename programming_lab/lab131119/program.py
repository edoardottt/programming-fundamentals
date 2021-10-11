#sum of matrices
#
# 1 2 3    2 2 2   3  4  5
# 4 5 6 +  2 2 2 = 6  7  8
# 7 8 9    2 2 2   9 10 11


def sum(mat1, mat2):
    mat3 = mat1.copy()
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] += mat2[i][j]
    return mat3


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
sum(mat1, mat2)


################################################

# matrix transpose:
#
# from matrix h x w we obtain matrix w x h
# 1 2 3            1 4
# 4 5 6  ------>   2 5
#                  3 6


def transpose(mat):
    h, w = len(mat), len(mat[0])
    # creates matrix of zeros of dimensions w x h
    mat1 = []
    for h1 in range(w):
        row = [0] * h
        mat1.append(row)
    # inserts values into the matrix
    for i in range(h):
        for j in range(w):
            mat1[j][i] = mat[i][j]
    return mat1


mat = [[1, 2, 3], [4, 5, 6]]
transpose(mat)
#  [[1, 4], [2, 5], [3, 6]]


###############################################

# product of matrices
# matrices of dimensions 3x2 and 2x4 give matrix 3x4
#
# 1 2    1 2 3 4      11 14 17 20
# 3 4 *  5 6 7 8  =   23 30 37 44
# 5 6                 35 46 57 68


def prodScal(i, j, mat1, mat2):
    w = len(mat1[0])
    tot = 0
    for k in range(w):
        tot += mat1[i][k] * mat2[k][j]
    return tot


def prod(mat1, mat2):
    h1 = len(mat1)
    w2 = len(mat2[0])
    # generates matrix of zeros of size h1xw2
    mat3 = []
    for i in range(h1):
        riga = [0] * w2
        mat3.append(riga)
    # inserts values into the array
    for i in range(h1):
        for j in range(w2):
            mat3[i][j] = prodScal(i, j, mat1, mat2)
    return mat3


mat1 = [[1, 2], [3, 4], [5, 6]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
prod(mat1, mat2)
# [[11, 14, 17, 20], [23, 30,37, 44], [35, 46, 57, 68]]

###############################################
###############################################
###############################################


def create(h, w, c=(0, 0, 0)):
    """returns a monochrome height image 
    alt and width lar and color c"""
    img = []
    for _ in range(h):
        row = [c] * w
        img += [row]
    return img


a = create(10, 10)

import images

images.save(a, "prova1.png")

################################################


def rotate1(img):
    """
    Returns a new image which is the image 
    img rotated around its horizontal axis
    """
    h, w = len(img), len(img[0])
    ret = create(h, w, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = img[h - 1 - y][x]
    return ret


img = images.load("fiore.png")
img1 = rotate1(img)
images.save(img1, "fiore1.png")


###############################################


def rotate2(img):
    """
    Returns a new image which is the image 
    where I swapped rows with columns
    """
    h, w = len(img), len(img[0])
    ret = create(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[x][y] = img[y][x]
    return ret


img = images.load("fiore.png")
img1 = rotate2(img)
images.save(img1, "fiore1.png")
##################################################


def border(img, s, c):
    """returns img image with border of thickness s and color c"""
    w, h = len(img[0]), len(img)
    img1 = create(h + s * 2, w + s * 2, c)
    for row in range(h):
        for column in range(w):
            img1[row + s][column + s] = img[row][column]
    return img1


img = images.load("fiore.png")
img1 = border(img, 10, (255, 0, 0))
images.save(img1, "fiore1.png")

#################################################


def square(img, y, x, l, col):
    """inserts on img a square of side l with vertex in 
    top left in pixel i, j"""
    for i in range(y, y + l):
        for j in range(x, x + l):
            img[i][j] = col


img = create(100, 100)
square(img, 10, 10, 30, (255, 0, 0))
square(img, 30, 20, 50, (0, 255, 0))
images.save(img, "prova.png")


square(img, 70, 70, 50, (0, 0, 255))

# correct version


def square1(img, y, x, l, col):
    """inserts on img a square of side l with vertex in 
    top left in pixel i, j"""
    h, w = len(img), len(img[0])
    for i in range(y, y + l):
        for j in range(x, x + l):
            if i < h and j < w:
                img[i][j] = col


square1(img, 70, 70, 50, (0, 0, 255))
images.save(img, "prova.png")

##################################################


def invert(img):
    """Returns a new image that is 
    img image with inverted colors"""
    w, h = len(img[0]), len(img)
    ret = create(h, w)
    for y in range(h):
        for x in range(w):
            r, g, b = img[y][x]
            ret[y][x] = (255 - r, 255 - g, 255 - b)
    return ret


img = images.load("fiore.png")
img1 = invert(img)
images.save(img1, "fiore1.png")

####################################################


def grey(img):
    """
    returns a new image which is the image 
    img with grayscale colors. 
    In this case each pixel of colors R, G, B must have as 
    color their average
    """
    h, w = len(img), len(img[0])
    img1 = create(h, w)
    for y in range(h):
        for x in range(w):
            c = round(sum(img[y][x]) / 3)
            img1[y][x] = c, c, c
    return img1


img = images.load("fiore.png")
img1 = grey(img)
images.save(img1, "fiore1.png")
