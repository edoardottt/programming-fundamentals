def es31(fname1,fname2):
    ''' 
    Implementate la funzione es31(fname1,fname2) che prende in input l'indirizzo di due  file di testo.
    Il testo del primo file va modificato come segue:
    - ciascun carattere tra 'a' e 'z' (minuscoli) che compare nel file in un numero dispari di parole
    (una parola e' una sequenza massimale di caratteri diversi dallo spazio, tab o a capo)
    va sostituito dal corrispondente carattere maiuscolo.
    Il file cosi' ottenuto va poi registrato all'indirizzo fname2.
    La funzione deve restituire quanti dei 26 caratteri tra 'a' e 'z' 
    da minuscoli son diventati maiuscoli nella trasformazione del file di testo. 
    Ad esempio se 
    - il file fname1 contiene  il testo 'Monti, Sterbini e Spognardi'
    - il file fname2 conterra' il testo 'MoNtI, SterBINI e SPoGNArDI'
    il valore restituito dalla funzione sara' 7 (le lettere cambiate sono NIBPGAD)
    '''
    with open(fname1) as f:
        text = f.read()
    testo_inv = text
    text = text.split()
    text = [word.replace(',','') for word in text]
    diz = {}
    for elem in text:
        for char in set(elem):
            if char!=char.upper() and char in set(elem):
                if char not in diz: diz[char] = 1
                else: diz[char]+=1
    sett = set()
    for k in diz.keys():
        if diz[k]%2==1:
            sett.add(k)
    for k in sett:
            testo_inv = testo_inv.replace(k,k.upper())
    with open(fname2,'w+') as f:
        f.write(testo_inv)
    return len(sett)

print(es31('ftesto3.txt','risposta3.txt')) 