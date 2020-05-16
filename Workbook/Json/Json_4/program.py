import json

def es34(fname1, fname2):
    '''  
    Un quadrato latino e' una scacchiera quadrata di lato N con un simbolo (scelto in un insieme di N elementi)
    su ogni casella in modo che ognuno dei simboli compaia una e una sola volta in ogni riga e in ogni colonna.
    Implementate la funzione es34(fname1,fname2) che prende in input l'indirizzo fname1 di un file json in cui e'
    contenuto un quadrato latino privato dell'ultima riga e dell'ultima colonna. 
    La scacchiera e' rappresentata come lista di liste. Bisogna completare il quadrato latino e 
    registrarlo come file json all'indirizzo fname2. 
    La funzione deve poi restituire l'insieme dei simboli che compaiono nel quadrato latino.
    Ad esempio: se la lista di liste in fname1 con il quadrato latino parziale e'
    [['X','1'],['?','X']] allora, l'insieme  con i simboli del quadrato latino sara' 
    {'X','1','?'} e la lista di liste in fname2 con il quadrato latino completo sara' 
    [['X','1','?'],['?','X','1'],['1','?','X']]
    Nota: assumete che sia sempre N>2
    '''
    with open(fname1) as f:
        m = json.load(f)
    elem = set()
    for el in m:
        elem = elem | set(el)
    mm = [[0 for e in range(len(m[0]) +1)] for j in range(len(m)+1)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            mm[i][j] = m[i][j]
    for i in range(len(mm)):
        for j in range(len(mm[0])):
            if mm[i][j]==0:
                elems = elementi(mm,i,j)
                el = elem - elems
                mm[i][j] = list(el)[0]
    with open(fname2,'w+') as f:
        json.dump(mm,f)
    return elem
                
def elementi(m,i,j):
    colonna = set()
    riga = set()
    for ii in range(len(m)):
        if m[ii][j]!=0:
            colonna.add(m[ii][j])
    for jj in range(len(m[0])):
        if m[i][jj]!=0:
            riga.add(m[i][jj])
    return colonna | riga