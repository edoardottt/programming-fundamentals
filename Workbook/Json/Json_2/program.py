import json


def es39(n, jsonFile):
    """
    Dato un intero n, una matrice a spirale di ordine n e' una matrice  di dimensioni n x n
    che riporta i numeri da 1 a n**2 seguendo un andamento a spirale in senso orario.
    Ad esempio  la matrice a spirale di ordine 4 e'

     1  2  3 4
    12 13 14 5
    11 16 15 6
    10  9  8 7

    si definisca la funzione es39(n, jsonFile), che presi come argomenti:
    - n: intero
    - jsonFile: il path di un file json
    registra in formato json nel file jsonFile una matrice a spirale di ordine n
    rappresentata come lista di liste.
    La funzione deve anche restituire la somma dei valori presenti nelle colonne
    di indice pari della matrice.
    Ad esempio per n=4 il jsonFile conterra'
     [[1,  2,  3, 4],[12, 13, 14, 5],[11, 16, 15, 6], [10,  9,  8, 7]]
     e il valore restituito sara' 74.
    """
    m = [[0 for i in range(n)] for j in range(n)]
    direzioni = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dire = 0
    x, y = 0, 0
    for i in range(1, n * n + 1):
        m[x][y] = i
        newx = x + direzioni[dire][0]
        newy = y + direzioni[dire][1]
        if not (0 <= newx < n and 0 <= newy < n and m[newx][newy] == 0):
            dire = (dire + 1) % 4
            newx = x + direzioni[dire][0]
            newy = y + direzioni[dire][1]
        x, y = newx, newy
    ma = 0
    for j in range(n):
        for i in range(n):
            if j % 2 == 0:
                ma += m[i][j]
    with open(jsonFile, "w+") as f:
        json.dump(m, f)
    return ma
