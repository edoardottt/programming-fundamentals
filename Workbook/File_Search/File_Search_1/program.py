import os
import os.path


def es68(dirs, estensioni):
    """
    Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es68(dir, estensioni),
    che deve contare quanti file di certi tipi si trovano in una directory o in una delle sue sottodirectories,
    e che riceve come argomenti
        dir: il path della directory in cui cercare
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
    La funzione deve tornare un dizionario che ha come chiavi le estensioni passate come argomento
    e come valori il numero di file il cui nome termina in quel modo, solo se > 0
    (ovvero, se nessun file con una data estensione appare nella directory o nelle sottodirectories
    la chiave non deve apparire nel dizionario tornato dalla funzione).

    Tests: date alcune directory contenenti file di tipo (ext) diverso, si chiama la funzione per contare alcuni dei tipi di file nelle diverse directory
    Test: che la funzione sia ricorsiva
    """
    diz = {}
    for elem in estensioni:
        diz[elem] = 0
    diz = rec(dirs, estensioni, diz)
    result = {}
    for k in diz.keys():
        if diz[k] != 0:
            result[k] = diz[k]
    return result


def rec(dirs, est, diz):
    if os.path.isfile(dirs):
        for es in est:
            if dirs[-len(es) :] == es:
                diz[es] += 1
    elif os.path.isdir(dirs):
        for elem in os.listdir(dirs):
            rec(dirs + "/" + elem, est, diz)
    return diz
