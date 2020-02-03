def es56(tabella):
    '''
    la funzione es56(tabella) che presa in input:
    - una tabella  di interi (rappresentata tramite lista di liste in cui ciascuna lista e' 
    una riga della tabella) restituisce la lista con gli interi che occorrono il massimo 
    numero di volte nella tabella e modifica la tabella distruttivamente. 
    La lista restituita deve risultare  ordinata in modo crescente. Al termine della funzione, 
    nella tabella i numeri che occorrevano un numero massimo di volte devono risultare sostituiti dal 
    carattere '*'.
    Ad esempio per tabella= [[3,2,1,3],[2,1,3,5],[1,3,2,1]] al termine della funzione la lista 
    restituita e' [1,3] e la tabella diviene [[*,2,*,*],[2,*,*,5],[*,*,2,*]] 
    '''
    diz={}
    for y in range(len(tabella)):
        for x in range(len(tabella[0])):
            e = tabella[y][x]
            if e not in diz: diz[e] = 1
            else: diz[e]+=1
    d = {}
    for k,v in diz.items():
        if v not in d: d[v] = [k]
        else: d[v].append(k)
    ls = d[max(d.keys())]
    for y in range(len(tabella)):
        for x in range(len(tabella[0])):
            if tabella[y][x] in ls:
                tabella[y][x] = '*'
    return sorted(ls)
