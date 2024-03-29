def es45(parola1, parola2):
    """
    progettare la funzione es45(parola1,parola2) che
    prende in input due  stringhe di caratteri parola1 e parola2, e restituisce
    la lista delle sottostringhe che risultano in comune ad entrambe le parole.
    La lista delle sottostringhe comuni deve essere ordinata
    lessicograficamente e non deve contenere duplicati.
    Si ricorda che una sottostringa e' quello che si ottiene da una stringa
    eliminando 0 o piu' caratteri all'inizio e 0 o piu' caratteri alla fine

    Ad esempio:
    con  parola1='aabbccdd' parola2='acccdzza' la funzione restituisce la lista [a,c,cc,ccd,cd,d]
    """
    ins1 = set()
    for i in range(len(parola1)):
        for j in range(i + 1, len(parola1) + 1):
            ins1.add(parola1[i:j])
    ins2 = set()
    for i in range(len(parola2)):
        for j in range(i + 1, len(parola2) + 1):
            ins2.add(parola2[i:j])
    return sorted(list(ins1 & ins2))
