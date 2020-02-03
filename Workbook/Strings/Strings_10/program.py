
def es77(parola):
    '''
    Si definisca la funzione NON ricorsiva e che NON faccia uso di funzioni ricorsive
    es77(parola), che presa in input una stringa di caratteri  parola restituisce la lista dei 
    suffissi di parola. Gli elementi della lista devono risultare ordinati per lunghezza crescente.
    Si ricorda che un suffisso di una parola e' quello che si ottiene concellando 0 o piu' 
    caratteri iniziali della parola.
    Ad esempio per es77("fondamenti") la lista restituita sara'
    ['i', 'ti', 'nti', 'enti', 'menti', 'amenti', 'damenti', 'ndamenti', 'ondamenti', 'fondamenti']
    '''
    lista = []
    for i in range(len(parola)):
        lista.append(parola[i:])
    diz = {}
    for elem in lista:
        if len(elem) not in lista: diz[len(elem)] = [elem]
        else: diz[len(elem)].append(elem)
    result = []
    for elem in list(sorted(diz.keys())):
        result.extend(diz[elem])
    return result
    
