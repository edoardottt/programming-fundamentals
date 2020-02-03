import os

def es35(dir1, parole):
    """
    Si definisca la funzione  es35(dir1, parole), che presi in input:
        dir1:   il path di una directory
        parole: un insieme di parole (stringhe di caratteri tra 'a' e 'z')
    esegue il seguente lavoro:
    Ricerca solo nella directory il cui path e'  dir1  (e non nelle sottodirectories)
    eventuali file con estensione .txt contenenti
    stringhe appartenenti all'insieme delle parole e restituisce un dizionario delle parole trovate.
    Nel dizionario restituito devono comparire  solo le parole effettivamente riscontrate all'interno
    dei file con estensione .txt presenti in dir1 e ciascuna chiave deve avere 
    come attributo una tupla  di due interi.
    Il primo elemento della tupla riporta il numero complessivo di volte che la
    parola  e' stata ritrovata in questi file in dir1,
    il secondo elemento della tupla riporta il numero di diversi file di dir1 
    in cui la parola e' risultata presente.
    Per parola intendiamo una sequenza di lunghezza massimale di caratteri tra 'a' e 'z'. 
    Si puo' assumere che tutti i file con estensione .txt contengono solo parole
    separate da  spazi, tab o andate a capo.
    (non sono presenti caratteri maiuscoli o segni di interpunzione)
    """
    files = []
    for elem in os.listdir(dir1):
        path=dir1+'/'+elem
        if path[-3:]=='txt':
            files.append(path)
    diz = {}
    for file in files:
        with open(file) as f:
            text = f.read()
        for par in parole:
            if par not in diz: 
                if counter(text,par)>0:
                    diz[par] = (counter(text,par),set([file]))
            else:
                count = diz[par][0] + counter(text,par)
                sett = diz[par][1]
                if counter(text,par)>0:
                    sett.add(file)
                diz[par] = (count,sett)
    for k,v in diz.items():
        if v[0] >0:
            diz[k] = (v[0],len(v[1]))
    return diz

def counter(text,a):
    count = 0
    for elem in text.split():
        if elem==a: count+=1
    return count
    
    
    
    
    
    
    
    
    
    
    
    
    
    