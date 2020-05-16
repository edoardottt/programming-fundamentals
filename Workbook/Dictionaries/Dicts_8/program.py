def es36(listaDizionari):
    '''
    Si implementi la funzione es36(listaDizionari) che presi in input una lista di dizionari
    restituisce  un dizionario.
    I dizionari in input della listaDizionari  hanno come  chiave stringhe
    di caratteri tra 'a' e 'z' e come attributo liste di interi.
    Il dizionario restituito deve avere le  chiavi che risultano presenti in tutti i dizionari della  listaDizionari.
    A ciascuna chiave x di questo dizionario e' associata una lista di interi.
    Un intero e' presente nella lista se e solo se e' presente in tutte le liste di attributi della chiave x.
    La lista deve risultare ordinata in modo crescente.

    Ad esempio se la listaDizionari contenente i tre dizionari
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    il dizionario restituito sara' {'a':[3,5],'d':[]}
    '''
    d = {}
    k = set(listaDizionari[0].keys())
    for elem in listaDizionari:
        k = k & set(elem.keys())
    for key in k:
        ls = set(listaDizionari[0][key])
        for elem in listaDizionari:
            v = set(elem[key])
            ls = v & ls
        d[key] = sorted(list(ls))
    return d