import os
import os.path


def es70(dirs, estensioni, parole):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es70(dir, estensioni, parole),
    che deve contare quante volte le parole indicate sono presenti nei files che NON hanno le estensioni indicate,
    e che riceve come argomenti:
        dir: la directory in cui cercare
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che evitiamo)
        parole: una lista di stringhe che non contengono spazi/tab/accapo, che vanno cercate nei files
                senza considerare la differenza tra maiuscole e minuscole.
    La funzione deve tornare un dizionario contenente come chiavi le parole cercate (in minuscolo)
    e come valori il numero di volte (>0) che queste parole appaiono (indipendentemente dalle maiuscole/minuscole)
    complessivamente nei files che NON hanno le estensioni indicate.
    Nota: una parola non deve apparire nel dizionario in output se nessun file con estensione diversa da quelle indicate la contiene.
    Nota: assumete che tutti i file presenti nelle directories siano file di testo indipendentemente dalla loro estensione.

    Test:   date alcune directory che contengono alcuni file con estensioni diverse a diverse profondita',
            contare alcune parole (in mixed-case) e controllare il dizionario risultante
    Test:   che la funzione sia ricorsiva
    """
    lista = recursion(dirs, [])
    utili = []
    ins = set()
    for elem in lista:
        for est in estensioni:
            if elem[-len(est) :] == est:
                ins.add(elem)
    tutti = set(lista)
    utili = list(tutti.difference(ins))
    diz = {}
    for elem in utili:
        with open(elem) as f:
            text = f.read()
        for par in parole:
            if par.lower() in text.lower():
                if par.lower() not in diz:
                    diz[par.lower()] = 1
                else:
                    diz[par.lower()] += 1
    return diz


def recursion(d, l):
    if os.path.isfile(d):
        l.append(d)
    elif os.path.isdir(d):
        for elem in os.listdir(d):
            path = d + "/" + elem
            recursion(path, l)
    return l


es70("t3", ["txt", "testo"], ["PaperIno", "MINNIE", "EdI"])
