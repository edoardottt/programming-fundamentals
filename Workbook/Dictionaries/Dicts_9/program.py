def es37(listaDizionari):
    """
    Si implementi la funzione es37(listaDizionari) che presi in input una lista di dizionari
    restituisce  un dizionario.
    I dizionari della listaDizionari  hanno come  chiave stringhe di caratteri tra 'a' e 'z'
    e come attributo liste di interi.

    Il dizionario restituito deve avere come chiavi le chiavi  comuni ad almeno la meta' dei
    dizionari della lista.
    A ciascuna chiave x di questo dizionario e' associato un insieme.
    Un intero deve essere presente nell'insieme associato ad x se e solo se compare come attributo di x
    in almeno uno dei dizionari della listaDizionari.
    Ad esempio se la listaDizionari contenente i tre dizionari
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    il dizionario restituito sara' {'a':{1,2,3,5},'b':{2,3},'d':{3,4}}
    """
    meta = len(listaDizionari) / 2
    d = {}
    c = []
    for elem in listaDizionari:
        c.extend(elem.keys())
    keys = []
    for key in c:
        ok = good(meta, key, listaDizionari)
        if ok:
            keys.append(key)
    for key in keys:
        sett = set()
        for diz in listaDizionari:
            if key in diz:
                sett = sett | set(diz[key])
        d[key] = sett
    return d


def good(meta, key, listaDizionari):
    count = 0
    for elem in listaDizionari:
        if key in elem:
            count += 1
    return count >= meta
