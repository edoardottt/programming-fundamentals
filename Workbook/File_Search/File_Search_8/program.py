import os
import os.path


def es67(path):
    """
    ATTENZIONE: e' VIETATO usare la funzione os.walk o altre funzioni di libreria che
    permettono di cercare tutti i file presenti in una directory.
    (la directory la dovete esplorare voi)

    Si definisca la funzione ricorsiva (o che fa uso di vostre funzioni ricorsive) es67 che:
    - riceve come argomento un path del filesystem
    - esplora ricorsivamente la directory corrispondente e torna un dizionario.
    Il dizionario ha come chiave le estensioni dei file trovati nella directory
    (ovvero gli ultimi 3 caratteri del nome dei file, es: 'txt', 'pdf', 'png').
    Il valore associato a ciascuna chiave K e' la distanza (differenza delle profondita')
    tra il piu' profondo file che ha quella estensione e il meno profondo.
    Assumete che i file contenuti nella directory path siano a profondita' 0.
    Esempio:
    se nella directory con path='A1' sono presenti i soli due file di tipo 'txt'
        A1/a/b/c/d/e/f/g/h/pippo.txt    a profondita' 8    (contando A1 = 0)
        A1/d/f/pappo.txt                a profondita' 2
        risultato contiene la coppia chiave: valore
        'txt' : 6
    """
    diz = rec(path, 0, {})
    res = {}
    for k, v in diz.items():
        res[k] = abs(max(v) - min(v))
    return res


def rec(p, pro, diz):
    if os.path.basename(p)[0] == ".":
        return diz
    if os.path.isfile(p):
        if p[-3:] not in diz:
            diz[p[-3:]] = set([pro])
        else:
            diz[p[-3:]].add(pro)
        return diz
    elif os.path.isdir(p):
        for elem in os.listdir(p):
            path = p + "/" + elem
            if os.path.isdir(path):
                c = 1
            else:
                c = 0
            diz = rec(path, pro + c, diz)
    return diz
