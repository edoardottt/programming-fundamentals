def es41(fname1):
    ''' 
    Data una sequenza S di  interi definiamo sequenza derivata da S la  sequenza
    di n interi dove l'i-esimo 
    elemento e' dato dalla somma dei primi i interi di S.
    Ad esempio:
    la sequenza derivata da 
    S= 2, -3, -4,  4, 4, -5, 3, 1,-1  e'
       2, -1, -5, -1, 3, -2, 1, 2, 1.
    
    Implementate la funzione es41(fname1) che prende in input l'indirizzo fname1
    di un file di testo contenente una 
    sequenza S di interi e restituisce il numero che compare con maggior 
    frequenza nella sequenza derivata da S.
    Nel caso in cui i numeri con maggior frequenza siano piu' di uno viene 
    restituito quello di valore massimo.
    Ad esempio se il file fname contiene la sequenza 
    S= 2, -3, -4,  4, 4, -5, 3, 1, -1   la funzione restituisce il valore 2.
    Nel file fname1, ciascun intero della sequenza  e' separato dal successivo
    da una virgola ed eventuali spazi.
    '''
    with open(fname1) as f:
        sporca = f.read().split(',')
    s = [int(item.strip()) for item in sporca]
    derivata = []
    for i in range(len(s)):
        if i==0: derivata.append(s[0])
        else:
            derivata.append(derivata[i-1]+s[i])
    freq = {}
    for elem in set(derivata):
        frequenza = derivata.count(elem)
        if frequenza not in freq: freq[frequenza] = [elem]
        else: freq[frequenza].append(elem)
    result = sorted(freq[max(freq.keys())],reverse=True)[0]
    return result