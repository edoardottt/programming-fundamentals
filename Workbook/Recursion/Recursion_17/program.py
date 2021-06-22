import os
import json
import os.path


def es72(dir, jsonFile):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva)
    es72(dir, jsonfile) che, data una directory, ne legge la struttura costruisce
    ricorsivamente un dizionario da salvare come Json.
    Argomenti:
        dir:      percorso della directory da leggere
        jsonFile: percorso del file json da scrivere
    Il dizionario deve contenere come chiavi i nomi dei file/directories e come valori:
        - se si tratta di un file, la sua dimensione (intero)
        - se si tratta di una directory, il dizionario che ne descrive il contenuto
    Il dizionario piu' esterno contiene come chiave il solo nome della
    directory fornita come argomento.
    La funzione inoltre ritorna il massimo numero di files/dir
    contenuto in una delle directory/sottodirectory.
    """
    diz, p = rec({}, dir, 0, 0)
    d = dict()
    d[dir] = diz
    with open(jsonFile, "w+") as f:
        json.dump(d, f)
    return p


def rec(diz, d, p, ma):
    print(d, diz, ma)
    if os.path.basename(d)[0] == ".":
        return diz, p
    if os.path.isfile(d):
        diz[os.path.basename(d)] = os.stat(d).st_size
        return diz, p
    elif os.path.isdir(d):
        cont = 0
        for elem in os.listdir(d):
            cont += 1
            path = d + "/" + elem
            if os.path.isdir(path):
                di, p = rec({}, path, p + 1, ma)
                diz[os.path.basename(path)] = di
            else:
                diz, p = rec(diz, path, p, ma)
            if cont > ma:
                ma = cont
    return diz, ma


print(es72("t3", "test.t3.71.json"))
