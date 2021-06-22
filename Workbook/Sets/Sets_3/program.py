def es3(ins1, ins2):
    """
    progettare la funzione es3(ins1, ins2) che:
    - riceve  in input due insiemi  di numeri naturali
    - trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
    - restituisce l'insieme di tutte le triple trovate.
    Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
    varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
    in ordine lessicografico crescente.
    ESEMPIO:
    se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    """
    insieme = set()
    for a in ins1:
        for b in ins1:
            for c in ins1:
                if a != b != c:
                    if a < b < c and a + b + c in ins2:
                        insieme.add((a, b, c))
    diz = {}
    for elem in insieme:
        if sum(elem) not in diz:
            diz[sum(elem)] = [elem]
        else:
            diz[sum(elem)].append(elem)
    result = []
    for k in sorted(diz.keys()):
        result.extend(sorted(diz[k]))
    return result
