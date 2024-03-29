def es76(parola):
    """
    Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva)
    es76(parola), che presa in input una stringa di caratteri  parola restituisce la lista dei
    suffissi di parola. Gli elementi della lista devono risultare ordinati per lunghezza decrescente .
    Si ricorda che un suffisso di una parola e' quello che si ottiene concellando 0 o piu'
    caratteri iniziali della parola.
    Ad esempio per es76("fondamenti") la lista restituita sara'
    ['fondamenti', 'ondamenti', 'ndamenti', 'damenti', 'amenti', 'menti', 'enti', 'nti', 'ti', 'i']
    """
    lista = ricorsione(parola, [])
    diz = {}
    result = []
    for elem in lista:
        if len(elem) not in diz:
            diz[len(elem)] = [elem]
        else:
            diz[len(elem)].append(elem)
    for elem in list(reversed(sorted(diz.keys()))):
        result.extend(diz[elem])
    return result


def ricorsione(parola, result=[]):
    if len(parola) == 1:
        result.append(parola)
        return result
    else:
        result.append(parola)
        return ricorsione(parola[1:], result)
