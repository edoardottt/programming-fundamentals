"""
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

"""

import os


def es9(pathDir):
    diz = recursion(pathDir, {})
    lista = []
    for v in sorted(set(diz.values()), reverse=True):
        appoggio = []
        for k in sorted(diz.keys()):
            if diz[k] == v:
                appoggio.append((k, v))
        lista.extend(appoggio)
    return lista


def recursion(p, diz):
    if p[0] == ".":
        return 0
    if os.path.isfile(p):
        if p[-3:] == "txt":
            return os.path.getsize(p)
        else:
            return 0
    elif os.path.isdir(p):
        diz[os.path.basename(p)] = 0
        for elem in os.listdir(p):
            if elem[0] != ".":
                if os.path.isdir(p + "/" + elem):
                    diz = recursion(p + "/" + elem, diz)
                elif os.path.isfile(p + "/" + elem):
                    diz[os.path.basename(p)] += recursion(p + "/" + elem, diz)
    return diz


print(es9("Informatica"))
