def es45(parola1,parola2):
    '''
    progettare la funzione es45(parola1,parola2) che
    prende in input due  stringhe di caratteri parola1 e parola2, e restituisce 
    la lista delle sottostringhe che risultano in comune ad entrambe le parole.
    La lista delle sottostringhe comuni deve essere ordinata 
    lessicograficamente e non deve contenere duplicati.
    Si ricorda che una sottostringa e' quello che si ottiene da una stringa
    eliminando 0 o piu' caratteri all'inizio e 0 o piu' caratteri alla fine

    Ad esempio:
    con  parola1='aabbccdd' parola2='acccdzza' la funzione restituisce la lista
    [a,c,cc,ccd,cd,d]
    '''
    sett = set()
    for i in range(len(parola1)-1):
        for j in range(i+1,len(parola1)+1):
            s = parola1[i:j]
            if s in parola2: sett.add(s)
    return sorted(list(sett))