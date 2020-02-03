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
    words = [elem.strip() for elem in words if len(elem)>1]
    dict = {}
    for word in words:
        k = extract_word(word)
        if k not in dict:
            dict[k] = [word]
        else: dict[k].append(word)
    diz = {}
    for k,v in dict.items():
        lenghts = set()
        res = []
        for elem in v:
            lenghts.add(len(elem))
        for elem in list(reversed(sorted(lenghts))):
            list_elem = [item for item in v if len(item)==elem]
            intermediate = sorted(list_elem)
            res.extend(intermediate)
        diz[k] = res
    return diz
    
def extract_word(parola):
    result = []
    for elem in parola:
        if elem not in 'aeiou':
            result.append(elem)
    res = ''
    for elem in sorted(result):
        res+=elem
    return res