def es78(parola):
    '''
    Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva)  
    es78(parola), che presa in input una stringa di caratteri  parola restituisce la lista delle  
    diverse "sottoparole crescenti"  di parola. Le sottoparole devono comparire nella lista in ordine lessicografico.
    Si ricorda che una sottoparola e' quello che si ottiene da una parola concellandone 0 o piu'
    caratteri (in testa, in coda o nel mezzo).
    Inoltre una sottoparola si dice crescente se i caratteri che la compongono
    letti da sinistra  a destra risultano ordinati lessicograficamente.
    
    Ad esempio  la lista restituita da es78('zanzara') sara'
    ['a', 'aa', 'aaa', 'aar', 'an', 'anr', 'anz', 'ar', 'az', 'n', 'nr', 'nz', 'r', 'z', 'zz']
    '''
    lista = recursion('',set(parola),[set(parola)],len(parola))
    print(lista)
    

def recursion(p,k,l,ll):
    pass
    

def crescente(p):
    if len(p)==1: return True
    if len(p)==0: return False
    for i in range(len(p)-1):
        if p[i]<p[i+1]:
            return False
    return True

es78('zanzara')