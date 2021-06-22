def es62(matrice):
    imax = jmax = 0
    for j in range(len(matrice[0])):
        for i in range(len(matrice)):
            if matrice[i][j] >= matrice[imax][jmax]:
                imax = i
                jmax = j
    imin = jmin = 0
    for j in range(len(matrice[0])):
        for i in range(len(matrice)):
            if matrice[i][j] < matrice[imin][jmin]:
                imin = i
                jmin = j
    print(matrice[imin][jmin], imin, jmin, matrice[imax][jmax], imax, jmax)
    m1 = [[matrice[i][j] for j in range(len(matrice[0]))] for i in range(len(matrice))]
    for j in range(len(matrice[0])):
        m1[imin][j] = matrice[imax][j]
        m1[imax][j] = matrice[imin][j]
    for i in range(len(matrice)):
        m1[i][jmin], m1[i][jmax] = m1[i][jmax], m1[i][jmin]
    return m1


print(es62([[52, 0, -4, 19], [5, 10, 10, 52], [25, 1, -95, -80], [-95, 14, 17, 42]]))
