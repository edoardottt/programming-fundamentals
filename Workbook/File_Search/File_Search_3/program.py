import os

def es71(dirs, minimo, massimo):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es71(dir, minimo, massimo)
    che cerca nella directory dir  i files che hanno una dimensione compresa tra minimo e massimo (inclusi).
    La funzione deve tornare un dizionario che contiene come chiavi i nomi dei files individuati (senza path),
    e come valori le corrispondenti profondita' (contando la directory 'dir' iniziale come profondita' 0)
    Nel caso in cui un nome di file sia presente a profondita' diverse, il dizionario deve contenere quella maggiore.
    Nota: per individuare la dimensione del file potete usare la funzione os.stat

    Test:   date alcune directory contenenti files di dimensioni varie a varie profondita',
            controllare che il risultato sia il dizionario corretto
    Test:   che la funzione sia ricorsiva
    """
    diz = rec(dirs,minimo,massimo,{},0)
    result = {}
    for k,v in diz.items():
        if len(v)>1: result[k]=sorted(v,reverse=True)[0]
        else: result[k] = v
    return result
    
def rec(d,mi,ma,diz,pro):
    if os.path.basename(d)[0]=='.': return diz
    if os.path.isfile(d):
        dim = os.stat(d).st_size
        if mi<=dim<=ma:
            d = os.path.basename(d)
            if d in diz: diz[d].append(pro)
            else: diz[d] = [pro]
            return diz
    else:
        for elem in os.listdir(d):
            path = d+'/'+elem
            if os.path.isdir(path):
                p = 1
            else: p = 0
            diz = rec(path,mi,ma,diz,pro+p)
    return diz

print(es71('t4', 0, 100))