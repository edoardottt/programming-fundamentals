def es21(matrice):
    """
    es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri,
    la restituisce dopo averne ordinato le colonne in ordine lessicografico.
    La matrice passata in input al termine della funzione non deve risultare modificata.
    Ad esempio se la matrice di input e'
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']]
    la funzione restituira' la matrice:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]
    """
    m = [[matrice[i][j] for j in range(len(matrice[0]))] for i in range(len(matrice))]
    for x in range(len(m[0])):
        co = col(m, x)
        for y in range(len(m)):
            m[y][x] = co[y]
    return m


def col(m, x):
    col = []
    for y in range(len(m)):
        col.append(m[y][x])
    return sorted(col)
