'''
    Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''

def es11(ftesto):
    with open(ftesto) as f:
        words = f.readlines()
    words = [item.strip() for item in words if len(item)>1]
    diz = {}
    for word in words:
        k = extract(word)
        if k not in diz: diz[k] = [word]
        else: diz[k].append(word)
    result = {}
    for k,v in diz.items():
        result[k] = sorted(v,key = lambda x: (-len(x),x))
    return result

def extract(word):
    res =  []
    for char in word:
        if char not in 'aeiouAEIOU':
            res.append(char)
    ress = ''
    for elem in sorted(res):
        ress+=elem
    return ress
        
print(es11('ft10a.txt'))