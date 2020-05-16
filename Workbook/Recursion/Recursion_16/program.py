def es46(parola):
    '''
    progettare la funzione es46(parola) che usa almeno una funzione ricorsiva e:
    - prende in input una stringa di caratteri parola e, tra tutte le sottostringhe 
    di parola restituisce quella di lunghezza massima che risulti anche palindroma.
    In caso ci siano piu' palindromi a lunghezza massima viene restituita quella che 
    precede lessicograficamente.
    Si ricorda che una sottostringa e' quello che si ottiene da una stringa
    eliminando 0 o piu' caratteri all'inizio e 0 o piu' caratteri alla fine mentre
    una stringa e' palindroma se puo' leggersi indifferentemente da sinistra a destra o viceversa.

    Ad esempio:
    con parola='zzzcdcaaabvv'  la funzione restituira' la stringa palindroma 'aaa'
    con parola='adbbabbcbbaad' la funzione restituira' la stringa palindroma 'abbcbba'
    '''
    pals = set()
    lenmax = 0
    for i in range(len(parola)):
        for j in range(1,len(parola)+1):
            e = parola[i:j]
            if len(e)>lenmax:
                if ispal(e):
                    pals = set()
                    lenmax = len(e)
                    pals.add(e)
            elif len(e)==lenmax:
                if ispal(e):
                    pals.add(e)
    return sorted(pals,key = lambda x: (-len(x),x))[0]
    
    
    
def ispal(s):
    if len(s)<2: return True
    else: return ispal(s[1:-1]) and s[0]==s[-1]