def es17(ls, k):
    """
    Es 7: 6 punti
    progettare la funzione es17(ls,k) che:
    - riceve  in input una lista di parole ls ed un intero k
    - cancella da ls le parole che contengono almeno k  caratteri uguali (sia in maiuscolo che in minuscolo)
    - restituisce il numero di parole cancellate da ls.
    Nota che al termine della funzione la lista passata come parametro deve risultare modificata
    (ricorda che le liste sono mutabili).
     ESEMPI:
     Se ls=[ 'ananas', 'pera', 'banana', 'melone', 'kiwi','albicocca'] e k=3
     la funzione restituisce 3 e la lista ls diventa ['pera', 'melone', 'kiwi']
     Se ls=[ 'Angelo', 'Andrea', 'Osvaldo', 'Anna', 'Monica', 'Adele'] e k=2
     la funzione restituisce 4 e la lista ls diventa ['Angelo', 'Monica']
    """
    lista = []
    for elem in ls:
        insieme = set(elem.lower())
        for item in insieme:
            if elem.lower().count(item) >= k:
                lista.append(elem)
    print(lista)
    for i in range(len(ls)):
        if ls[i] in lista:
            ls[i] = None
    remaining = [item for item in ls if item != None]
    result = len(ls) - len(remaining)
    ls.clear()
    ls.extend(remaining)
    return result


ls = ["Angelo", "Andrea", "Osvaldo", "Anna", "Monica", "Adele"]

print(es17(ls, 2))
