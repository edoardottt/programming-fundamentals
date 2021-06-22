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
    d = rec(path, {}, 0)
    for k in d:
        d[k] = abs(max(d[k]) - min(d[k]))
    return d


def rec(p, d, pro):
    if os.path.isfile(p):
        est = p[-3:]
        if est not in d:
            d[est] = (pro, pro)
        else:
            d[est] = (min(d.get(est)[0], pro), max(d.get(est)[1], pro))
        return d
    elif os.path.isdir(p):
        for elem in os.listdir(p):
            path = p + "/" + elem
            if os.path.basename(path)[0] == ".":
                continue
            if os.path.isdir(path):
                pr = 1
            else:
                pr = 0
            d = rec(path, d, pro + pr)
    return d
