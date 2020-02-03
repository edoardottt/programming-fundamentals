def es16(s, k):
    '''
    Es 5: 3 punti
    progettare la funzione es16(s,k) che: 
    - riceve  in input una stringa s di caratteri   ed un intero k 
    - costruisce la lista con  le diverse sottostringhe  di s  in cui compaiono 
      esattamente k caratteri distinti
    - restituisce la lista delle sottostringhe dopo averla ordinata  per
      lunghezze decrescenti e, a parita' di lunghezza, in ordine lessicografico
   Nota che la lista non deve contenere duplicati.
   Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
   caratteri iniziali  e 0 o piu' caratteri finali.
   ESEMPI: 
   con  s='aabbb' e k=1 la funzione restituisce la lista ['bbb', 'aa', 'bb', 'a', 'b']
   cons s='bcafedg' e k=3 la funzione restituisce la lista ['afe', 'bca', 'caf', 'edg', 'fed']
   cons s='ccaabbdd' e k=3 la funzione restituisce la lista 
        ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']
    '''
    insieme = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if len(set(s[i:j]))==k:
                insieme.add(s[i:j])
    lista = list(insieme)
    diz = {}
    for elem in lista:
        if len(elem) not in diz: diz[len(elem)] = [elem]
        else: diz[len(elem)].append(elem)
    ordered_keys = [k for k in reversed(sorted(diz.keys()))]
    result = []
    for elem in ordered_keys:
        ordered_list = sorted(diz[elem])
        result.extend(ordered_list)
    return result