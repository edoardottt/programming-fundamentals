def es19(ftesto):
    '''
    Es 10: 6 punti
    Una matrice  di interi e' registrata all'interno di un file di testo.
    Il file contiene linee vuote inframmezzate a  linee corrispondenti alle righe della matrice. 
    All'interno  delle linee corrispondenti alle righe della matrice ciascun  intero della 
    riga della matrice compare preceduto da uno o piu' spazi.
    Si veda ad esempio il file fm10_1.txt dove e' registrata la matrice:
     1 20  3 40  5
    60  7  8  9 10
    11 12 13 14 15
    Si definisca la  funzione es19(ftesto) che, 
    - riceve l'indirizzo di un file di testo in cui e' registrata la matrice di interi.
    - restituisce una coppia (tupla) contenente:
        - la matrice nel formato di lista di liste di interi
        - la somma degli elementi della cornice esterna della matrice (prima e ultima riga e prima e ultima colonna)
    Ad esempio per il filefm10_1.txt la funzione es10 deve restituire:
        ([[ 1, 20,  3, 40,  5],
          [60,  7,  8,  9, 10],
          [11, 12, 13, 14, 15]],
          204)
    '''
    with open(ftesto) as f:
        text = f.readlines()
    text = [item.split() for item in text if len(item)>1]
    m = [[int(item) for item in text[i]] for i in range(len(text))]
    res = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            elem = m[i][j]
            if i==0: res+=elem
            elif i==len(m)-1: res+=elem
            elif j==0: res+=elem
            elif j==len(m[0])-1: res+=elem
            print(res,elem)
    result = (m,res)
    return result


print(es19('fm10_1.txt'))