# somma di matrici:
#
# 1 2 3    2 2 2   3  4  5
# 4 5 6 +  2 2 2 = 6  7  8
# 7 8 9    2 2 2   9 10 11


def somma(mat1, mat2):
    mat3 = mat1.copy()
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] += mat2[i][j]
    return mat3


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
somma(mat1, mat2)


################################################

# trasposta di matrice:
#
# da matrice h x w si ottiene matrice w x h
# 1 2 3            1 4
# 4 5 6  ------>   2 5
#                  3 6


def trasposta(mat):
    h, w = len(mat), len(mat[0])
    # crea  matrice di zeri di dimensioni w x h
    mat1 = []
    for h1 in range(w):
        riga = [0] * h
        mat1.append(riga)
    # inserisce i valori nella matrice
    for i in range(h):
        for j in range(w):
            mat1[j][i] = mat[i][j]
    return mat1


mat = [[1, 2, 3], [4, 5, 6]]
trasposta(mat)
#  [[1, 4], [2, 5], [3, 6]]


###############################################

# prodotto di matrici
# matrici di dimensioni 3x2 e 2x4 danno matrice 3x4
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
    # genera matrice di zeri di dimensioni h1xw2
    mat3 = []
    for i in range(h1):
        riga = [0] * w2
        mat3.append(riga)
    # inserisce i valori nella matrice
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


def crea(h, w, c=(0, 0, 0)):
    """ritorna un'immagine monocromatica  di altezza
    alt e larghezza lar e colore c"""
    img = []
    for _ in range(h):
        riga = [c] * w
        img += [riga]
    return img


a = crea(10, 10)

import immagini

immagini.save(a, "prova1.png")

################################################


def ruota1(img):
    """Ritorna una nuova immagine che e' l'immagine
    img ruotata intorno al suo asse orizzontale
    """
    h, w = len(img), len(img[0])
    ret = crea(h, w, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = img[h - 1 - y][x]
    return ret


img = immagini.load("fiore.png")
img1 = ruota1(img)
immagini.save(img1, "fiore1.png")


###############################################


def ruota2(img):
    """Ritorna una nuova immagine che e' l'immagine
    in cui ho scambiato righe con colonne
    """
    h, w = len(img), len(img[0])
    ret = crea(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            ret[x][y] = img[y][x]
    return ret


img = immagini.load("fiore.png")
img1 = ruota2(img)
immagini.save(img1, "fiore1.png")
##################################################


def bordo(img, s, c):
    """restituisce immagine img con  bordo di spessore s  e colore c"""
    w, h = len(img[0]), len(img)
    img1 = crea(h + s * 2, w + s * 2, c)
    for riga in range(h):
        for colonna in range(w):
            img1[riga + s][colonna + s] = img[riga][colonna]
    return img1


img = immagini.load("fiore.png")
img1 = bordo(img, 10, (255, 0, 0))
immagini.save(img1, "fiore1.png")

#################################################


def quadrato(img, y, x, l, col):
    """inserisce su img un quadrato di lato l con vertice in
    alto a sinistra nel pixel i,j"""
    for i in range(y, y + l):
        for j in range(x, x + l):
            img[i][j] = col


img = crea(100, 100)
quadrato(img, 10, 10, 30, (255, 0, 0))
quadrato(img, 30, 20, 50, (0, 255, 0))
immagini.save(img, "prova.png")


quadrato(img, 70, 70, 50, (0, 0, 255))

# versione corretta


def quadrato1(img, y, x, l, col):
    """inserisce su img un quadrato di lato l con vertice in
    alto a sinistra nel pixel i,j"""
    h, w = len(img), len(img[0])
    for i in range(y, y + l):
        for j in range(x, x + l):
            if i < h and j < w:
                img[i][j] = col


quadrato1(img, 70, 70, 50, (0, 0, 255))
immagini.save(img, "prova.png")

##################################################


def inverti(img):
    """Ritorna una nuova immagine che e'
    l'immagine img con colori invertiti"""
    w, h = len(img[0]), len(img)
    ret = crea(h, w)
    for y in range(h):
        for x in range(w):
            r, g, b = img[y][x]
            ret[y][x] = (255 - r, 255 - g, 255 - b)
    return ret


img = immagini.load("fiore.png")
img1 = inverti(img)
immagini.save(img1, "fiore1.png")

####################################################


def grigio(img):
    """ritorna una nuova immagine che e' l'immagine
    img con i colori in scala di grigi.
    In questo caso ciascun pixel di colori R,G,B deve avere come
    colore la loro media"""
    h, w = len(img), len(img[0])
    img1 = crea(h, w)
    for y in range(h):
        for x in range(w):
            c = round(sum(img[y][x]) / 3)
            img1[y][x] = c, c, c
    return img1


img = immagini.load("fiore.png")
img1 = grigio(img)
immagini.save(img1, "fiore1.png")
