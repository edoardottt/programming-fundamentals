import os
import json
import os.path


def es72(dir, jsonFile):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es72(dir, jsonfile) che,
    data una directory, ne legge la struttura costruisce ricorsivamente un dizionario da salvare come Json.
    Argomenti:
        dir:      percorso della directory da leggere
        jsonFile: percorso del file json da scrivere
    Il dizionario deve contenere come chiavi i nomi dei file/directories e come valori:
        - se si tratta di un file, la sua dimensione (intero)
        - se si tratta di una directory, il dizionario che ne descrive il contenuto
    Il dizionario piu' esterno contiene come chiave il solo nome della directory fornita come argomento.
    La funzione inoltre ritorna il massimo numero di files/dir contenuto in una delle directory/sottodirectory.
    """
    diz, conta = rec(dir, {}, 0)
    d = {}
    d[dir] = diz
    with open(jsonFile, "w+") as f:
        json.dump(d, f, indent=4)
    return conta


def rec(dir, diz, conta):
    if os.path.basename(dir)[0] == ".":
        return diz, conta
    if os.path.isfile(dir):
        diz[os.path.basename(dir)] = os.stat(dir).st_size
        return diz, conta
    elif os.path.isdir(dir):
        cont = 0
        for elem in os.listdir(dir):
            cont += 1
            path = dir + "/" + elem
            if os.path.isdir(path):
                diz[os.path.basename(path)], conta = rec(path, {}, 0)
                conta = max(conta, cont)
            else:
                diz, conta = rec(path, diz, conta)
    return diz, conta
