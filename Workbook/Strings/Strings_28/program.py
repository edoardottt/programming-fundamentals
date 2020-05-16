def es46(parola):
    '''
    progettare la funzione es46(parola) che usa almeno una funzione ricorsiva e:
    - prende in input una stringa di caratteri parola e, tra tutte le sottostringhe 
    di parola restituisce quella di lunghezza massima che risulti anche palindroma.
    In caso ci siano piu' palindromi a lunghezza massima viene restituita quella che 
    precede lessicograficamente.
    Si ricorda che una sottostringa e' quello che si ottiene da una stringa
    eliminando 0 o piu' caratteri all'inizio e 0 o piu' caratteri alla fine mentre
    una stringa e' palindroma se puo' leggersi indifferentemente da sinistra a destra 
    o viceversa.
    Ad esempio:
    con parola='zzzcdcaaabvv'  la funzione restituira' la stringa palindroma 'aaa'
    con parola='adbbabbcbbaad' la funzione restituira' la stringa palindroma 'abbcbba'
    '''
    pals = set()
    lenmax = 0
    for i in range(len(parola)-1):
        for j in range(i,len(parola)+1):
            if len(parola[i:j])>lenmax:
                if ispal(parola[i:j]):
                    pals = set()
                    pals.add(parola[i:j])
                    lenmax = len(parola[i:j])
            elif len(parola[i:j])==lenmax:
                if ispal(parola[i:j]):
                    pals.add(parola[i:j])
                    lenmax = len(parola[i:j])
    return sorted(pals)[0]

def ispal(s):
    if len(s)==0 or len(s)==1: return True
    else:
        if s[0]==s[-1]: return ispal(s[1:-1])
        else: return False
    