import os

def es71(dirr, minimo, massimo):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es71(dir, minimo, massimo)
    che cerca nella directory dirr i files che hanno una dimensione compresa tra minimo e massimo (inclusi).
    La funzione deve tornare un dizionario che contiene come chiavi i nomi dei files individuati (senza path),
    e come valori le corrispondenti profondita' (contando la directory 'dirr' iniziale come profondita' 0)
    Nel caso in cui un nome di file sia presente a profondita' diverse, il dizionario deve contenere quella maggiore.
    Nota: per individuare la dimensione del file potete usare la funzione os.stat

    Test:   date alcune directory contenenti files di dimensioni varie a varie profondita',
            controllare che il risultato sia il dizionario corretto
    Test:   che la funzione sia ricorsiva
    """
    lista = recursion(dirr,minimo,massimo,0,[])
    lista = list(set(lista))
    lista = [(os.path.basename(item[0]),item[1]) for item in lista]
    diz = {}
    for elem in lista:
        if not elem[0] in lista: diz[elem[0]] = elem[1]
        else: 
            val = diz[elem[0]]
            if elem[1] > val:
                diz[elem[0]] = val
    return diz
    
def recursion(d,mi,ma,pro,l):
    if os.path.isfile(d):
        if mi<=os.stat(d).st_size and os.stat(d).st_size<=ma:
            return [(d,pro)]
    elif os.path.isdir(d):
        for elem in os.listdir(d):
            if os.path.isdir(d+'/'+elem): c = 1
            else: c = 0
            l.extend(recursion(d+'/'+elem,mi,ma,pro+c,l))
    return l

es71('t4',0,40)